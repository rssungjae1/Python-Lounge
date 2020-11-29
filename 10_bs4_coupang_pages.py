import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : ""}

# 참고 사이트 : "https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/"
for i in range(1, 6):
    print("--page : {}".format(i))
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class" : "name"}).get_text())
    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs ={"class" : "ad-badge-text"})
        if ad_badge:
            # print(" <광고 상품 제외>")
            continue
        # 애플 제품 제외
        name = item.find("div", attrs={"class" : "name"}).get_text() # 제품명

        if "Apple" in name:
            # print("<Apple 상품 제외합니다>")
            continue

        price = item.find("strong", attrs={"price-value"}).get_text() # 가격

        # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class" : "rating"}) # 평점
        rate_cnt = item.find("span", attrs={"class" : "rating-total-count"})# 평점 수

        if rate or rate_cnt:
            rate = rate.get_text()
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            rate = "평점 없음"
            rate_cnt = "평점 수 없음"
            # print("<평점 없는 상품 제외합니다>")
            continue
        link = item.find("a", attrs={"class" : "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 50:
            # print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100)
        
        