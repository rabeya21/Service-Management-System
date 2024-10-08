from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector



import pymysql  #pip install pymysql

class Sregistration:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration From")
        self.root.geometry("1550x800+0+0")

        #self.var_ref = StringVar()
        # x = random.randint(1000, 9999)
        #self.var_ref.set(str(x))

        # *******Variabless*******

        self.ver_idtype=StringVar()
        self.ver_ids = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_mobail = StringVar()
        self.var_dtype=StringVar()
        self.var_gender = StringVar()
        self.var_week = StringVar()
        self.var_address = StringVar()

        self.var_password = StringVar()
        self.var_cnfrmpassword=StringVar()



        # *******login Fram*****
        login_frame1 = Frame(self.root, bg="gray", relief=RIDGE)
        login_frame1.place(x=0, y=0, width=1550, height=1000)

        # ***************** 1st image********************
        login_bg = Image.open( r"C:\Users\rabey\Pictures\sign .jpg" )
        login_bg = login_bg.resize( (550, 200), Image.ANTIALIAS )
        self.photo_login_bg = ImageTk.PhotoImage( login_bg )

        lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        lblimg.place( x=220, y=50, width=550, height=450 )
        # ====Register Frame====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=750, y=50, width=550, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 25, "bold"), bg="white", fg="green").place(
            x=140, y=60)

        # --------------------Row1
        self.ide = Label(frame1, text="Id Type.", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=10, y=110)

        cmb_ide = ttk.Combobox(frame1 , textvariable=self.ver_idtype, font=("times new roman", 13), state="readonly", justify=CENTER)
        cmb_ide['values'] = ("Select", "National Id", "Organization Id", "Passport Id")
        cmb_ide.place(x=10, y=140, width=200)
        cmb_ide.current(0)

        self.var_id = StringVar()
        self.id = Label(frame1, text="Id", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=305,
                                                                                                          y=110)
        self.txt_id = Entry(frame1,textvariable=self.ver_ids, font=("times new roman", 15), bg="gray")
        self.txt_id.place(x=305, y=140, width=200)

        # --------------------Row2
        self.f_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=10,
                                                                                                                y=180)
        self.txt_fname = Entry(frame1,textvariable=self.var_name, font=("times new roman", 15), bg="gray")
        self.txt_fname.place(x=10, y=210, width=200)

        self.email = Label(frame1, text="Mail Id", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=305,
                                                                                                                  y=180)
        self.txt_email = Entry(frame1,textvariable=self.var_email, font=("times new roman", 15), bg="gray")
        self.txt_email.place(x=305, y=210, width=200)

        self.contact = Label(frame1, text="Contact Info.", font=("times new roman", 15, "bold"), bg="white",
                        fg="black").place(
            x=10, y=250)
        self.txt_contact = Entry(frame1,textvariable=self.var_mobail, font=("times new roman", 15), bg="gray")
        self.txt_contact.place(x=10, y=280, width=200)

        # --------------------Row3

        self.doctor = Label(frame1, text="Type Of Organization", font=("times new roman", 15, "bold"), bg="white",fg="black").place( x=305, y=250)

        cmb_doc = ttk.Combobox(frame1,textvariable=self.var_dtype, font=("times new roman", 13), state="readonly", justify=CENTER)
        cmb_doc['values'] = ("Select", "Bangladesh Mahila Samiti", "Bangladesh National Women Lawyers' Association", "Bonhishikha",
            "Bangladesh Homeworkers Women Association", "Association for Community Development (ACD)", "BRAC",
            "Child Rights Information Network (CRIN)-Bangladesh", "Families For Children (FFC)",
            "Global Foodprints: CSKS (Cinnamul-Shishu Kishore Sangstha)", "Bangladesh Mahila Parishad",
            "Hope Foundation for Women & Children of Bangladesh", "Manusher Jonno Foundation")
        cmb_doc.place(x=305, y=280, width=200)
        cmb_doc.current(0)

        # --------------------Row4
        self.gender = Label(frame1, text="Gender.", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=10, y=320)

        cmb_gender = ttk.Combobox(frame1,textvariable=self.var_gender,font=("times new roman", 13), state="readonly", justify=CENTER)
        cmb_gender['values'] = ("Select", "Male", "Female")
        cmb_gender.place(x=10, y=350, width=200)
        cmb_gender.current(0)

        # --------------------Row5

        self.week = Label(frame1, text="Week Days", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=305,
                                                                                                                  y=320)
        self.txt_week = Entry(frame1, textvariable=self.var_week, font=("times new roman", 15), bg="gray")
        self.txt_week.place(x=305, y=350, width=200)


        self.chamber = Label(frame1, text="Chamber Address", font=("times new roman", 15, "bold"), bg="white",
                    fg="black").place(x=10,
                                      y=390)
        self.txt_chamber = Entry(frame1,textvariable=self.var_address , font=("times new roman", 15), bg="gray")
        self.txt_chamber.place(x=10, y=420, width=200)

        # ====Register Now Frame====
        frame2 = Frame(self.root, bg="white")
        frame2.place(x=220, y=500, width=1080, height=250)

        # --------------------Row6


        self.passw = Label(frame2, text="Password", font=("times new roman", 15, "bold"), bg="white",
                      fg="black").place(x=540, y=70)
        self.txt_passw = Entry(frame2, textvariable=self.var_password, font=("times new roman", 15), bg="gray")
        self.txt_passw.place(x=540, y=100, width=200)

        self.nfrm = Label(frame2, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                     fg="black").place(x=835, y=70)
        self.txt_cnfrm = Entry(frame2, textvariable=self.var_cnfrmpassword, font=("times new roman", 15), bg="gray")
        self.txt_cnfrm.place(x=835, y=100, width=200)

        # ------Terms----
        self.var_chk = IntVar()
        self.chk = Checkbutton(frame2, text="I Agree All The Terms & Conditions", variable=self.var_chk, onvalue=1,
                          offvalue=0, bg="white", font=("times new roman", 15)).place(x=540, y=140)

        self.btn_register = Button(frame2, text="Registered", font=("times new roman", 15, "bold"), bd=0, cursor="hand2",
                              command=self.register_data, bg="green", fg="white").place(x=690, y=180, width=200,
                                                                                        height=40)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_email.get() == "" or self.txt_contact.get() == "" or self.txt_passw.get() == "" or self.txt_cnfrm.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_passw.get() != self.txt_cnfrm.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms & conditions", parent=self.root)

        else:
            conn=mysql.connector.connect(host="127.0.0.1", user="root", password="",database="socialregistration" )
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ver_idtype.get(),
                                                                                                          self.ver_ids.get(),
                                                                                                          self.var_name.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_mobail.get(),
                                                                                                          self.var_dtype.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_week.get(),
                                                                                                          self.var_address.get(),

                                                                                                          self.var_password.get()
                                                                                                          ))
                conn.commit()
                conn.close()
                messagebox.showinfo( "Success", "Register successfully ")
            else:
                messagebox.showerror("Error","User already exist , please try another email")





if __name__ == '__main__':
    root = Tk()
    app = Sregistration(root)
    root.mainloop()
