from fastapi import FastAPI, UploadFile, File
import yara
import oletools.olevba
import tempfile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Yara를 사용하여 악성 문서 판별
    rules = yara.compile(filepath='rules/maldocs_index.yar')
    matches = rules.match(data=contents)
    
    # 매칭된 룰의 이름 추출
    matched_rules = [match.rule for match in matches]
    
    # 임시 파일에 업로드된 파일 저장
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(contents)
    temp_file.close()
    
    # Olevba를 사용하여 매크로 추출
    vba = oletools.olevba.VBA_Parser(temp_file.name)
    macros = []
    if vba.detect_vba_macros():
        for (filename, stream_path, vba_filename, vba_code) in vba.extract_macros():
            macros.append({
                "filename": filename,
                "stream_path": stream_path,
                "vba_filename": vba_filename,
                "vba_code": vba_code
            })
    
    return {"filename": file.filename, "matched_rules": matched_rules, "macros": macros}