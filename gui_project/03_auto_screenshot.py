import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기, 사용자가 준비하는 시간

for i in range(1,11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save(r"python_gui_basic\gui_project\img\image{}.png".format(i)) # 파일로 저장
    time.sleep(2)