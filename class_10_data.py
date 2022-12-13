import mysql.connector as sq
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *

my_w = tk.Tk()
my_w.geometry('900x600+50+50')
my_w.configure(bg="navy blue")
my_w.geometry("400x250")

def back():
    import TEACHER_CREDENTIALS

Label1=Label(my_w,text="Your Class Report",font=("Arial",40,"bold"),bg="wheat2",fg="navy blue")
Label1.place(x=280,y=0)

connect=sq.connect(host="localhost",user="root",passwd="HPSdb2018",database="world")
conn=connect.cursor()
conn.execute("select r.name as NAME,r.age as AGE,r.class as CLASS,k.credits as CREDITS from class_10_details r, student_10_credits k where r.name=k.name group by class order by credits")
results = conn.fetchall()
tree=ttk.Treeview(my_w)
tree['show']='headings'

tree["columns"]=("NAME","AGE","CLASS","CREDITS")

tree.column("NAME",width=100,minwidth=10,anchor=tk.CENTER)
tree.column("AGE",width=100,minwidth=10,anchor=tk.CENTER)
tree.column("CLASS",width=100,minwidth=10,anchor=tk.CENTER)
tree.column("CREDITS",width=100,minwidth=10,anchor=tk.CENTER)

tree.heading("NAME",text="NAME",anchor=tk.CENTER)
tree.heading("AGE",text="AGE",anchor=tk.CENTER)
tree.heading("CLASS",text="CLASS",anchor=tk.CENTER)
tree.heading("CREDITS",text="CREDITS",anchor=tk.CENTER)

i=0
for student in results:
    tree.insert('',i,text="",values=(student[0],student[1],student[2],student[3]))
    i=i+1

scrollbary=ttk.Scrollbar(my_w,orient='vertical')
scrollbary.configure(command=tree.yview)
tree.configure(yscrollcommand=scrollbary.set)
scrollbary.place(relx=0.509,rely=0.145,width=22,height=225)

tree.grid(padx=300,pady=100)
    
def save():
    import csv
    f=open("F:\\HSDS_ADISHREE_CLASS_12\\student_10.csv","w")
    teachers_redpen=csv.writer(f)
    teachers_redpen.writerow(['NAME','AGE','CLASS','CREDITS'])
    for row in results:
        teachers_redpen.writerow(row)
    showinfo('Success', "Saved Successfully", parent=my_w)
savebutton=Button(my_w,text="SAVE",font=("Arial",35,"bold"),bg="green",fg="white",command=save).place(x=300,y=350)
backbutton=Button(my_w,text='BACK',font=('arial', 35, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=550,y=350)
my_w.mainloop()
