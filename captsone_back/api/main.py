from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
import yara
import oletools.olevba
import os
import openai
from firebase_admin import initialize_app, credentials, storage

# Firebase 초기화
cred = credentials.Certificate("/home/ubuntu/server/secmali-firebase-adminsdk-fu5bv-11cf4968bf.json")
firebase_app = initialize_app(cred, options={
    "storageBucket": "secmali.appspot.com"  
})
firebase_storage = storage.bucket()

openai.api_key = "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"
app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), document_id: str = Form(...)):
    # Firebase Storage에서 다운로드 URL 얻기
    blob = firebase_storage.blob(f"uploads/{document_id}/{file.filename}")
    try:
        download_url = blob.generate_signed_url(expiration=3600)  # URL의 만료 시간은 1시간으로 설정
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate download URL: {str(e)}")

    # Firebase Storage에서 파일 다운로드
    try:
        file_contents = blob.download_as_text()  # 텍스트 파일의 경우
        # 또는
        # file_contents = blob.download_as_bytes()  # 바이너리 파일의 경우
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to download file from storage: {str(e)}")

    # Yara를 사용하여 악성 문서 판별
    rules = yara.compile(filepath='rules/maldocs_index.yar')
    matches = rules.match(data=file_contents)

    # 매칭된 룰의 이름 추출
    matched_rules = [match.rule for match in matches]

    # Olevba를 사용하여 매크로 추출
    vba = oletools.olevba.VBA_Parser(file.file, data=file_contents)
    macros = []
    if vba.detect_vba_macros():
        for (filename, stream_path, vba_filename, vba_code) in vba.extract_macros():
            macros.append({
                "stream_path": stream_path,
                "vba_filename": vba_filename,
                "vba_code": vba_code
            })
        vba_codes = [macro["vba_code"] for macro in macros]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a malicious macro code analyst."},
                {"role": "user", "content": vba_codes[0] + "위의 코드가 어떤 행동을 하는지 일반인이 알아듣기 쉽게 말해줘"}
            ]
        )

    # 분석 결과 반환
    return {
        "filename": file.filename,
        "matched_rules": matched_rules,
        "macros": macros,
        "macro_analysis": completion.choices[0].message.content
    }
