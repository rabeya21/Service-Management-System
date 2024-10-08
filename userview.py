from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
#from service import UserService
from patientTakeAppointment import PatientTakeapp
from socialserviceUser import SocialUser
from crimeVictims import Victims

from tkinter import ttk
class UserSite():
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
        l1 = Label( self.root, text="Services", font=("times in roman", 15, "bold"), bg="red", fg="white",bd=4, relief=RIDGE )
        l1.place( x=845, y=240, width=250, height=50 )

        medical_btn = Button( self.root, command=self.cust_details,text="Medical  Service", font=("times in roman", 12, "bold"), bd=3,relief=RIDGE, fg='white', bg="blue", activeforeground="white", activebackground="blue" )
        medical_btn.place( x=900, y=300, width=130, height=35 )

        social_btn = Button( self.root, command=self.cust_details1,text="Social  Service", font=("times in roman", 12, "bold"), bd=3, relief=RIDGE,fg='white', bg="blue", activeforeground="white", activebackground="blue" )
        social_btn.place( x=900, y=352, width=130, height=35 )

        lawer_btn = Button( self.root, text="Legal  Action", command=self.cust_details2,font=("times in roman", 12, "bold"), bd=3, relief=RIDGE,fg='white', bg="blue", activeforeground="white", activebackground="blue" )
        lawer_btn.place( x=900, y=404, width=130, height=35 )


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app= PatientTakeapp(self.new_window)
    def cust_details1(self):
        self.new_window=Toplevel(self.root)
        self.app= SocialUser(self.new_window)

    def cust_details2(self):
        self.new_window=Toplevel(self.root)
        self.app= Victims(self.new_window)






if __name__ == '__main__':
    root=Tk()
    ob=UserSite(root)
    root.mainloop()
