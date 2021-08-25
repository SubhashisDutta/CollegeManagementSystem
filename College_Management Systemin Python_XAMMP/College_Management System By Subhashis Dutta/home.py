from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import ImageTk
def addstudent():
	rt.destroy()
	import addstudent
def student():
	rt.destroy()
	import student
def login():
	rt.destroy()
	import login
def login1():
	rt.destroy()
	import login1
def login2():
	rt.destroy()
	import login2
def reg_win():
	rt.destroy()
	import register

rt=Tk()
rt.title("Home Page")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Welcome To NSEC College",font=("constantia",30,"bold"),bg="black",fg="yellow")
reg.place(x=50,y=30,width=700)
b1=Button(frame,text="STUDENT LOGIN",command=login1,font=("times new roman",15,"bold"),bg="white")
b1.place(x=60,y=115)
b2=Button(frame,text="ADMINISTRATOR LOGIN",command=login,font=("times new roman",15,"bold"),bg="white")
b2.place(x=250,y=115)
b3=Button(frame,text="PROFESSOR LOGIN",command=login2,font=("times new roman",15,"bold"),bg="white")
b3.place(x=520,y=115)

b5=Button(frame,text="Register",command=reg_win,font=("times new roman",15,"bold"),bg="white")
b5.place(x=60,y=160)

bg6=ImageTk.PhotoImage(file="c.jpg")
bglb2=Label(frame,image=bg6)
bglb2.place(x=192,y=210,width=350,height=350)
rt.mainloop()