from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL

from adminMedical import Cust_Win
import pymysql
import random
from tkinter import messagebox
import fetchDBconn

from Tools.scripts.make_ctype import values


class DoctorFile:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor's File")
        self.root.geometry( "1050x550+225+180" )

        self.var_dc_name = StringVar()
        self.var_patient_name = StringVar()
        self.var_patient_phone = StringVar()
        self.var_patient_email = StringVar()
        self.var_appoint_date = StringVar()
        self.var_appoint_media = StringVar()
        self.var_do = StringVar()

        l1 = Label( self.root, text="Total Patient", font=("times in roman", 18, "bold"), bg="gray",fg="white",bd=4, relief=RIDGE )
        l1.place( x=0, y=0, width=1050, height=50 )


        # *********************Table Fram Srarch System************************
        tablefram = LabelFrame( self.root, bd=2, relief=RIDGE, text="Patient Details and Search System",font=("arial", 12, "bold"), padx=2 )
        tablefram.place( x=300, y=150, width=500, height=400 )

        lbl_cust_ref = Label( tablefram, text="Search", font=("arial", 12, "bold"), bg="red", fg="white" )
        lbl_cust_ref.grid( row=1, column=0, sticky=W, padx=2 )


#doctor name

        lbl_doctor_name = Label( tablefram, text="Doctor Name", font=("arial", 12, "bold"), width=18,fg="blue" )
        lbl_doctor_name.grid( row=1, column=1, padx=2 )

        self.text_search = StringVar()
        txts = ttk.Entry( tablefram, textvariable=self.text_search, width=18, font=("arial", 13, "bold") )
        txts.grid( row=1, column=2, padx=2 )

#date

        lbl_doctor_name = Label( tablefram, text="Date", font=("arial", 12, "bold"), width=18,fg="blue" )
        lbl_doctor_name.grid( row=2, column=1, padx=2 )

        self.text_search1 = StringVar()
        txts = ttk.Entry( tablefram, textvariable=self.text_search1, width=18, font=("arial", 13, "bold") )
        txts.grid( row=2, column=2, padx=2 )


        btnsearch = Button( tablefram, command=self.search,text="Search", font=("arial", 8, "bold"), bg="black",fg="gold", width=10 )
        btnsearch.place(x=150,y=90)

        btnshowall = Button( tablefram,command=self.fetch_data, text="Show All", font=("arial", 8, "bold"), bg="black", fg="gold", width=10 )
        btnshowall.place(x=250,y=90)

        # ***************Show data Table************************
        details_table = LabelFrame( tablefram, bd=2, relief=RIDGE )
        details_table.place( x=0, y=150, width=500, height=200 )

        scroll_x = ttk.Scrollbar( details_table, orient=HORIZONTAL )
        scroll_y = ttk.Scrollbar( details_table, orient=VERTICAL )

        self.cust_ditals_table = ttk.Treeview( details_table, column=( "pname", "mobail", "mail", "date", "media", "do"),xscrollcommand=scroll_x, yscrollcommand=scroll_y )
        scroll_x.pack( side=BOTTOM, fill=X )
        scroll_y.pack( side=RIGHT, fill=Y )

        scroll_x.config( command=self.cust_ditals_table.xview )
        scroll_y.config( command=self.cust_ditals_table.yview )

        #self.cust_ditals_table.heading( "dname", text="Doctor name" )
        self.cust_ditals_table.heading( "pname", text="Patient Name" )
        self.cust_ditals_table.heading( "mobail", text="Patient Mobile No." )
        self.cust_ditals_table.heading( "mail", text="Email Id" )
        self.cust_ditals_table.heading( "date", text="Appointment Date" )
        self.cust_ditals_table.heading( "media", text="Appointment Media" )
        self.cust_ditals_table.heading( "do", text="Add or Update" )


        self.cust_ditals_table["show"] = "headings"

        #self.cust_ditals_table.column( "dname", width=100 )
        self.cust_ditals_table.column( "pname", width=100 )
        self.cust_ditals_table.column( "mobail", width=100 )
        self.cust_ditals_table.column( "mail", width=100 )
        self.cust_ditals_table.column( "date", width=100 )
        self.cust_ditals_table.column( "media", width=100 )
        self.cust_ditals_table.column( "do", width=100 )
        self.cust_ditals_table.pack( fill=BOTH, expand=1 )

        #self.cust_ditals_table.bind( "<ButtonRelease-1>", self.get_cursor )
        self.fetch_data()

    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select Patientname,pmobile,pmail,adate,amedia,do from showpatient" )
        rows = my_cursor.fetchall()
        if len( rows ) != 0:
            self.cust_ditals_table.delete( *self.cust_ditals_table.get_children() )
            for i in rows:
                self.cust_ditals_table.insert( "", END, values=i )
            conn.commit()
        conn.close()

    def search(self):

        conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()

        qury = ("select Patientname,pmobile,pmail,adate,amedia,do from showpatient where dname=%s and adate=%s ")
        value = (self.text_search.get(), self.text_search1.get(), )
        my_cursor.execute( qury, value )
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    def doctor_details(self):
        self.new_window = Toplevel( self.root )
        self.app = Cust_Win( self.new_window )



if __name__ == '__main__':
    root: Tk = Tk()
    obj = DoctorFile( root )
    root.mainloop()