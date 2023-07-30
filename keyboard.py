#GUI (Graphical User Interface) using Tkinter

import tkinter as tk
from tkinter import *

win = tk.Tk()

win.title("GUI")
win.geometry("300x200")
'''l=Label(win,text="Arundhati",font=(("Arial",28,"bold")),fg="red",bg="yellow")
l.pack()'''
b1=Button(win,text="Button1",bg="grey",height=1,width=10)
b1.place(y=30,x=20)

b2=Button(win,text="Button2",bg="grey",height=1,width=10)
b2.place(y=30,x=110)

b3=Button(win,text="Button3",bg="grey",height=1,width=10)
b3.place(y=30,x=200)

b4=Button(win,text="Button4",bg="grey",height=1,width=10)
b4.place(y=60,x=60)

b5=Button(win,text="Button5",bg="grey",height=1,width=10)
b5.place(y=60,x=150)

b6=Button(win,text="Button6",bg="grey",height=1,width=10)
b6.place(y=90,x=110)

'''b1=Button(win,text="A",bg="grey",height=1,width=10)
b1.place(y=30,x=100)

b2=Button(win,text="SHIFT",bg="grey",height=1,width=10)
b2.place(y=60,x=50)

b3=Button(win,text="ENTER",bg="grey",height=1,width=10)
b3.place(y=60,x=150)

b4=Button(win,text="CTRL",bg="grey",height=1,width=10)
b4.place(y=90,x=10)

b5=Button(win,text="Spacebar",bg="grey",height=1,width=10)
b5.place(y=90,x=100)

b6=Button(win,text="ALT",bg="grey",height=1,width=10)
b6.place(y=90,x=190)
'''
win.mainloop()
