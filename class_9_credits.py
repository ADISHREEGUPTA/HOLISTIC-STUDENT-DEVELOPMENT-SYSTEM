from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
import mysql.connector as sq


def connection():
    conn = sq.connect(
        host='localhost',
        user='root', 
        password='HPSdb2018',
        db='world',
    )
    return conn

def back():
    import STUDENT_DETAILS

root=Tk()
root.title("CREDIT BOOSTER")        
root.geometry('900x600+50+50')
root.configure(bg="navy blue")
frame1=Frame(root,bg="white")
frame1.place(x=70,y=30,width=960,height=500)
title=Label(frame1,text="Questionnaire" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=360,y=10)       
name=Label(frame1,text="Enter your registered name ",font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=70)
entryname = Entry(frame1, font=('Bookman Old Style', 16), bg='white')
entryname.place(x=700, y=70, width=230, height=24)
que1=Label(frame1,text="Did you secure NTSE scholarship last year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=100)
que1 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que1['values'] = ("Select","yes","no")
que1.place(x=700,y=100,width=230)
que1.current(0)
que2=Label(frame1,text="Were you a state level awardee in the international science/maths/computer olympiads last year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=130)
que2 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que2['values'] = ("Select","yes","no")
que2.place(x=700,y=130,width=230)
que2.current(0)
que3=Label(frame1,text="Were you a national awardee in any of the CBSE competitions last year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=160)
que3 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que3['values'] = ("Select","yes","no")
que3.place(x=700,y=160,width=230)
que3.current(0)
que4=Label(frame1,text="Were you national awardee in any of the IIT/Government hackathons organized  last  year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=190)
que4 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que4['values'] = ("Select","yes","no")
que4.place(x=700,y=190,width=230)
que4.current(0)
que5=Label(frame1,text="Have you been an awardee for any of the Azadi ka Amrit Mahotsav competitions ?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=220)
que5 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que5['values'] = ("Select","yes","no")
que5.place(x=700,y=220,width=230)
que5.current(0)
que6=Label(frame1,text="Have you participated in any interhouse team events in your school last year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=250)
que6 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que6['values'] = ("Select","yes","no")
que6.place(x=700,y=250,width=230)
que6.current(0)
que7=Label(frame1,text="Are you currently a part of any awareness campaigns being  led in your neighborhood ?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=280)
que7 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que7['values'] = ("Select","yes","no")
que7.place(x=700,y=280,width=230)
que7.current(0)
que8=Label(frame1,text="Have you celebrated  Har Ghar Tiranga  this year in your house?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=310)
que8 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que8['values'] = ("Select","yes","no")
que8.place(x=700,y=310,width=230)
que8.current(0)
que9=Label(frame1,text="Have you won any inter school sports tournaments this year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=340)
que9 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que9['values'] = ("Select","yes","no")
que9.place(x=700,y=340,width=230)
que9.current(0)    
que10=Label(frame1,text="Have contributed towards teaching poor children this year?" , font=("time new roman",10,"bold"),bg= "white" ,fg ="gray").place(x=30,y=370)
que10 = ttk.Combobox(frame1,font=("time new roman",10),state = 'readonly',justify=CENTER)
que10['values'] = ("Select","yes","no")
que10.place(x=700,y=370,width=230)
que10.current(0)

def submit_ans():
    
    result=0
    if que1.get() =="yes":
       result+=100
    if que2.get() =="yes":
       result+=80
    if que3.get() =="yes":
       result+=50
    if que4.get() =="yes":
       result+=50
    if que5.get() =="yes":
       result+=80
    if que6.get() =="yes":
       result+=50
    if que7.get() =="yes":
       result+=80
    if que8.get() =="yes":
       result+=50
    if que9.get() =="yes":
       result+=80
    if que10.get() =="yes":
       result+=100
    messagebox.showinfo("Bonus",str(result),parent=root)

    try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='world')
            cur = con.cursor()
            code='insert into student_9_credits(name,credits) values(%s,%s)'
            values=(entryname.get(),str(result),)
            cur.execute(code,values)
            con.commit()
            con.close()
            showinfo('Success', "Submitted Successfully", parent=root)

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)
    
submit=Button(frame1,text ="Submit",font=("time new roman",15),bd=0,cursor="hand2",command=submit_ans).place(x=30,y=440)

backbutton=Button(frame1,text=' Back ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=850,y=440)

root.mainloop()

