"""
[조건]
1. 네이버에서 오늘 서울의 날씨정보를 가져온다
2. 헤드라인 뉴스 3건을 가져온다
3. IT 뉴스 3건을 가져온다
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다

[출력 예시]

[오늘의 날시]
흐림, 어제보다 00도 높아요
현재 00도 (최저 00도 / 최고 00도)
오전 강수확률 00퍼센트 / 오후 강수확률 00퍼센트

미세먼지 00~ 좋음
초미세먼지 00~ 좋음

[헤드라인 뉴스]
1. ~~...
(링크 : ~)
2. ~~...
(링크 : ~)

[IT 뉴스]
1. 무슨 무슨일이~
(링크 : ~)

[오늘의 영어 회화]
(영어 지문)
~
(한글 지문)
~
"""
import requests
import re
from bs4 import BeautifulSoup
#########################################################################################
def scrape_weather_seoul(weather_url, headers):
    # 서울 날씨
    res = requests.get(weather_url, headers = headers)
    res.raise_for_status()
    weather = BeautifulSoup(res.text, "lxml")

    case = weather.find("p", attrs ={"class" : "cast_txt"}).get_text()
    todaytemp = weather.find("span", attrs ={"class" : "todaytemp"}).get_text()
    tempmark = weather.find("span", attrs ={"class" : "tempmark"}).get_text().replace("도씨","")
    min_temp = weather.find("span", attrs ={"class" : "min"}).get_text()
    max_temp = weather.find("span", attrs ={"class" : "max"}).get_text()
    morning_rain_rate = weather.find("span", attrs ={"class" : "point_time morning"}).find("span", attrs ={"class" : "rain_rate"}).get_text()
    afternoon_rain_rate = weather.find("span", attrs ={"class" : "point_time afternoon"}).find("span", attrs ={"class" : "rain_rate"}).get_text()
    dd = weather.find("dl", attrs = {"class" : "indicator"}).find_all("dd")

    print("[오늘의 날시]")
    print(case)
    print(f"현재 {todaytemp}{tempmark} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전{morning_rain_rate} / 오후{afternoon_rain_rate}")
    print("")
    print(f"미세먼지 {dd[0].get_text()}")
    print(f"초미세먼지 {dd[1].get_text()}")
    print("")
#########################################################################################
def scrape_headline_news(news_url, headers):
    # 헤드라인 뉴스
    res = requests.get(news_url, headers = headers)
    res.raise_for_status()
    news = BeautifulSoup(res.text, "lxml")

    news_headline = news.find_all("div", attrs ={"class" : "hdline_article_tit"})

    print("[헤드라인 뉴스]")
    for new in range(0, len(news_headline)):
        print(f"{new+1}. {news_headline[new].get_text().strip()}")
        print("https://news.naver.com/" + news_headline[new].find("a")["href"])
    print("")
#########################################################################################
def scrape_headline_it_news(it_news_url, headers):
    # IT 뉴스
    res = requests.get(it_news_url, headers = headers)
    res.raise_for_status()
    it_news = BeautifulSoup(res.text, "lxml")

    it_news_headline = it_news.find("ul", attrs ={"class" : "type06_headline"}).find_all("li", limit=5)
    print("[IT 뉴스]")
    for idx, headline in enumerate(it_news_headline):
        # 사진 제외
        headlines = headline.find_all("dt")
        for i in headlines:
            if i.find("img"):
                continue
            else:
                print(f"{idx + 1}. {i.get_text().strip()}")
                print(i.find("a")["href"])
    print("")
#########################################################################################
# 해커스 매일 영어회화 학습
def hackers(hackers_url, headers):
    res1 = requests.get(hackers_url, headers = headers)
    res1.raise_for_status()
    hackers = BeautifulSoup(res1.text, "lxml")
    today_englishs = hackers.find_all("div", attrs ={"id" : re.compile("^conv_kor_t")})
    print("[오늘의 영어 회화]")
    print("(영어 지문)")
    for today_english in today_englishs[len(today_englishs)//2:]:
        print(today_english.get_text().strip())
    print("")
    print("(한글 지문)")
    for today_english in today_englishs[:len(today_englishs)//2]:
        print(today_english.get_text().strip())
    print("")
#########################################################################################
# 출력
headers = {"User-Agent" : ""}
weather_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
news_url = "https://news.naver.com/"
it_news_url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
hackers_url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english#"

if __name__ == "__main__":
    scrape_weather_seoul(weather_url, headers)
    scrape_headline_news(news_url, headers)
    scrape_headline_it_news(it_news_url, headers)
    hackers(hackers_url, headers)




