from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
import pymysql
import random
from tkinter import messagebox
from doctorsFile import DoctorFile
import fetchDBconn
from patientviewDoctor import PatientseeDoctorlist

from Tools.scripts.make_ctype import values


class PatientTakeapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Take Appointment")
        self.root.geometry("1050x550+225+180")

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        #login_bg = Image.open( r"C:\Users\Maysha\Downloads\appointment.jpg")
        #login_bg = login_bg.resize( (1050, 550), Image.ANTIALIAS )
        #self.photo_login_bg = ImageTk.PhotoImage( login_bg )

        #lblimg = Label( self.root, image=self.photo_login_bg, bd=4, relief=RIDGE )
        #lblimg.place( x=0, y=0, width=1050, height=550 )

        self.var_dc_name = StringVar()
        self.var_patient_name = StringVar()
        self.var_patient_phone = StringVar()
        self.var_patient_email = StringVar()
        self.var_appoint_date = StringVar()
        self.var_appoint_media = StringVar()
        self.var_do=StringVar()

        # ***************tiTle**********

        l1 = Label( self.root, text="Patient Takes Appointment ", font=("times in roman", 18, "bold"), bg="gray", fg="white",
                    bd=4, relief=RIDGE )
        l1.place( x=0, y=0, width=1050, height=50 )

        # ******************2nd image logo*********************
