from tkinter import *

root = Tk()
root.title("SONG Scheduler")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) # 여러개 선택가능
# listbox = Listbox(root, selectmode="single", height=4) # 하나만 선택가능

# height = n n개수만큼 표시
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 앞 항목을 삭제

    # 갯수 확인
    # print("리스트에는 ", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1~3번째 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인 (idx 위치로 반환)
    print("선택된 항목 : ", listbox.curselection())



btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()