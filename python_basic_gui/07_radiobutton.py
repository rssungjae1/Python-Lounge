from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() # 기본값 선택
btn_burger2 = Radiobutton(root, text="치킨 햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치즈 햄버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="레몬에이드", value="레몬에이드", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)
    print(drink_var.get()) # 드링크 중 선택된 라디오 항목의 값(value)

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()