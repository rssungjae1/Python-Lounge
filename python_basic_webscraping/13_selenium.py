import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
browser = webdriver.Chrome() # Chrome("위치")

# 네이버 로그인 실패시 캡챠 우회하기 https://hogni.tistory.com/71

# 1. 네이버 이동
browser.get("http://naver.com")

# browser.back()
# browser.forward()
# browser.refresh()
# elem = browser.find_element_by_id("query")
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_tag_name("a")
# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     e.get_attribute("href")
# browser.get("http://daum.net")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")


# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
pyperclip.copy("")
browser.find_element_by_id("id").send_keys(Keys.CONTROL, 'v')
time.sleep(1)
pyperclip.copy("")
browser.find_element_by_id("pw").send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 4. 로그인 버튼 클릭
elem = browser.find_element_by_id("log.login").click()

time.sleep(3)

# # 5. id를 새로 입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 해당 탭 닫기
# browser.quit() # 전체 닫기