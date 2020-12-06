from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx = 90, pady = 10, text="button22222222222222") # 크기 동적
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text="button3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text="button444444444444") # 크기 고정
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="python_basic_gui\img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()