import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# 같은게 여러개일 경우 for문 사용
# for i in pyautogui.locateOnScreen("checkbox.png")
#     print(i)
#     pyautogui.click(i, duration=0.25)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. grayscale 정확도가 떨어질 수 있다.
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(2292, 522, 200, 300))
# pyautogui.moveTo(trash_icon)
# pyautogui.mouseInfo()

# 3. 정확도 조정
# trash_icon = pyautogui.locateOnScreen("run_btn.png", confidence=0.7) # 70퍼센트
# pyautogui.moveTo(trash_icon)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_noteped = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_noteped:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")
# while file_menu_noteped is None:
#     file_menu_noteped = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# pyautogui.click(file_menu_noteped)

# 2. 일정 시간동안 기다리기(TimeOut)
import time
import sys
# timeout = 10
# start = time.time()
# file_menu_noteped = None
# while file_menu_noteped is None:
#     file_menu_noteped = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout: # 지정 10초가 초과되면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print("f[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()
pyautogui.click(file_menu_noteped)