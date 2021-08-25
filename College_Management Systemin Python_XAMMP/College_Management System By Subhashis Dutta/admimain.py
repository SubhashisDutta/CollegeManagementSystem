from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import ImageTk

def addstudent():
	rt.destroy()
	import addstudent
def teacher():
	rt.destroy()
	import teacher
def fees():
	rt.destroy()
	import fees
def library():
	rt.destroy()
	import library
def place():
	rt.destroy()
	import place

rt=Tk()
rt.title("ADMISTRATOR")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Netaji Subhash Engineering College",font=("constantia",30,"bold"),bg="black",fg="yellow")
reg.place(x=50,y=30,width=700)
b1=Button(frame,text="Students Profile",command=addstudent,font=("times new roman",15,"bold"),bg="white")
b1.place(x=130,y=115)
b2=Button(frame,text="Professors Profile",command=teacher,font=("times new roman",15,"bold"),bg="white")
b2.place(x=300,y=115)
b3=Button(frame,text="Fees Details",command=fees,font=("times new roman",15,"bold"),bg="white")
b3.place(x=500,y=115)
b3=Button(frame,text="Placement Details",command=place,font=("times new roman",15,"bold"),bg="white")
b3.place(x=130,y=160)
b4=Button(frame,text="Library System",command=library,font=("times new roman",15,"bold"),bg="white")
b4.place(x=305,y=160)
bg4=ImageTk.PhotoImage(file="c.jpg")
bglb2=Label(frame,image=bg4)
bglb2.place(x=192,y=210,width=350,height=350)
rt.mainloop()