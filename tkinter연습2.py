import tkinter

window = tkinter . Tk()

photo= tkinter.PhotoImage(file = "./gif/dog.gif")
label1 = tkinter. Label(window,image=photo)
label1.pack()

window.mainloop()