#        img2 = Image.open( r"C:\Users\Maysha\Downloads\168592796_446166953124394_8073031393291666163_n.png" )
       # img2 = img2.resize( (100, 46), Image.ANTIALIAS )
       # self.photoimg2 = ImageTk.PhotoImage( img2 )

        #lblimg1 = Label( self.root, image=self.photoimg2, bd=0, relief=RIDGE )
        #lblimg1.place( x=0, y=0, width=100, height=46 )

        # ******************Level fram***********************
        labelframleft = LabelFrame( self.root, bd=2, relief=RIDGE, text="Patient's Information",font=("times in roman", 15, "bold"),fg="blue", padx=2 )
        labelframleft.place( x=5, y=50, width=370, height=525 )

        # ******************Levels and entries***********************
        # doctor name
        lbl_doctor_name = Label( labelframleft, text="Doctor Name", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_doctor_name.grid( row=0, column=0, sticky=W )

        enty_docbame= ttk.Entry( labelframleft,textvariable=self.var_dc_name, width=15, font=("arial", 12, "bold") )
        enty_docbame.grid( row=0, column=1,sticky=W  )

        #Fetch data button

        btn_fetch_data = Button( labelframleft, command=self.fetch_name,text="Info", font=("arial", 9, "bold"), bg="blue", fg="white", width=12 )
        btn_fetch_data.place( x=280, y=3, width=80, height=28)


        # patient name
        lbl_patient_name = Label( labelframleft, text="Patient Name", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_patient_name.grid( row=1, column=0, sticky=W )

        enty_patname = ttk.Entry( labelframleft, textvariable=self.var_patient_name,width=25, font=("arial", 12, "bold"))
        enty_patname.grid( row=1, column=1 )

        # patient Phone No.
        lbl_patientPhone = Label( labelframleft, text="Patient Phone No.", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_patientPhone.grid( row=2, column=0, sticky=W )

        enty_pn = ttk.Entry( labelframleft,textvariable=self.var_patient_phone, width=25, font=("arial", 12, "bold"))
        enty_pn.grid( row=2, column=1 )

        # patient Email Id
        lbl_cust_em = Label( labelframleft, text="Patient Email Id.", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_cust_em.grid( row=3, column=0, sticky=W )

        enty_em = ttk.Entry( labelframleft, textvariable=self.var_patient_email,width=25, font=("arial", 12, "bold") )
        enty_em.grid( row=3, column=1 )

         # Appointment date
        lbl_cust_date = Label( labelframleft, text="Appointment date", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_cust_date.grid( row=4, column=0, sticky=W )

        enty_date = ttk.Entry( labelframleft, textvariable=self.var_appoint_date,width=25, font=("arial", 12, "bold") )
        enty_date.grid( row=4, column=1 )

        # Appointment Media
        lbl_media = Label( labelframleft, text="Appointment Media", font=("arial", 10, "bold"), padx=2, pady=6 )
        lbl_media.grid( row=5, column=0, sticky=W )

        c__media = ttk.Combobox( labelframleft,  textvariable=self.var_appoint_media,font=("arial", 12), width=23,state="readonly" )
        c__media["value"] = ("_________Select_________","Online", "Offline")
        c__media.current( 0 )
        c__media.grid( row=5, column=1 )

        # Appointment do
        lbl_media = Label( labelframleft, text="Creat or Update", font=("arial", 11, "bold"), padx=2, pady=6 ,fg="red")
        lbl_media.grid( row=6, column=0, sticky=W )

        c__media = ttk.Combobox( labelframleft, textvariable=self.var_do,font=("arial", 12), width=23, state="readonly" )
        c__media["value"] = ("_________Select_________","Add", "Update")
        c__media.current( 0 )
        c__media.grid( row=6, column=1 )



    #button

        btnadd = Button( labelframleft,  command=self.add_data,text="Add", font=("arial", 9, "bold"), bg="black", fg="gold",width=12 )
        btnadd.place(x=10, y=240, width=120, height=35 )

        btnupdate = Button( labelframleft,command=self.update, text="Update", font=("arial", 9, "bold"), bg="black",fg="gold", width=12 )
        btnupdate.place(x=10, y=280, width=120, height=35 )

        btndelete = Button( labelframleft, command=self.mDelete,text="Delete",  font=("arial", 9, "bold"), bg="black", fg="gold", width=12)
        btndelete.place(x=10, y=320, width=120, height=35 )

        btnreset = Button(labelframleft, command=self.reset,text="Reset",  font=("arial", 9, "bold"), bg="black",fg="gold", width=12 )
        btnreset.place(x=10, y=360, width=120, height=35 )

        btnshow = Button( labelframleft, command=self.doctor_all, text="All Doctor", font=("arial", 9, "bold"), bg="black",fg="gold", width=12 )
        btnshow.place( x=150, y=250, width=120, height=35)

        btnshow1 = Button( labelframleft,command=self.fetch_pname,  text="Your Information", font=("arial", 9, "bold"),bg="black", fg="gold", width=12 )
        btnshow1.place( x=150, y=320, width=120, height=35 )

        self.cust_ditals_table = ttk.Treeview( self.root, column=("name", "type") )

    def fetch_pname(self):
        if self.var_patient_name.get() == "" and self.var_appoint_date.get()=="":
            messagebox.showerror( "Error", "Please Enter Patient Name and Appointment Date", parent=self.root )

        else:
            conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
            my_cursor = conn.cursor()
            query = ("select dname from showpatient where Patientname=%s and adate=%s")
            value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
            my_cursor.execute( query, value )
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror( "Error", "This Patient not found or Appointment data not found", parent=self.root )
            else:
                conn.commit()
                conn.close()
                showdatafram = Frame( self.root, bd=4, relief=RIDGE, padx=6 )
                showdatafram.place( x=500, y=230, width=500, height=180 )

                # doctor name
                lblName = Label( showdatafram, text="Doctor Name :", font=("arial", 12, "bold") )
                lblName.place( x=0, y=0 )

                lbl = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl.place( x=120, y=0 )

                # Phone No.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select pmobile from showpatient where Patientname=%s and adate=%s")
                value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, text="Patient's Phone number :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=30 )

                lbl1 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl1.place( x=200, y=30 )

                # email.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select pmail from showpatient where Patientname=%s and adate=%s")
                value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, text="Email Id is :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=60 )

                lbl2 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl2.place( x=130, y=60 )

                # date.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select adate from showpatient where Patientname=%s and adate=%s")
                value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblWeek = Label( showdatafram, text="Appointment Date :", font=("arial", 12, "bold") )
                lblWeek.place( x=0, y=90 )

                lbl3 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl3.place( x=180, y=90 )

                # media
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select amedia from showpatient where Patientname=%s and adate=%s")
                value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblTs = Label( showdatafram, text="Media : ", font=("arial", 12, "bold") )
                lblTs.place( x=0, y=120 )

                lbl4 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl4.place( x=60, y=120 )

                # patient Name.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select Patientname from showpatient where Patientname=%s and adate=%s")
                value = (self.var_patient_name.get(),self.var_appoint_date.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, text="Patient name :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=150 )

                lbl2 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl2.place( x=130, y=150 )

    #******************* All data Fetch *******************


    def fetch_name(self):
        if self.var_dc_name.get()=="":
            messagebox.showerror("Error","Please Enter Doctor Name" ,parent=self.root)

        else:
            conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
            my_cursor = conn.cursor()
            query=("select Doctortype from dregister where Doctorname=%s ")
            value=(self.var_dc_name.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Doctor not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdatafram=Frame(self.root,bd=4,relief=RIDGE,padx=6)
                showdatafram.place(x=500,y=50,width=500,height=180)

                #doctor type
                lblName=Label(showdatafram,text="Doctor of ",font=("arial", 12, "bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showdatafram,text=row,font=("arial", 12, "bold"))
                lbl.place(x=80,y=0)


                #Phone No.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select Mobile from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, text="Doctor's Phone number :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=30 )

                lbl1 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl1.place( x=200, y=30 )

                # Name.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select Doctorname from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblMobile = Label( showdatafram, text="Doctor's Name :", font=("arial", 12, "bold") )
                lblMobile.place( x=0, y=60 )

                lbl2 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl2.place( x=130, y=60 )

                # Week.
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select week from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblWeek = Label( showdatafram, text="Doctor's Sitting Week :", font=("arial", 12, "bold") )
                lblWeek.place( x=0, y=90 )

                lbl3 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl3.place( x=180, y=90 )


                #time Start
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select TimeS from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblTs = Label( showdatafram, text="From :", font=("arial", 12, "bold") )
                lblTs.place( x=0, y=120 )

                lbl4 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl4.place( x=50, y=120 )

                # time End
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select TimeE from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblTe = Label( showdatafram, text="To :", font=("arial", 12, "bold") )
                lblTe.place( x=130, y=120 )

                lbl5 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl5.place( x=170, y=120 )

                #Chember
                # time End
                conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                query = ("select address from dregister where Doctorname=%s ")
                value = (self.var_dc_name.get(),)
                my_cursor.execute( query, value )
                row = my_cursor.fetchone()

                lblAdd = Label( showdatafram, text="Chamber :", font=("arial", 12, "bold") )
                lblAdd.place( x=0, y=150 )

                lbl6 = Label( showdatafram, text=row, font=("arial", 12, "bold") )
                lbl6.place( x=85, y=150 )



    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select * from showpatient" )
        rows = my_cursor.fetchall()
        if len( rows ) != 0:
            self.cust_ditals_table.delete( *self.cust_ditals_table.get_children() )
            for i in rows:
                self.cust_ditals_table.insert( "", END, values=i )
            conn.commit()
        conn.close()






    def get_cursor(self, event=""):
        cursor_row = self.cust_ditals_table.focus()
        contant = self.cust_ditals_table.item( cursor_row )
        row = contant["values"]

        self.var_dc_name.set( row[0] )
        self.var_patient_name.set( row[1] )
        self.var_patient_phone.set( row[2] )
        self.var_patient_email.set( row[3] )
        self.var_appoint_date.set( row[4] )
        self.var_appoint_media.set( row[5] )
        self.var_do.set( row[6] )


    def add_data(self):
        if self.var_dc_name .get() == "" or self.var_patient_phone.get() == "":
            messagebox.showerror( "Error", "Data field has required", parent=self.root )

        else:
            try:
                conn1 = pymysql.connect( host="127.0.0.1", user="root", password="",database="doctorinfo" )
                my_cursor = conn1.cursor()
                my_cursor.execute( "insert into showpatient values (%s,%s,%s,%s,%s,%s,%s)", (self.var_dc_name .get(), self.var_patient_name.get(), self.var_patient_phone.get(),self.var_patient_email.get(),self.var_appoint_date.get(),self.var_appoint_media.get(),self.var_do.get()))

                conn1.commit()
                self.fetch_data()
                conn1.close()
                messagebox.askyesno( "Success", "Patient will Added if you choose add option",parent=self.root )

            except Exception as es:
                messagebox.showwarning( "Warning", f"Something is wrong : {str( es )} ", parent=self.root )

    def update(self):
        if self.var_patient_name.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)

        else:
            try:
                conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                my_cursor.execute( "update showpatient set  Patientname=%s,pmobile=%s,pmail=%s,adate=%s,amedia=%s,do=%s where dname= %s",( self.var_patient_name.get(),self.var_patient_phone.get(),self.var_patient_email.get(),self.var_appoint_date.get(), self.var_appoint_media.get(), self.var_do.get(), self.var_dc_name.get()))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo( "Updated", "Patient details has been updated sucessfully", parent=self.root )
            except Exception as es:
                messagebox.showwarning( "Warning", f"Something is wrong : {str( es )} ", parent=self.root )

    def mDelete(self):
        mDelete=messagebox.askyesno("Doctor Appointment System","Do you want delete Doctor information delete?",parent=self.root)
        if mDelete>0:
            conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
            my_cursor = conn.cursor()
            query= "delete from showpatient where Patientname=%s "
            value=(self.var_patient_name.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()



    def reset(self):
        self.var_dc_name.set("")

        self.var_patient_name.set("")
        self.var_patient_phone.set("")

        self.var_patient_email.set("")
        self.var_appoint_date.set("")


    def search(self):

        conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()

        my_cursor.execute(" select * from showpatient where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def doctor_all(self):
        self.new_window = Toplevel( self.root )
        self.app = PatientseeDoctorlist( self.new_window )




if __name__ == '__main__':
    root: Tk = Tk()
    obj = PatientTakeapp( root )
    root.mainloop()