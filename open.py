from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk

from option import Option
#from service import UserService

from tkinter import ttk
class OpenApp():
    def __init__(self,root):
        self.root=root
        self.root.title("Taking Services")
        self.root.geometry("1550x800+0+0")

        login_bg = Image.open( r"C:\Users\rabey\Pictures\open logo.jpeg" )
        login_bg = login_bg.resize( (1400,750), Image.ANTIALIAS )
        self.photo_login_bg = ImageTk.PhotoImage( login_bg )

        lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        lblimg.place( x=0, y=0, width=1400, height=750 )
#***********************click*********************
        next_btn = Button( self.root, text="Next", command=self.next,font=("times in roman", 12, "bold"), bd=3,
                              relief=RIDGE, fg='white', bg="blue", activeforeground="white", activebackground="blue" )
        next_btn.place( x=900, y=300, width=130, height=35 )

    def next(self):
        self.new_window = Toplevel( self.root )
        self.app = Option( self.new_window )






if __name__ == '__main__':
    root=Tk()
    ob=OpenApp(root)
    root.mainloop()
