from fastapi import FastAPI, UploadFile
import yara
import olevba

app = FastAPI()
yara_rules = yara.compile("capstone_back\myapi\yaraRule\rules\maldocs_index.yar")

@app.post("/analyze/")
async def analyze_files():
    result = []
    matches = rules.match('file_to_scan.exe') # DB연결하여 업로드 된 파일 가져오기
    
    if matches:
        for match in matches:
            result += match.rule + "\n"
    else:
         result = "파일이 안전합니다."

    return {result}
