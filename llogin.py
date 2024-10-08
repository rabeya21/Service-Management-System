from tkinter import *
from tkinter import ttk, Toplevel
from tkinter import font
from tkinter import test
from PIL import Image, ImageTk
from doctorsFile import DoctorFile
import mysql.connector
from tkinter import messagebox
from appoinmentclient import HotelManagementSystem

from lawerregistrarion import Lregistration
from laweradd import AddLawyer



def main():
    win=Tk()
    app=LLogin_Window(win)
    win.mainloop()




class LLogin_Window():

    def __init__(self, root) :
        self.root = root
        self.root.title("Taking Appointment")
        self.root.geometry("1550x800+0+0")

        self.ver_idtype = StringVar()
        self.ver_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_mobail = StringVar()
        self.var_dtype = StringVar()
        self.var_gender = StringVar()
        self.var_week = StringVar()
        self.var_address = StringVar()
        self.var_TimeS = StringVar()
        self.var_TimeE = StringVar()
        #self.var_fees = StringVar()
        self.var_password = StringVar()
        self.var_cnfrmpassword = StringVar()

        # *****************1st image********************
        login_bg = Image.open( r"C:\Users\rabey\Pictures\open logo.jpeg" )
        login_bg = login_bg.resize( (1400, 750), Image.ANTIALIAS )
        self.photo_login_bg = ImageTk.PhotoImage( login_bg )
        #
        lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        lblimg.place( x=0, y=0, width=1400, height=750 )
        # ******************login Fram****************
        login_frame = Frame(self.root, bg="black", relief=RIDGE)
        login_frame.place(x=425, y=170, width=400, height=450)


        # ************fram image*************
        #login_fram_image = Image.open(r"C:\Users\Maysha\Downloads\user icon.png")
        #login_fram = login_fram_image.resize((100, 100), Image.ANTIALIAS)
        #self.photo_login_fram_image = ImageTk.PhotoImage(login_fram)

        #lblimg = Label(login_frame, image=self.photo_login_fram_image, bd=4)
        #lblimg.place(x=150, y=10, width=100, height=100)

        # ***************Fram Label******************
        get_str = Label(login_frame, text="Login", font=("times in roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=155, y=120)

        # **************Labels**************
        self.username = lbl = Label(login_frame, text="User Name", font=("times in roman", 10, "bold"), fg="white",
                               bg="black")
        self.username.place(x=60, y=200)
        self.txtuser = ttk.Entry(login_frame, font=("times in roman", 10, "bold"))
        self.txtuser.place(x=30, y=230, width=270)

        self.passward = lbl = Label(login_frame, text="Passward", font=("times in roman", 10, "bold"), fg="white",
                               bg="black")
        self.passward.place(x=60, y=260)
        self.txtpass = ttk.Entry(login_frame, font=("times in roman", 10, "bold"))
        self.txtpass.place(x=30, y=290, width=270)



        # *************Login button*****************
        login_btn = Button(login_frame, text="LOGIN", font=("times in roman", 14, "bold"),command=self.login, bd=3,relief=RIDGE, fg='white', bg="red", activeforeground="white", activebackground="red")
        login_btn.place(x=110, y=325, width=120, height=35)

        # *********Register button***************

        register_btn = Button(login_frame, command=self.registerpage,text="New User Register",font=("times in roman", 8, "bold"), borderwidth=0,fg='white', bg="black", activeforeground="white", activebackground="black")
        register_btn.place(x=20, y=375, width=160)

        # *********forget passward***************

        fogetpass_btn = Button(login_frame, command=self.forget_pass,text="Foget Passward", font=("times in roman", 8, "bold"), borderwidth=0,
                               fg='white', bg="black", activeforeground="white", activebackground="black")
        fogetpass_btn.place(x=12, y=400, width=160)



    def login(self):
        if self.txtuser.get() == "mash" and self.txtpass.get() == "1234":
            messagebox.showinfo("Success", "Welcome !!",parent=self.root)
            self.new_window3 = Toplevel(self.root)
            self.app3 =  HotelManagementSystem(self.new_window3)
        elif self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field required",parent=self.root)
        else:
            conn = mysql.connector.connect( host="127.0.0.1", user="root", password="", database="lawerinfo" )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from laweradd where email=%s and passw=%s",(self.var_email.get(),self.var_password.get()))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalied Username and Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YseNo","Access only Lawer",parent=self.root)
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=AddLawyer(self.new_window)

                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    ################################################reset Password##############################

    def reset(self):
        if self.cmb_ide.get()=="select":
            messagebox.showerror("Error","Select Id",parent=self.root2)
        elif self.txt_fname.get()=="":
            messagebox.showerror( "Error", "Write Id", parent=self.root2 )
        elif self.txt_passw.get()=="":
            messagebox.showerror( "Error", "Write Password", parent=self.root2 )
        else:
            conn = mysql.connector.connect( host="127.0.0.1", user="root", password="", database="lawerinfo" )
            my_cursor = conn.cursor()
            qury=("select * from laweradd where email=%s and ide=%s and id=%s")
            value=(self.txtuser.get(),self.cmb_ide.get(),self.txt_fname.get(),)
            my_cursor.execute(qury,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update dregister set passw=%s where email=%s")
                value=(self.txt_passw.get(),self.txtuser.get(),)
                my_cursor.execute( query, value )
                conn.commit()
                conn.close()
                messagebox.showinfo( "Success", "Reset successfully ",parent=self.root2 )
                self.root2.destroy()

    ################################################reset Password##############################

    def forget_pass(self):
        if self.txtuser.get=="":
            messagebox.showerror("Error","Please enter the email address to reste password",parent=self.root)

        else:
            conn = mysql.connector.connect( host="127.0.0.1", user="root", password="", database="lawerinfo" )
            my_cursor = conn.cursor()
            query=("select * from laweradd where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valied user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry( "420x450+410+170" )
                get_str = Label(self.root2, text="Forget password", font=("times in roman", 20, "bold"),fg="white",bg="black" )
                get_str.place( x=0, y=0,relwidth=1 )

                self.doctor = Label( self.root2, text="Type of ID", font=("times new roman", 15, "bold"), fg="black" ).place( x=50, y=80 )
                self.cmb_ide = ttk.Combobox( self.root2, textvariable=self.ver_idtype, font=("times new roman", 13),state="readonly", justify=CENTER )
                self.cmb_ide['values'] = ("Select", "National Id", "Hospital Id", "Passport Id")
                self.cmb_ide.place( x=50, y=110, width=250 )
                self.cmb_ide.current( 0 )

                self.f_name = Label( self.root2, text="ID", font=("times new roman", 15, "bold"),fg="black" ).place( x=50,y=150 )
                self.txt_fname = Entry(self.root2 , textvariable=self.var_name, font=("times new roman", 15), bg="white" )
                self.txt_fname.place( x=50, y=180, width=250 )

                self.passw = Label( self.root2, text="Password", font=("times new roman", 15, "bold"),fg="black" ).place( x=50, y=220 )
                self.txt_passw= Entry( self.root2, font=("times new roman", 15), bg="white" )
                self.txt_passw.place( x=50, y=250, width=250 )

                self.btn_register = Button( self.root2, text="Reset", command=self.reset,font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="green", fg="white" ).place( x=150, y=290)

    def registerpage(self):
        self.new_window = Toplevel( self.root )
        self.app = Lregistration( self.new_window )




if __name__ == '__main__':
    main()