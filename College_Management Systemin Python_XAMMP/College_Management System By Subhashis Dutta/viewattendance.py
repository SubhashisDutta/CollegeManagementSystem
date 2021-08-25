from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import ImageTk

def add():
    if name1.get()=="" or rol1.get()=="" or unirol1.get()=="" or cs1.get()=="" or courselist.get()=="" or department1.get()=="" or sub1.get()=="" or dat1.get()=="" or atte1.get()=="" :
       messagebox.showerror("Error","All fields are required")
    else:
     nam=name1.get()
     r1=rol1.get()
     unir1=unirol1.get()
     sem=cs1.get()
     course1=courselist.get()
     dep=department1.get()
     sb=sub1.get()
     dt=dat1.get()
     att=atte1.get()
     db=mysql.connector.connect(host="localhost",user="root",password="",database="sd")
     mycursor=db.cursor()
     try:
        sql="insert into attendanceinfo(name,rol,unirol,cs,course,department,sub,date,attendance)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(nam,r1,unir1,sem,course1,dep,sb,dt,att)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Record Inserted successfully")
        fectdata()
        cleardata()
     except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
def fectdata():
    nam = name1.get()
    r1 = rol1.get()
    unir1 = unirol1.get()
    sem = cs1.get()
    course1 = courselist.get()
    dep = department1.get()
    sb = sub1.get()
    dt = dat1.get()
    att = atte1.get()
    db=mysql.connector.connect(host="localhost", user="root", password="", database="sd")
    mycursor = db.cursor()
    mycursor.execute("select * from attendanceinfo")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        studtab.delete(*studtab.get_children())
    for row in rows:
       studtab.insert('',END,values=row)
    db.commit()
    db.close()
def cleardata():
    name1.delete(0, 'end')
    rol1.delete(0, 'end')
    unirol1.delete(0, 'end')
    cs1.delete(0, 'end')
    courselist.delete(0, 'end')
    department1.delete(0, 'end')
    sub1.delete(0, 'end')
    dat1.delete(0 ,'end')
    atte1.delete(0, 'end')
    name1.focus_set()
def getdata(event):
    currow=studtab.focus()
    contents=studtab.item(currow)
    row=contents['values']
    name1.delete(0, END)
    rol1.delete(0, END)
    unirol1.delete(0, END)
    cs1.delete(0, END)
    courselist.delete(0, END)
    department1.delete(0, END)
    sub1.delete(0, END)
    dat1.delete(0, END)
    atte1.delete(0, END)
    name1.insert(0,row[0])
    rol1.insert(0,row[1])
    unirol1.insert(0, row[2])
    cs1.insert(0,row[3])
    courselist.insert(0,row[4])
    department1.insert(0,row[5])
    sub1.insert(0, row[6])
    dat1.insert(0,row[7])
    atte1.insert(0,row[8])
def update():
    nam = name1.get()
    r1 = rol1.get()
    unir1 = unirol1.get()
    sem = cs1.get()
    course1 = courselist.get()
    dep = department1.get()
    sb = sub1.get()
    dt = dat1.get()
    att = atte1.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="sd")
    mycursor = db.cursor()
    try:
        sql = "update attendanceinfo set rol=%s,unirol=%s,cs=%s,course=%s,department=%s,sub=%s,date=%s,attendance=%s where name=%s"
        val = (r1,unir1,sem,course1,dep,sb,dt,att,nam)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information", "Record Updated successfully")
        name1.delete(0, END)
        rol1.delete(0, END)
        unirol1.delete(0, END)
        cs1.delete(0, END)
        courselist.delete(0, END)
        department1.delete(0, END)
        sub1.delete(0, END)
        dat1.delete(0, END)
        atte1.delete(0, END)
        fectdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
def delete1():
    nam = name1.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="sd")
    mycursor = db.cursor()
    try:
        sql = "delete from attendanceinfo where name=%s"
        val = (nam,)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Deleted successfully")
        name1.delete(0, END)
        rol1.delete(0, END)
        unirol1.delete(0, END)
        cs1.delete(0, END)
        courselist.delete(0, END)
        department1.delete(0, END)
        sub1.delete(0, END)
        dat1.delete(0, END)
        atte1.delete(0, END)
        fectdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()

def back():
	rt.destroy()
	import studmain

