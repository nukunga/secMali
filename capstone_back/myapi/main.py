from fastapi import FastAPI, UploadFile
from typing import List

app = FastAPI()

@app.post("/analyze/")
async def analyze_files(files: List[UploadFile]):
    analysis_results = []

    for file in files:
        # 파일을 어딘가에 저장하고 분석에 사용할 준비를 합니다.
        with open(file.filename, "wb") as f:
            f.write(file.file.read())

        # YARA 및 olevba를 사용하여 파일을 분석하고 결과를 얻습니다.
        # 이 부분은 YARA 및 olevba를 사용하여 분석하는 코드로 대체해야 합니다.

        result = {"filename": file.filename, "analysis_results": analysis_results}
        analysis_results.append(result)

    return {"results": analysis_results}
