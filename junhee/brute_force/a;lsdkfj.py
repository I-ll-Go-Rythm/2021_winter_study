from tkinter import *
win = Tk()# 창 생성
win.geometry("1000x500") #창크기설정 픽셀단위
win.title("calculator")
win.option_add("*Font","맑은고딕 25")
labl = Label(win, text = "아이디")
labl.pack()
text = Entry(win)
text.pack()
btn = Button(win, text ="버튼")
btn.pack()
win.mainloop()#창 실행