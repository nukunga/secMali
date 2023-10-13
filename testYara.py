import yara

rules = yara.compile('malware.yar')

matches = rules.match('file_to_scan.exe')

if matches:
    for match in matches:
        print(match.rule)
else:
    print("No matches found.")