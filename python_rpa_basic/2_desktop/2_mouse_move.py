import pyautogui

# pyautogui.moveTo(100,100)
# pyautogui.moveTo(100,200, duration= 1) #1초 동안 100,200으로 이동

# 상대좌표
pyautogui.move(100,100, duration= 1)
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)