import os
import sys
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

label1 = Label(root, text="hi")
label1.pack()

photo = PhotoImage(file=resource_path("python_basic_gui\img.png"))
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="hi, again")

    global photo2
    photo2 = PhotoImage(file=resource_path("python_basic_gui\img2.png"))
    label2.config(image=photo2)
btn = Button(root, text="동작하는 버튼", command=change)

btn.pack()

root.mainloop()