#create the calculater

#import the tkinter

from tkinter import *

#create gui window
window=Tk()
window.geometry('300x400')
window.title("Calculator")



#add widget
e=Entry(window,width=40,borderwidth=25,bg="powder blue")
e.place(x=0,y=0)

#def
def btclick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

#create button
b=Button(window,text='7',width=12,bg="sky blue",command=lambda:btclick(7))
b.place(x=10,y=60)
b=Button(window,text='8',width=12,bg="sky blue",command=lambda:btclick(8))
b.place(x=100,y=60)
b=Button(window,text='9',width=12,bg="sky blue",command=lambda:btclick(9))
b.place(x=190,y=60)
b=Button(window,text='4',width=12,bg="sky blue",command=lambda:btclick(4))
b.place(x=10,y=120)
b=Button(window,text='5',width=12,bg="sky blue",command=lambda:btclick(5))
b.place(x=100,y=120)
b=Button(window,text='6',width=12,bg="sky blue",command=lambda:btclick(6))
b.place(x=190,y=120)
b=Button(window,text='1',width=12,bg="sky blue",command=lambda:btclick(1))
b.place(x=10,y=180)
b=Button(window,text='2',width=12,bg="sky blue",command=lambda:btclick(2))
b.place(x=100,y=180)
b=Button(window,text='3',width=12,bg="sky blue",command=lambda:btclick(3))
b.place(x=190,y=180)
b=Button(window,text='0',width=12,bg="sky blue",command=lambda:btclick(0))
b.place(x=10,y=240)

#-------------------------------------------------

def add():
    firstno=e.get()
    global math
    math = 'addition'
    global f
    f=int(firstno)
    e.delete(0,END)


b=Button(window,text='+',width=12,bg="DarkOrange1",command=add)
b.place(x=100,y=240)


def sub():
    firstno = e.get()
    global math
    math='subtration'
    global f
    f = int(firstno)
    e.delete(0, END)


b=Button(window,text='-',width=12,bg="DarkOrange1",command=sub)
b.place(x=190,y=240)


def mul():
    firstno = e.get()
    global math
    math = 'multiplication'
    global f
    f = int(firstno)
    e.delete(0, END)


b=Button(window,text='*',width=12,bg="DarkOrange1",command=mul)
b.place(x=10,y=300)


def div():
    firstno = e.get()
    global math
    math = 'division'
    global f
    f = int(firstno)
    e.delete(0, END)


b=Button(window,text='/',width=12,bg="DarkOrange1",command=div)
b.place(x=100,y=300)


def eq():
    secondno = e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f + int(secondno))
    elif math=='subtration':
        e.insert(0,f - int(secondno))
    elif math=='multiplication':
        e.insert(0,f * int(secondno))
    elif math=='division':
        e.insert(0,f / int(secondno))


b=Button(window,text='=',width=12,bg="SpringGreen2",command=eq)
b.place(x=190,y=300)


def clear():
    e.delete(0, END)


b=Button(window,text='CLEAR',bg="orangeRed2",width=12,command=clear)
b.place(x=100,y=350)




#mainloop
window.mainloop()