def fectdata1():
    ser1=comboser.get()
    lsearch1 = lsearch.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="sd")
    mycursor = db.cursor()
    mycursor.execute("select * from attendanceinfo where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        studtab.delete(*studtab.get_children())
    for row in rows:
       studtab.insert('',END,values=row)
    db.commit()
    db.close()
rt=Tk()
rt.title("View Attendace")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=900,y=200,width=350,height=350)
bg1=ImageTk.PhotoImage(file="c.jpg")
bglb2=Label(frame,image=bg1)
bglb2.place(x=0,y=0,width=350,height=350)
title=Label(rt,text="View Attendace",bd=5,relief=GROOVE,font=("constantia",30,"bold"),bg="yellow",fg="black")
title.pack(side=TOP,fill=X)
managefrm=Frame(rt,bd=4,relief=RIDGE,bg="white")
managefrm.place(x=20,y=100,width=520,height=0)
mtitle=Label(managefrm,text="Students List",font=("times new roman",20,"bold"),fg="black",bg="white")
mtitle.grid(row=0,columnspan=2,pady=20)
name=Label(managefrm,text="Name",font=("times new roman",15,"bold"),fg="black",bg="white")
name.grid(row=1,column=0,pady=10,padx=50,sticky="w")
name1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
name1.grid(row=1,column=1,pady=10,padx=20,sticky="w")
rol=Label(managefrm,text="Roll",font=("times new roman",15,"bold"),fg="black",bg="white")
rol.grid(row=2,column=0,pady=10,padx=50,sticky="w")
rol1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
rol1.grid(row=2,column=1,pady=10,padx=20,sticky="w")
unirol=Label(managefrm,text="Uni.Roll",font=("times new roman",15,"bold"),fg="black",bg="white")
unirol.grid(row=3,column=0,pady=10,padx=50,sticky="w")
unirol1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
unirol1.grid(row=3,column=1,pady=10,padx=20,sticky="w")
cs=Label(managefrm,text="Current Semester",font=("times new roman",15,"bold"),fg="black",bg="white")
cs.grid(row=4,column=0,pady=10,padx=50,sticky="w")
cs1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
cs1.grid(row=4,column=1,pady=10,padx=20,sticky="w")
course=Label(managefrm,text="Course",font=("times new roman",15,"bold"),fg="black",bg="white")
course.grid(row=5,column=0,pady=10,padx=50,sticky="w")
courselist=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
courselist.grid(row=5,column=1,pady=10,padx=20,sticky="w")
department=Label(managefrm,text="Department",font=("times new roman",15,"bold"),fg="black",bg="white")
department.grid(row=6,column=0,pady=10,padx=50,sticky="w")
department1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
department1.grid(row=6,column=1,pady=10,padx=20,sticky="w")
sub=Label(managefrm,text="Subject",font=("times new roman",15,"bold"),fg="black",bg="white")
sub.grid(row=7,column=0,pady=10,padx=50,sticky="w")
sub1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
sub1.grid(row=7,column=1,pady=10,padx=20,sticky="w")
dat=Label(managefrm,text="Date",font=("times new roman",15,"bold"),fg="black",bg="white")
dat.grid(row=8,column=0,pady=10,padx=50,sticky="w")
dat1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
dat1.grid(row=8,column=1,pady=10,padx=20,sticky="w")
atte=Label(managefrm,text="Attendance",font=("times new roman",15,"bold"),fg="black",bg="white")
atte.grid(row=9,column=0,pady=10,padx=50,sticky="w")
atte1=Entry(managefrm,font=("times new roman",15,"bold"),fg="black",bg="white")
atte1.grid(row=9,column=1,pady=10,padx=20,sticky="w")

detfrm=Frame(rt,bd=4,relief=RIDGE,bg="yellow")
detfrm.place(x=20,y=100,width=850,height=650)
lsearch=Label(detfrm,text="Search By",font=("times new roman",15,"bold"),bg="yellow")
lsearch.grid(row=0,column=0,padx=10,pady=20,sticky="w")
comboser=ttk.Combobox(detfrm,font=("times new roman",15,"bold"),width=10,state='readonly')
comboser['values']=("name","roll")
comboser.grid(row=0,column=1,padx=20,pady=10,sticky="w")
lsearch=Entry(detfrm,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")
serbt=Button(detfrm,text="Search",command=fectdata1,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
showbt=Button(detfrm,text="Show All",command=fectdata,font=("Times New Roman",10,"bold"),width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
btnfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="gray")
btnfrm.place(x=10,y=580,width=100,height=50)
backbt=Button(btnfrm,text="BACK",command=back,width=10).grid(row=0,column=0,padx=10,pady=10)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=70,width=800,height=450)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
studtab=ttk.Treeview(tabfrm,columns=("name","roll","uniroll","currentsem","course","department","subject","date","attendance"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=studtab.xview)
scrolly.config(command=studtab.yview)
studtab.heading("name",text="Name")
studtab.heading("roll",text="Roll")
studtab.heading("uniroll",text="Uni.Roll")
studtab.heading("currentsem",text="Current Sem")
studtab.heading("course",text="Course")
studtab.heading("department",text="Department")
studtab.heading("subject",text="Subject")
studtab.heading("date",text="Date")
studtab.heading("attendance",text="Attendance")
studtab['show']="headings"
studtab.column("name",width=100)
studtab.column("roll",width=100)
studtab.column("uniroll",width=100)
studtab.column("currentsem",width=100)
studtab.column("course",width=100)
studtab.column("department",width=100)
studtab.column("subject",width=100)
studtab.column("date",width=100)
studtab.column("attendance",width=100)
studtab.pack(fill=BOTH,expand=1)
studtab.bind("<ButtonRelease-1>",getdata)



fectdata()
rt.mainloop()