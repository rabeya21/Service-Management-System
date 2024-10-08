from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow

# import pymysql #pip install pymysql

class lout:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Out")
        self.root.geometry("1550x800+0+0")

        # ******************login Fram****************
        login_frame1 = Frame(self.root, bg="gray", relief=RIDGE)
        login_frame1.place(x=0, y=0, width=1550, height=1000)

        # ***************** 1st image********************
        #login_bg = Image.open(r"C:\Users\jasia\OneDrive\Desktop\My Code\images\ok.png")
        #login_bg = login_bg.resize((550, 200), Image.ANTIALIAS)
        #self.photo_login_bg = ImageTk.PhotoImage(login_bg)

        #lblimg = Label(self.root, image=self.photo_login_bg, bd=4, relief=RIDGE)
        #lblimg.place(x=220, y=50, width=550, height=450)

        # ====Register Frame====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=750, y=50, width=550, height=449)

        title = Label(frame1, text="LOGOUT HERE", font=("times new roman", 25, "bold"), bg="white", fg="green").place(
            x=160, y=60)

        # ------Terms----
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="Are You Sure Logout Now", variable=self.var_chk, onvalue=1,
                          offvalue=0, bg="white", font=("times new roman", 18)).place(x=10, y=140)

        btn_logout = Button(frame1, text="Logout", font=("times new roman", 20, "bold"), bd=0, cursor="hand2",
                              command=self.register_data, bg="green", fg="white").place(x=180, y=250, width=200,
                                                                                        height=40)

    def register_data(self):

        # ******************login Fram****************
        login_frame1 = Frame(self.root, bg="gray", relief=RIDGE)
        login_frame1.place(x=0, y=0, width=1550, height=1000)

        # ***************** 1st image********************
        #login_bg = Image.open(r"C:\Users\jasia\OneDrive\Desktop\My Code\images\ok.png")
        #login_bg = login_bg.resize((550, 200), Image.ANTIALIAS)
        #self.photo_login_bg = ImageTk.PhotoImage(login_bg)

        #lblimg = Label(self.root, image=self.photo_login_bg, bd=4, relief=RIDGE)
        #lblimg.place(x=220, y=30, width=550, height=250)

        # ====Register Frame====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=750, y=10, width=550, height=50)

        title = Label(frame1, text="Logout Here", font=("times new roman", 25, "bold"), bg="white", fg="green").place(
            x=100, y=0)


        # ------Terms----
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="Are you sure Logout now", variable=self.var_chk, onvalue=1,
                          offvalue=0, bg="white", font=("times new roman", 12)).place(x=540, y=140)

        btn_logout = Button(frame1, text="Logout Now", font=("times new roman", 15, "bold"), bd=0, cursor="hand2",
                              command=self.register_data, bg="green", fg="white").place(x=0, y=0, width=200,
                                                                                        height=40)


    def register_data(self):
        if self.var_chk.get() == 0:
            messagebox.showinfo("Success", "Please Agree our terms & conditions", parent=self.root)
        else:
            messagebox.showinfo("Success", "Congratulations Logout Complete", parent=self.root)

    def next(self):
        self.new_window = Toplevel(self.root)
        self.app =lout(self.new_window)


if __name__ == '__main__':
    root = Tk()
    app = lout(root)
    root.mainloop()