from tkinter import *
from tkinter import ttk, Toplevel
from tkinter import font
from tkinter import test
from PIL import Image, ImageTk
from tkinter import messagebox
from dlogin import Login_Window
from userview import UserSite
from selectservice import SelectService

class Option():
    def __init__(self,root):
        self.root=root
        self.root.title("Choose Who Are you")
        self.root.geometry( "1550x800+0+0" )

        login_bg = Image.open( r"C:\Users\rabey\Pictures\open logo.jpeg" )
        login_bg = login_bg.resize( (1400, 750), Image.ANTIALIAS )
        self.photo_login_bg = ImageTk.PhotoImage( login_bg )

        lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        lblimg.place( x=0, y=0, width=1400, height=750 )

        #***********Who are you*****************
        l1 = Label( self.root, text="Choose who you are", font=("times in roman", 12, "bold"), bg="blue", fg="white", bd=4,relief=RIDGE )
        l1.place( x=875, y=200, width=250, height=50 )

        admin_btn=Button(self.root,text="Admin",command=self.adminstie,font=("times in roman", 12, "bold"),bg="black", fg="red", bd=4,activeforeground="white", activebackground="black",cursor="hand1")
        admin_btn.place(x=900, y=270, width=200, height=50)

        user_btn = Button( self.root, text="User", command=self.usersite,font=("times in roman", 12, "bold"), bg="black", fg="red", bd=4,activeforeground="white", activebackground="black",cursor="hand1" )
        user_btn.place( x=900, y=325, width=200, height=50 )

        service_btn = Button( self.root, text="Service Provider", command=self.select_login,font=("times in roman", 12, "bold"), bg="black", fg="red", bd=4,activeforeground="white", activebackground="black",cursor="hand1" )
        service_btn.place( x=900, y=380, width=200, height=50 )



    def adminstie(self):
        self.new_window = Toplevel( self.root )
        self.app = Login_Window( self.new_window )

    def usersite(self):
        self.new_window = Toplevel( self.root )
        self.app = UserSite( self.new_window )

    def select_login(self):
        self.new_window = Toplevel( self.root )
        self.app = SelectService( self.new_window )

if __name__ == '__main__':
    root=Tk()
    obj=Option(root)
    root.mainloop()
