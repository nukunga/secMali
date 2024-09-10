from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import initialize_app, credentials, firestore
import requests
import yara
import oletools.olevba
import openai

app = FastAPI()

# Firebase 초기화
cred = credentials.Certificate("/home/ubuntu/server/secmali-firebase-adminsdk-fu5bv-11cf4968bf.json")
firebase_app = initialize_app(cred)
firestore_db = firestore.client()

openai.api_key = ""

# CORS 설정 추가
origins = [
    "http://localhost",  # 로컬 개발 환경
    "http://localhost:8080",  # 다른 포트의 로컬 개발 환경
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze_document/{document_id}")
async def analyze_document(request: Request, document_id: str):
    if not document_id:
        raise HTTPException(status_code=422, detail="Missing document_id in the request path")

    # Firestore에서 다운로드 URL 가져오기
    document_ref = firestore_db.collection("fileUpload").document(document_id)
    document_data = document_ref.get().to_dict()

    if not document_data or "download_url" not in document_data:
        raise HTTPException(status_code=404, detail="Document not found or missing download_url")

    download_url = document_data["download_url"]

    # 파일 다운로드
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        file_contents = response.content
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to download file: {str(e)}")

    # Yara를 사용하여 악성 문서 판별
    rules = yara.compile(filepath='rules/maldocs_index.yar')
    matches = rules.match(data=file_contents)
    matched_rules = [match.rule for match in matches]

    # Olevba를 사용하여 매크로 추출
    vba = oletools.olevba.VBA_Parser(None, data=file_contents)
    macros = []
    if vba.detect_vba_macros():
        for (filename, stream_path, vba_filename, vba_code) in vba.extract_macros():
            macros.append({
                "stream_path": stream_path,
                "vba_filename": vba_filename,
                "vba_code": vba_code
            })

    # OpenAI GPT-4.0을 사용하여 매크로 분석
    if macros:
        vba_codes = [macro["vba_code"] for macro in macros]
        vba_codes_str = "\n".join(vba_codes)
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a malicious macro code analyst."},
                {"role": "user", "content": f"{vba_codes_str}위의 코드가 어떤 행동을 하는지 일반인이 알아듣기 쉽게 말해주고 위험한 파일인지 판별해줘"}
            ]
        )

        macro_analysis = completion.choices[0].message.content
    else:
        macro_analysis = "매크로가 발견되지 않았습니다."

    # 분석 결과를 Firestore에 추가하고 문서 ID를 반환
    result_data = {
        "document_id": document_id,
        "matched_rules": matched_rules,
        "macros": macros,
        "macro_analysis": macro_analysis
    }

    # Firestore에 데이터 추가
    result_ref = firestore_db.collection("analysisResults").add(result_data)

    # 추가한 문서의 ID를 반환
    return {"result_document_id": result_ref.id}
