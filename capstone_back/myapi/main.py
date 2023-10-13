from fastapi import FastAPI, UploadFile, File
import yara
from oletools.olevba import VBA_Parser

app = FastAPI()

# YARA 규칙 파일을 로드
#rules = yara.compile('capstone_back\myapi\rules\maldocs_index.yar')

@app.post("/scan_document/")
async def scan_document(file: UploadFile): # DB서버 연동하여 파일 가져오기
    content = await file.read()
    
    # 파일을 YARA로 스캔
    yara_matches = rules.match(data=content)

    yara_matched_strings = []
    for match in yara_matches:
        yara_matched_strings.append({
            "rule_name": match.rule,
            "offset": match.strings[0][0],
            "matched_content": match.strings[0][2],
        })

    if yara_matches:
        return {"message": "Malicious document detected by YARA", "yara_matches": yara_matched_strings}

    # 파일을 olevba로 스캔하여 매크로 추출
    vba_parser = VBA_Parser(content)
    macro_code = []
    for (subfilename, stream_path, vba_filename, vba_code) in vba_parser.extract_macros():
        macro_code.append({
            "subfilename": subfilename,
            "stream_path": stream_path,
            "vba_filename": vba_filename,
            "vba_code": vba_code
        })

    if macro_code:
        return {"message": "Macros found in the document", "macros": macro_code}
    else:
        return {"message": "No macros found in the document"}

#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="127.0.0.1", port=8000)