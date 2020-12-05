from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

txt = Text(root, width=30, height=5) # 여러 줄 가능
txt.pack()
txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width=30) # 한줄만 가능
e.pack()
e.insert(0, "한 줄만 입력하세요.")

def btncmd():
    print(txt.get("1.0", END)) # .get("(라인).(comlum위치)", 어디까지)
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()