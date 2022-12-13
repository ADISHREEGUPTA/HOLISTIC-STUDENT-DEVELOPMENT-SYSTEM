
#**************************************************************************
#'*                      FLOWER BOX                                       *
#'**************************************************************************
#'*   FILENAME:         THREE_LEVELS.IPYNB                                  *
#'*   AUTHOR:           ADISHREE GUPTA                                    *
#'*   COMPUTER NUMBER:  IN-00003291                                       * 
#'*   DATE:             09/10/2022                                        *
#'*   PURPOSE:          THE BELOW APPLICATION WILL BE USED TO MANAGE      *
#'*                     USER PROFILES ROLES AS ADMIN,TEACHER & STUDENT    *   		                  *
#'**************************************************************************

from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as sq

root = Tk()
root.configure(background="navy blue")
root.title('THREE LEVELS')
label1 = Label(root, text="Holistic Student Development System", font=('Bookman Old Style', 30,"bold"),bg="wheat2",fg="navy blue")
label1.grid(row=0, column=0, columnspan=8, rowspan=2, padx=150, pady=55)
    
def admin():

    import Admin_login

adminbutton1 = Button(root, text='ADMIN', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='grey',
                      activebackground='orange', activeforeground='white',command=admin)
adminbutton1.place(x=200, y=200)

def students():
    
    import Student_login

studentbutton2 = Button(root, text='STUDENTS', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='grey',
                      activebackground='white', activeforeground='red',command=students)
studentbutton2.place(x=380, y=200)

def teachers():
    
    import Teacher_login

teacherbutton3 = Button(root, text='TEACHERS', font=('Bookman Old Style', 25, 'bold'), fg='white', bg='grey',
                      activebackground='green', activeforeground='white',command=teachers)
teacherbutton3.place(x=630, y=200)

def back():
    
    import User_login

backbutton=Button(root,text=' BACK ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=460,y=450)

root.mainloop()
