"""
[조회 조건]
1. http://daum.net 접속
2. '송파 헬리오시티 검색'
3. 다음 부동산 부분에 나오는 결과 정보

[출력 결과]
=========== 매물 1 ===========
거래 : 매매
면적 : 84/59 (공급/전용)
가격 : 165,000(만원)
동 : 214동
층 : 고/23
=========== 매물 2 ===========
...

"""

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : ""}
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("table", attrs ={"class" : "tbl"}).find("tbody").find_all("tr")
for idx, item in enumerate(items):
    columns = item.find_all("td")
    data = [column.get_text().strip() for column in columns]
    print("=" * 11 + "매물" + str(idx + 1) + "=" * 11)
    print("거래 : " + data[0])
    print("면적 : " + data[1] + "(공급/전용)")
    print("가격 : " + data[2] + "(만원)")
    print("동 : " + data[3])
    print("층 : " + data[4])

