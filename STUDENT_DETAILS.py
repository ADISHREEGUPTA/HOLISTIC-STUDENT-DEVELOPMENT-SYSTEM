from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as sq

root = Tk()
root.configure(bg="navy blue")
root.title('STUDENT CREDENTIALS')

def back():
    
    import Student_login

titleLabel = Label(root, text='STUDENT CREDENTIALS', font=('Bookman Old Style', 40, 'bold '),bg='black',
                   fg='white', )
titleLabel.place(x=200, y=50)

nameLabel = Label(root, text='REGISTERED NAME', font=('Bookman Old Style', 16, 'bold'), bg='black',
                       fg='white', )
nameLabel.place(x=200, y=180)
entryname = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryname.place(x=500, y=180, width=250, height=24)

AgeLabel = Label(root, text='AGE', font=('Bookman Old Style', 16, 'bold'), bg='black',
                      fg='white', )
AgeLabel.place(x=200, y=250)
entryage = Entry(root, font=('Bookman Old Style', 16), bg='white')
entryage.place(x=500, y=250, width=250,height=24)

def class9():
    try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='world')
            cur = con.cursor()
            code='insert into class_9_details(name,age,class) values(%s,%s,%s)'
            values=(entryname.get(),str(entryage.get()),'9')
            cur.execute(code,values)
            con.commit()
            con.close()

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

    import class_9_credits

class9button = Button(root,text="CLASS 9",font=('Arial', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class9)
class9button.place(x=200, y=300)

def class10():
    try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='world')
            cur = con.cursor()
            code='insert into class_10_details(name,age,class) values(%s,%s,%s)'
            values=(entryname.get(),str(entryage.get()),'10')
            cur.execute(code,values)
            con.commit()
            con.close()

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

    import class_10_credits

class10button = Button(root,text="CLASS 10",font=('Arial', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class10)
class10button.place(x=620, y=300)

def class11():
    try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='world')
            cur = con.cursor()
            code='insert into class_11_details(name,age,class) values(%s,%s,%s)'
            values=(entryname.get(),str(entryage.get()),'11')
            cur.execute(code,values)
            con.commit()
            con.close()

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

    import class_11_credits
    
class11button = Button(root,text="CLASS 11",font=('Arial', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class11)
class11button.place(x=200, y=400)

def class12():
    
    try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='world')
            cur = con.cursor()
            code='insert into class_12_details(name,age,class) values(%s,%s,%s)'
            values=(entryname.get(),str(entryage.get()),'12')
            cur.execute(code,values)
            con.commit()
            con.close()

    except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

    import class_12_credits
    
class12button = Button(root,text="CLASS 12",font=('Arial', 18, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class12)
class12button.place(x=620, y=400)

backbutton=Button(root,text=' BACK ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=460,y=500)
root.mainloop()






