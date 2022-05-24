import tkinter

window = tkinter.Tk()
window.title('윈도우창 연습')
window.geometry('400x100')
window.resizable(False,False)

window.mainloop()

from tkinter import *
window = Tk()
window.title("레이블 연습")
label1 = Label(window, text="파이썬 세계 방문을 환영합니다")
label2 = Label(window, text="신한대학교", font=("궁서체", 26), fg="blue")
label3 = Label(window, text="SHINHAN UNIVERSITY", bg="magenta",
width=30, height=10, anchor=SE)
# anchor는 위젯을 표시할 위치(N,NE,E,SE,S,SW,W,NW,CENTER)
label1.pack() # Label.pack()함수로 윈도에 표시
label2.pack()
label3.pack()
window.mainloop()

import tkinter

window = tkinter . Tk()

photo= tkinter.PhotoImage(file = ".gif/dog.gif")
label1 = Label(window,image=photo)
label1.pack()

window.mainloop()
