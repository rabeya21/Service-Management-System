from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from adminMedical import Cust_Win
from socialAdmin import SocialAdmin
from socialserviceUser import SocialUser

from doctorsFile import DoctorFile
from laweradd import AddLawyer

from patientTakeAppointment import PatientTakeapp



#from PIL import ImageTk
from tkinter import ttk
class SocialService():
    def __init__(self,root):
        self.root=root
        self.root.title("Social Service")
        self.root.geometry("228x137+228+181")

        #******************main frame******************
        btn_frame = Frame( self.root, bd=4, relief=RIDGE )
        btn_frame.place( x=0, y=0, width=228, height=200 )
        cust_btn = Button( btn_frame, text="Service Holder's\ninformation", width=22,command=self.cust_details,font=("times in roman", 12, "bold"), bg="black", fg="gold", bd=0, cursor="hand1" )
        cust_btn.grid( row=0, column=0, pady=1 )

        room_btn = Button( btn_frame, text="Client's take\nAppointment",command=self.patient_details, width=22, font=("times in roman", 12, "bold"),bg="black", fg="gold", bd=0, cursor="hand1" )
        room_btn.grid( row=1, column=0, pady=1 )

        logout_btn = Button( btn_frame,command=self.logout, text="LogOut", width=22, font=("times in roman", 12, "bold"), bg="black",fg="gold", bd=0, cursor="hand1" )
        logout_btn.grid( row=4, column=0, pady=1 )

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=SocialAdmin(self.new_window)


    def patient_details(self):
        self.new_window = Toplevel( self.root )
        self.app = SocialUser( self.new_window )


    def logout(self):
        self.root.destroy()
if __name__ == '__main__':
    root=Tk()
    ob=SocialService(root)
    root.mainloop()
