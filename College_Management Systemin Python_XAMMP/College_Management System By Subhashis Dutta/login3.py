from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from PIL import Image,ImageTk #pip install Pillow

def register_win():
    rt.destroy()
    import register
def college():
    rt.destroy()
    import college
def sel():
    if fmail.get()=="" or pss1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
     nm=fmail.get()
     pss2=pss1.get()
     try:
        db=mysql.connector.connect(host="localhost",user="root",password="",database="sd")
        mycursor=db.cursor()
        mycursor.execute("select * from college where email=%s and password=%s",(nm,pss2))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid UserName and Password")
        else:
          messagebox.showinfo("Success", "User Welcome")
          rt.destroy()
          import college
        db.commit()
     except EXCEPTION as e:
         print(e)
    db.rollback()
    db.close()
rt=Tk()
rt.title("COLLEGE/CENTER Login")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg='white')
frame.place(x=520,y=100,width=400,height=630)
reg=Label(frame,text="Login HERE",font=("Times New Roman",25,"bold"),fg="black",bg="yellow")
reg.place(x=20,y=20)
mailid=Label(frame,text="Enter Email",font=("Times New Roman",15,"bold"),bg="white")
mailid.place(x=30,y=100)
fmail=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
fmail.place(x=30,y=130,width=250)
pss=Label(frame,text="Password",font=("Times New Roman",15,"bold"),bg="white")
pss.place(x=30,y=190)
pss1=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
pss1.place(x=30,y=220,width=250)
pss1.config(show="*")
b1=Button(frame,text="Login",command=sel,font=("Times New Roman",15,"bold"),bg="white")
b1.place(x=30,y=260)
reg=Button(frame,command=register_win,cursor="hand2",text="Register New Account",font=("Times New Roman",15,"bold"),bg="white",fg="red")
reg.place(x=30,y=320)

rt.mainloop()
