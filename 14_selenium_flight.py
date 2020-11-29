import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() # Chrome("위치")
browser.maximize_window # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 29일, 30일 선택
# time.sleep(1)
# browser.find_elements_by_link_text("29")[0].click() # [0] -> 이번달
# time.sleep(1)
# browser.find_elements_by_link_text("30")[0].click() # [0] -> 이번달

# 다음달 29일, 30일 선택
time.sleep(1)
browser.find_elements_by_link_text("29")[1].click() # [0] -> 이번달
time.sleep(1)
browser.find_elements_by_link_text("30")[1].click() # [0] -> 이번달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    # 검색 결과 대기
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행
    # 첫번째 결과 출력
    print(elem.text)
finally:
    browser.quit()
