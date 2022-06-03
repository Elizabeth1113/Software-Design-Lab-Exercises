# this is a sample GUI page for the login system of the ATM
from tkinter import *
from tkinter import messagebox


def atm_login():

    count=0
#
    for _ in range(3):
        uname = e1.get()
        password = e2.get()
        if(uname == "Admin" and password == "123"):

            messagebox.showinfo("","Login Successful!!!!")
            #root.destroy()
            break
        else:
            messagebox.showinfo("","Incorrent Username and Password")


    else:

        messagebox.showinfo("","I'm Shutting down and calling the cops!")
root = Tk()
root.title(" ATM Login Page")
root.geometry("300x200")
global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=atm_login ,height = 3, width = 13).place(x=10, y=100)

root.mainloop()
