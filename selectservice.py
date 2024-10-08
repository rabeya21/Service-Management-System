from tkinter import *
from lawerregistrarion import Lregistration

from slogin import SLogin_Window
from llogin import Lregistration
from dlogin import Login_Window
from llogin import LLogin_Window


from tkinter import ttk, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow


class SelectService:
    def __init__(self, root):
        self.root = root
        self.root.title("Login as Services")
        self.root.geometry("1550x800+0+0")

        login_bg = Image.open(r"C:\Users\rabey\Pictures\open logo.jpeg")
        login_bg = login_bg.resize((230, 150), Image.ANTIALIAS)
        self.photo_login_bg = ImageTk.PhotoImage(login_bg)

        lblimg = Label(self.root, image=self.photo_login_bg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=150)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=150, width=1550, height=620)

        lblimg = Label(main_frame, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=800)

        l1 = Label(self.root, text="Chose Login as You are", font=("times in roman", 50, "bold"), bg="gray",
                   fg="white", bd=4,
                   relief=RIDGE)
        l1.place(x=230, y=0, width=1340, height=150)

        # *******************main Fram*****************
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=150, width=1550, height=600)

        # ***********Menu***********
        l1_menu = Label(main_frame, text="Dashboard", font=("times in roman", 20, "bold"), bg="black", fg="white", bd=4,
                        relief=RIDGE)
        l1_menu.place(x=0, y=0, width=230, height=40)
        # ******************btn fram****************
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=130)

        cust_btn = Button(btn_frame, text="Doctor Service", command=self.doctor_register, width=22,
                          font=("times in roman", 12, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="Lawyer Service", command=self.lawyer_register,width=22, font=("times in roman", 12, "bold"), bg="black",
                         fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="Social Service",command=self.Socialservice_register, width=22, font=("times in roman", 12, "bold"),
                            bg="black",
                             fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)


        noob_btn = Button(btn_frame, text="Log Out",command=self.logout, width=22, font=("times in roman", 12, "bold"), bg="black",
                          fg="gold", bd=0, cursor="hand1")
        noob_btn.grid(row=4, column=0, pady=1)

    def doctor_register(self):
        self.new_window = Toplevel( self.root )
        self.app =Login_Window ( self.new_window )


    def lawyer_register(self):
        self.new_window = Toplevel(self.root)
        self.app = LLogin_Window(self.new_window)

    def Socialservice_register(self):
        self.new_window = Toplevel(self.root)
        self.app = SLogin_Window(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    app = SelectService(root)
    root.mainloop()
