from tkinter import *
from tkinter import font
from tkinter import test
from PIL import Image,ImageTk
from medical import MedicalService
from lawer import LawerService
from social import SocialService
from tkinter import ttk

class HotelManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Taking services")
        self.root.geometry("1550x800+0+0")

        login_bg = Image.open( r"C:\Users\rabey\Pictures\open logo.jpeg")
        login_bg = login_bg.resize( (230,150), Image.ANTIALIAS )
        self.photo_login_bg = ImageTk.PhotoImage( login_bg )

        lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        lblimg.place( x=0, y=0, width=230, height=150 )

        #***************tiTle**********

        l1=Label(self.root,text="Admin Page",font=("times in roman",50,"bold"),bg="gray",fg="white",bd=4,relief=RIDGE)
        l1.place(x=230,y=0,width=1200,height=150)

        #*******************main Fram*****************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=150,width=1550,height=620)

        # ******************1st image*********************
        #img1=Image.open(r"C:\Users\Maysha\Downloads\appointment.jpg")
        #img1=img1.resize((1550,800),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #lblimg=Label(main_frame,image=self.photoimg1,bd=4,relief=RIDGE)
        #lblimg.place(x=0,y=0,width=1550,height=800)

        #***********Menu***********
        l1_menu = Label(main_frame, text="Dashboard", font=("times in roman", 20, "bold"), bg="black",fg="white", bd=4, relief=RIDGE)
        l1_menu.place(x=0, y=0, width=230, height=40)
        # *******************btn fram*****************
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=130)

        cust_btn=Button(btn_frame,text="Medical Service",command=self.cust_details,width=22, font=("times in roman", 12, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="Social  Service", width=22,command=self.cust_details2, font=("times in roman", 12, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="Legal  Action",command=self.cust_details1, width=22, font=("times in roman", 12, "bold"), bg="black", fg="gold",bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LogOut",command=self.logout, width=22, font=("times in roman", 12, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=MedicalService(self.new_window)

    def cust_details1(self):
        self.new_window=Toplevel(self.root)
        self.app=LawerService(self.new_window)

    def cust_details2(self):
        self.new_window=Toplevel(self.root)
        self.app=SocialService(self.new_window)


    def logout(self):
        self.root.destroy()


if __name__ == '__main__':
    root=Tk()
    ob=HotelManagementSystem(root)
    root.mainloop()
