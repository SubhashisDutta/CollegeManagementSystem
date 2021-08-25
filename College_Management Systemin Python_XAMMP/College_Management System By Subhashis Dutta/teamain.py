from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import ImageTk

def ca():
	rt.destroy()
	import ca
def labmarks():
	rt.destroy()
	import labmarks
def attendance():
	rt.destroy()
	import attendance
rt=Tk()
rt.title("Teacher")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Welcome To NSEC College",font=("constantia",30,"bold"),bg="black",fg="yellow")
reg.place(x=50,y=30,width=700)


b2=Button(frame,text="CA Marks",command=ca,font=("times new roman",15,"bold"),bg="white")
b2.place(x=150,y=130)
b3=Button(frame,text="Lab Marks",command=labmarks,font=("times new roman",15,"bold"),bg="white")
b3.place(x=300,y=130)
b3=Button(frame,text="Attendance",command=attendance,font=("times new roman",15,"bold"),bg="white")
b3.place(x=450,y=130)
bg4=ImageTk.PhotoImage(file="c.jpg")
bglb2=Label(frame,image=bg4)
bglb2.place(x=192,y=210,width=350,height=350)
rt.mainloop()