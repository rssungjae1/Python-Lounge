import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocodisng.tistory.com")
res.raise_for_status() # 문제가 있을경우 에러처리
# print("응답코드 :", res.status_code ) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)