from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

label1 = Label(root, text="hi")
label1.pack()

photo = PhotoImage(file="python_gui_basic\img.png")
photo2 = PhotoImage(file="python_gui_basic\img2.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="hi, again")

    global photo2
    photo2 = PhotoImage(file="python_gui_basic\img2.png")
    label2.config(image=photo2)
btn = Button(root, text="동작하는 버튼", command=change)

btn.pack()

root.mainloop()