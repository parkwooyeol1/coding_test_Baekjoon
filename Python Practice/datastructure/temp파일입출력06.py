# 파일열기
# 변수명 = open("파일경로/파일이름.txt", "모드")


# new_file = open("sample.txt", "w") 
# newf_file.close()
# 유니코드에러 해결 encoding="utf-8"

# with open("sample.txt", "w") as file:


# r  읽기모드
# w  쓰기모드
# a  쓰기, 이어쓰기 모드 (수정)


#data 딕셔너리 저장하는 법
"""
import json 

data = {
    key : value
}

with open("경로.json", "w",encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# 딕셔너리 읽는 법 
import json 

with open("경로.json", "r",encoding="utf-8") as file:
    data = json.load(file)
"""
