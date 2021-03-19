from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1080")
options.add_argument("user-agent=")

browser = webdriver.Chrome(options=options) # Chrome("위치")
browser.maximize_window() # 창 최대화

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
# 화면에서 보이는 것

# headless로 크롬 열어서 얻었을때

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()