"""
[GUI 조건]
1. title : 제목 없음 - Windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비어 있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기
"""

import os
from tkinter import *

root = Tk()
root.title("SONG Memo")
root.geometry("640x480")

filename = "python_gui_basic\mynote.txt"

# 열기
def func_open():
    if os.path.isfile(filename):
        # with open(filename, "r", encoding="utf8") as file:
        #     txt.delete("1.0", END)
        #     txt.insert(END, file.read())
        file = open(filename, "r", encoding="utf8")
        txt.delete("1.0", END)
        txt.insert(END, file.read())
        file.close()

# 저장
def func_save():
    file = open(filename, "w", encoding="utf8")
    file.write(txt.get("1.0", END))
    file.close()

# 메뉴
menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = func_open)
menu_file.add_command(label="저장", command = func_save)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# 편집, 서식, 보기, 도움말 메뉴
menu_edit = Menu(menu, tearoff=0)
menu_doc = Menu(menu, tearoff=0)
menu_w = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_doc)
menu.add_cascade(label="보기", menu=menu_w)
menu.add_cascade(label="도움말", menu=menu_help)

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set) # 여러 줄 가능
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()