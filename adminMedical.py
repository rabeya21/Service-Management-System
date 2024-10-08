from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
#import mysql.connector
import pymysql
import random
from tkinter import messagebox

from doctorList import DoctorList
import fetchDBconn

from Tools.scripts.make_ctype import values


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor's Information")
        self.root.geometry("1050x570+225+160")

        #**********************Variabless********************

        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_mobail = StringVar()
        self.ver_doctortype=StringVar()
        self.ver_gender = StringVar()
        self.var_week = StringVar()
        self.var_address = StringVar()
        self.var_TimeS = StringVar()
        self.var_TimeE = StringVar()
        self.var_fees = StringVar()
        self.ver_pass=StringVar()

        # ***************tiTle**********

        l1 = Label(self.root, text="Add Doctor Details", font=("times in roman", 18, "bold"), bg="gray", fg="white",bd=4, relief=RIDGE)
        l1.place(x=0, y=0, width=1050, height=50)

        # ******************2nd image logo*********************
        #img2 = Image.open(r"C:\Users\Maysha\Downloads\168592796_446166953124394_8073031393291666163_n.png")
        #img2 = img2.resize((100, 46), Image.ANTIALIAS)
        #self.photoimg2 = ImageTk.PhotoImage(img2)

        #lblimg1 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        #lblimg1.place(x=0, y=0, width=100, height=46)

        # ******************Level fram***********************
        labelframleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Doctors Details",
                                   font=("times in roman", 12, "bold"), padx=2)
        labelframleft.place(x=5, y=50, width=400, height=525)

        # ******************Levels and entries***********************
        # idprove box
        lbl_proof = Label( labelframleft, text="ID Proof Type", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_proof.grid( row=0, column=0, sticky=W )

        c_id = ttk.Combobox( labelframleft, textvariable=self.var_idproof, font=("arial", 12, "bold"), width=23,state="readonly" )
        c_id["value"] = ("Hospital Id", "Driving Licence", "NID", "Passport")
        c_id.current( 0 )
        c_id.grid( row=0, column=1 )

        # ID number
        lbl_id = Label( labelframleft, text="ID number", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_id.grid( row=1, column=0, sticky=W )

        txtid = ttk.Entry( labelframleft, textvariable=self.var_idnumber, width=25, font=("arial", 13, "bold") )
        txtid.grid( row=1, column=1 )


        # doctor name
        cname = Label(labelframleft, text="Doctor name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=2, column=0, sticky=W)

        textcname = ttk.Entry(labelframleft,textvariable=self.var_name, width=25, font=("arial", 13, "bold"))
        textcname.grid(row=2, column=1)

        # Email
        lbl_email = Label( labelframleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_email.grid( row=3, column=0, sticky=W )

        txtemail = ttk.Entry( labelframleft, textvariable=self.var_email, width=25, font=("arial", 13, "bold") )
        txtemail.grid( row=3, column=1 )

        # Mobail Number
        lbl_mobailno = Label( labelframleft, text="Mobail Number", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_mobailno.grid( row=4, column=0, sticky=W )

        txtmobailno = ttk.Entry( labelframleft, textvariable=self.var_mobail, width=25, font=("arial", 13, "bold") )
        txtmobailno.grid( row=4, column=1 )

        #doctor type
        lbl_mname = Label(labelframleft, text="Doctor Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=5, column=0, sticky=W)

        c_dt = ttk.Combobox( labelframleft,textvariable=self.ver_doctortype, font=("arial", 12, "bold"), width=23, state="readonly" )
        c_dt["value"] = ("Select", "MEDICINE", "NEUROLOGISTS", "PEDIATRICIANS", "CARDIOLOGISTS", "SURGEONS", "PHYSIATRIST")
        c_dt.current( 0 )
        c_dt.grid( row=5, column=1 )

        #gender
        lbl_mobailno = Label( labelframleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_mobailno.grid( row=6, column=0, sticky=W )

        txtmobailno = ttk.Entry( labelframleft, textvariable=self.ver_gender, width=25, font=("arial", 13, "bold") )
        txtmobailno.grid( row=6, column=1 )

        # Week :
        lbl_week = Label( labelframleft, text="Week", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_week.grid( row=7, column=0, sticky=W )

        txtweek = ttk.Entry( labelframleft, textvariable=self.var_week, width=25, font=("arial", 13, "bold") )
        txtweek.grid( row=7, column=1 )

        # Address
        lbl_address = Label( labelframleft, text="Hospital", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_address.grid( row=8, column=0, sticky=W )

        txtaddress = ttk.Entry( labelframleft, textvariable=self.var_address, width=25, font=("arial", 13, "bold") )
        txtaddress.grid( row=8, column=1 )


        # Time start:
        lbl_postcode = Label(labelframleft, text="Time Start", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=9, column=0, sticky=W)

        c_ts = ttk.Combobox( labelframleft, textvariable=self.var_TimeS, font=("arial", 12, "bold"), width=23,state="readonly" )
        c_ts["value"] =( "8.00 am", "9.00 am", "10.00 am","11.00 am", "12.00 am ", "1.00 pm", "2.00 pm", "3.00 pm", "4.00 pm", "5.00 pm", "6.00 pm ", "7.00 pm","8.00 pm", "9.00 pm", "10.00 pm", "11.00 pm", "12.00 pm ")
        c_ts.current( 0 )
        c_ts.grid( row=9, column=1 )

        # Time End:
        lbl_postcode1 = Label( labelframleft, text="Time End", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_postcode1.grid( row=10, column=0, sticky=W )

        c_te = ttk.Combobox( labelframleft, textvariable=self.var_TimeE, font=("arial", 12, "bold"), width=23,state="readonly" )
        c_te["value"] = ( "8.00 am", "9.00 am", "10.00 am","11.00 am", "12.00 am ", "1.00 pm", "2.00 pm", "3.00 pm", "4.00 pm", "5.00 pm", "6.00 pm ", "7.00 pm","8.00 pm", "9.00 pm", "10.00 pm", "11.00 pm", "12.00 pm ")
        c_te.current( 0 )
        c_te.grid( row=10, column=1 )

        # ********************** Bottons****************
        btn_fram = Frame(labelframleft, bd=2, relief=RIDGE)
        btn_fram.place(x=0, y=400, height=40, width=400)

        btnupdate = Button(btn_fram, text="Update",command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=12)
        btnupdate.grid(row=0, column=1)

        btndelete = Button(btn_fram, text="Delete", command=self.mDelete,font=("arial", 11, "bold"), bg="black", fg="gold", width=12)
        btndelete.grid(row=0, column=2)

        btnreset = Button(btn_fram, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=12)
        btnreset.grid(row=0, column=3)

        # *********************Table Fram Srarch System************************
        tablefram = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",font=("arial", 12, "bold"), padx=2)
        tablefram.place(x=412, y=50, width=1150 ,height=525)

        lbl_cust_ref = Label(tablefram, text="Search", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_cust_ref.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        c_s = ttk.Combobox(tablefram,textvariable=self.search_var, font=("arial", 12, "bold"), width=18, state="readonly")
        c_s["value"] = ("DoctorName","Doctortype","Ref","Mobile")
        c_s.current(0)
        c_s.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txts = ttk.Entry(tablefram, textvariable=self.text_search,width=18, font=("arial", 13, "bold"))
        txts.grid(row=0, column=2, padx=2)

        btnsearch = Button(tablefram, command=self.search ,text="Search", font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0, column=3)

        btnshowall = Button(tablefram, command=self.fetch_data,text="Show All", font=("arial", 8, "bold"), bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=5)

        # ***************Show data Table************************
        details_table = LabelFrame(tablefram, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=600, height=300)

        btnshowall1 = Button( tablefram, command=self.next, text="Show doctor as Patient", font=("arial", 12, "bold"), bg="black",fg="gold", width=10 )
        btnshowall1.place(x=200, y=370, width=250, height=50)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(details_table, column=( "idproof", "idnumber","name","mail","mobail",  "type", "gender","week", "address","timestart", "timeend"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_ditals_table.xview)
        scroll_y.config(command=self.cust_ditals_table.yview)


        self.cust_ditals_table.heading("idproof",text="ID Type")
        self.cust_ditals_table.heading( "idnumber", text="ID Number" )
        self.cust_ditals_table.heading( "name", text="Doctor Name" )
        self.cust_ditals_table.heading( "mail", text="Email" )
        self.cust_ditals_table.heading( "mobail", text="Mobile" )
        self.cust_ditals_table.heading( "type", text="Doctor Type" )
        self.cust_ditals_table.heading( "gender", text="Gender" )
        self.cust_ditals_table.heading( "week", text="Week" )
        self.cust_ditals_table.heading( "address", text="Hospital" )
        self.cust_ditals_table.heading( "timestart", text="Time Start" )
        self.cust_ditals_table.heading( "timeend", text="Time End" )


        self.cust_ditals_table["show"] = "headings"
        self.cust_ditals_table.column( "idproof",  width=100 )
        self.cust_ditals_table.column( "idnumber",  width=100 )
        self.cust_ditals_table.column( "name", width=100 )
        self.cust_ditals_table.column( "mail",width=100 )
        self.cust_ditals_table.column( "mobail", width=100 )
        self.cust_ditals_table.column( "type",  width=100)
        self.cust_ditals_table.column( "gender", width=100 )
        self.cust_ditals_table.column( "week", width=100 )
        self.cust_ditals_table.column( "address", width=100 )
        self.cust_ditals_table.column( "timestart", width=100 )
        self.cust_ditals_table.column( "timeend", width=100 )
        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        self.cust_ditals_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select idtype,id,Doctorname,Mail ,Mobile,Doctortype,Gender,week,address,TimeS,TimeE from dregister" )
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

        self.var_idproof.set( row[0] )
        self.var_idnumber.set( row[1] )
        self.var_name.set( row[2] )
        self.var_email.set( row[3] )
        self.var_mobail.set( row[4] )
        self.ver_doctortype.set(row[5])
        self.ver_gender.set( row[6] )
        self.var_week.set( row[7] )
        self.var_address.set(row[8])
        self.var_TimeS.set( row[9] )
        self.var_TimeE.set( row[10] )

    def update(self):
        if self.var_mobail.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)

        else:
            try:
                conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
                my_cursor = conn.cursor()
                my_cursor.execute( "update dregister set idtype= %s,id=%s,Doctorname=%s,Mobile=%s,Doctortype=%s,Gender=%s,week=%s,address=%s,TimeS=%s,TimeE=%s  where Mail=%s",(self.var_idproof.get(),self.var_idnumber.get(),self.var_name.get(),self.var_mobail.get(),self.ver_doctortype.get(),self.ver_gender.get(),self.var_week.get(),self.var_address.get(),self.var_TimeS.get(),self.var_TimeE.get(),self.var_email.get()))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo( "Updated", "Doctor details has been updated sucessfully", parent=self.root )
            except Exception as es:
                messagebox.showwarning( "Warning", f"Something is wrong : {str( es )} ", parent=self.root )


    def mDelete(self):
        mDelete=messagebox.askyesno("Doctor Appointment System","Do you want delete Doctor information delete?",parent=self.root)
        if mDelete>0:
            conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
            my_cursor = conn.cursor()
            query= "delete from dregister where Doctorname =%s "
            value=(self.var_name.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()





    def reset(self):

        self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_name.set( "" )
        self.var_email.set("")
        self.var_mobail.set( "" )
        self.ver_doctortype.set("")
        self.ver_gender.set("")
        self.var_week.set( "" )
        self.var_address.set( "" )
        self.var_TimeS.set( "" )



    def search(self):

        conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()

        my_cursor.execute(" select * from dregister where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def next(self):
        self.new_window = Toplevel(self.root)
        self.app = DoctorList(self.new_window)


if __name__ == '__main__':
    root: Tk = Tk()
    obj = Cust_Win(root)
    root.mainloop()