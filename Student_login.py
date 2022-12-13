from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as sq

def register_window():
    
    import Student_register
    
def interface():
    
    import STUDENT_DETAILS

def back():
    
    import three_levels
    
def signin():
    if userentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='credit_management_system')
            cur = con.cursor()
            cur.execute('select * from student where username=%s and password=%s', (userentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid username or Password')
                root.destroy()
            else:
                showinfo('Authenticated', 'Welcome')
                interface()
            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)
            
def forgot_password():
    
    def authentication():
        
        if user_entry.get()==" " or DOB_entry.get()==" " or newpass_entry==" ":
            showerror('Error', 'All Fields Are Required',parent=window)
        else:
            con = sq.connect(host='localhost',user='root',password='HPSdb2018', database='credit_management_system')
            cur = con.cursor()
            query='select * from student where username=%s and date_of_birth=%s'
            cur.execute(query,(user_entry.get(),DOB_entry.get()))
            row=cur.fetchone()
            if row==None:
                message.showerror('Error','Incorrect username and date of birth',parent=window)
            else:
                query='update student set password=%s where username=%s and date_of_birth=%s'
                cur.execute(query,(newpass_entry.get(),user_entry.get(),DOB_entry.get()))
                con.commit()
                con.close()
                showinfo('Success','Password is reset,please login with new password',parent=window)
                window.destroy()
                
    window=Toplevel()
    window.title("Forgot password")
    
    window.configure(bg="navy blue")

    heading_label = Label(window,text="Password Manager",font=('Arial','50' , 'bold'),bg='navy blue',fg='white')
    heading_label.place(x=200,y=60)

    userlabel=Label(window,text=" Username   ",font=('Arial','20' , 'bold'),bg='navy blue',fg='white')
    userlabel.place(x=200,y=200)

    user_entry=Entry(window,width=25,fg='black',font=('Arial','20','italic'),bd=0)
    user_entry.place(x=520,y=200)

    DOBlabel=Label(window,text="Date of Birth",font=('Arial','20' , 'bold'),bg='navy blue',fg='white')
    DOBlabel.place(x=200,y=250)

    DOB_entry=Entry(window,width=25,fg='black',font=('Arial','20','italic'),bd=0)
    DOB_entry.place(x=520,y=250)

    newpasslabel=Label(window,text="New Password",font=('Arial','20' , 'bold'),bg='navy blue',fg='white')
    newpasslabel.place(x=200,y=300)

    newpass_entry=Entry(window,width=25,fg='black',font=('Arial','20','italic'),bd=0)
    newpass_entry.place(x=520,y=300)

    resetbutton = Button(window,text=' RESET ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=authentication)
    resetbutton.place(x=800, y=380)

    window.mainloop()

root = Tk()
root.configure(background="navy blue")
root.title('STUDENT LOGIN')

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=50, y=140)

label = Label(root, text="STUDENT LOGIN", font=('Arial', 20),bg="grey",fg='white')
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=105)

mailLabel = Label(frame, text='Username', font=('arial', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=200, y=32)
userentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
userentry.place(x=110, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=200, y=120)
passentry = Entry(frame,show="*",font=('arial', 22,), bg='white', fg='black')
passentry.place(x=110, y=160)

regbutton = Button(frame,text="Register As STUDENT ?", bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=register_window)
regbutton.place(x=300, y=230)

forgotbutton = Button(frame,text="Forgot Password", bd=0, cursor='hand2', bg='gold', activebackground='gold',
                      activeforeground='gold', command=forgot_password)
forgotbutton.place(x=125, y=230)

loginbutton2 = Button(frame, text='Login', font=('arial', 15, 'bold'), fg='white', bg='grey', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=125, y=280)

backbutton=Button(frame,text=' Back ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=315,y=280)

root.mainloop()
