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