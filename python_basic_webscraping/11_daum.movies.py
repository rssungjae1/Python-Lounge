import requests
import re
from bs4 import BeautifulSoup

for year in range(2015,2020):
    headers = {"User-Agent" : ""}
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)
        image_res = requests.get(image_url, headers = headers)
        image_res.raise_for_status()

        with open("./webscraping_basic/images/{0}_movie{1}.jpg".format(year, idx + 1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4: # (0~4)
            break

