import pyautogui
# pyautogui.mouseInfo()

# 화면 끝에가면 예외처리되고 종료되는 문제를 해결, 그러나 추천하지는 않음
# pyautogui.FAILSAFE = False

# 모든 동장에 1초씩 sleep 적용
# pyautogui.PAUSE = 1 

for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)