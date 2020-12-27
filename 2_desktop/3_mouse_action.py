import pyautogui

# p = pyautogui.position()
# pyautogui.sleep(3) # 3초 대기
# print(p.x, p.y)

# pyautogui.click(1321, 19, duration=1) # 1321,19좌표를 마우스 클릭
# pyautogui.click()

# 드래그 드랍
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# 더블 클릭
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)

# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown()
# pyautogui.moveTo(200,300)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# pyautogui.sleep(2)
# pyautogui.drag(100,100, duration = 0.25) # 빠른 동작으로 drag 수행이 안될때는 duration 지정
# pyautogui.dragTo() # 절대좌표 드래그

pyautogui.scroll(300) # 양수이면 윗방향, 음수이면 아래방향으로