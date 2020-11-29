import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent" : ""
    ,"Accept-Language":"ko-KR,ko"}

res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

for movie in movies:
    title = movie.find("div", attrs ={"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)
# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html파일을 예쁘게 출력