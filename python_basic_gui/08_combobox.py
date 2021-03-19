import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)] # 1~31
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")       

# 읽기 전용의 콤보 박스
readonly_combobox = ttk.Combobox(root, height=5, values=values, state="readonly") 
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="choice", command=btncmd)
btn.pack()

root.mainloop()