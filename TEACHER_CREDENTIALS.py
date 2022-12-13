from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.configure(bg="navy blue")
root.title('CHOICE OF CLASS')

titleLabel = Label(root, text='CHOOSE YOUR CLASS', font=('Arial', 40, 'bold '),bg='black',
                   fg='white', )
titleLabel.place(x=200, y=50)

def class9():
    import class_9_data

def class10():
    import class_10_data

def class11():
    import class_11_data

def class12():
    import class_12_data

def back():
    import Teacher_login

class9button = Button(root,text="CLASS 9",font=('Arial', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class9)
class9button.place(x=200, y=200)

class10button = Button(root,text="CLASS 10",font=('Arial', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class10)
class10button.place(x=570, y=200)

class11button = Button(root,text="CLASS 11",font=('Arial', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class11)
class11button.place(x=200, y=330)

class12button = Button(root,text="CLASS 12",font=('Arial', 30, 'bold'), bd=0, cursor='hand2', fg='white', bg='grey', activebackground='white'
                        , activeforeground='white', command=class12)
class12button.place(x=570, y=330)

backbutton=Button(root,text=' BACK ',font=('arial', 15, 'bold'),fg='white',bg='grey',cursor='hand2',
                  activebackground='gray20', activeforeground='white', command=back)
backbutton.place(x=460,y=500)

root.mainloop()



