from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import ImageTk

def student():
	rt.destroy()
	import student
def viewca():
	rt.destroy()
	import viewca
def viewlabmarks():
	rt.destroy()
	import viewlabmarks
def viewattendance():
	rt.destroy()
	import viewattendance
def viewlibrary():
	rt.destroy()
	import viewlibrary
def viewfees():
	rt.destroy()
	import viewfees
def viewplace():
	rt.destroy()
	import viewplace

rt=Tk()
rt.title("student")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Check Your Details",font=("constantia",30,"bold"),bg="black",fg="yellow")
reg.place(x=50,y=30,width=700)
b1=Button(frame,text="Personal Details",command=student,font=("times new roman",15,"bold"),bg="white")
b1.place(x=130,y=115)
b2=Button(frame,text="CA Marks",command=viewca,font=("times new roman",15,"bold"),bg="white")
b2.place(x=290,y=115)
b3=Button(frame,text="Lab Marks",command=viewlabmarks,font=("times new roman",15,"bold"),bg="white")
b3.place(x=400,y=115)
b5=Button(frame,text="Fees Details",command=viewfees,font=("times new roman",15,"bold"),bg="white")
b5.place(x=520,y=115)
b4=Button(frame,text="Attendance",command=viewattendance,font=("times new roman",15,"bold"),bg="white")
b4.place(x=130,y=160)
b5=Button(frame,text="Library",command=viewlibrary,font=("times new roman",15,"bold"),bg="white")
b5.place(x=260,y=160)
b5=Button(frame,text="Placement",command=viewplace,font=("times new roman",15,"bold"),bg="white")
b5.place(x=350,y=160)
bg4=ImageTk.PhotoImage(file="c.jpg")
bglb2=Label(frame,image=bg4)
bglb2.place(x=192,y=210,width=350,height=350)
rt.mainloop()