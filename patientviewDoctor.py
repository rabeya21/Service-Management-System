from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
import pymysql
import random
from tkinter import messagebox
import fetchDBconn

from Tools.scripts.make_ctype import values
class PatientseeDoctorlist():
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor search")
        self.root.geometry( "1050x550+225+180" )

        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_mobail = StringVar()
        self.ver_doctortype = StringVar()
        self.ver_gender = StringVar()
        self.var_week = StringVar()
        self.var_address = StringVar()
        self.var_TimeS = StringVar()
        self.var_TimeE = StringVar()
        self.var_fees = StringVar()
        self.ver_pass = StringVar()

        l1 = Label( self.root, text="Doctor List", font=("times in roman", 18, "bold"), bg="gray", fg="white", bd=4,relief=RIDGE )
        l1.place( x=0, y=0, width=1050, height=50 )

        # *********************Table Fram Srarch System************************
        tablefram = LabelFrame( self.root, bd=2, relief=RIDGE, text="Doctor Details",
                                font=("arial", 12, "bold"), padx=2 )
        tablefram.place( x=300, y=50, width=500, height=470 )

        lbl_cust_ref = Label( tablefram, text="Search", font=("arial", 12, "bold"), bg="red", fg="white" )
        lbl_cust_ref.grid( row=0, column=0, sticky=W, padx=2 )


        # doctor type
        lbl_mname = Label( tablefram, text="Doctor Type", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_mname.grid( row=0, column=1, sticky=W )

        self.search_var = StringVar()
        c_dt = ttk.Combobox( tablefram, textvariable=self.ver_doctortype, font=("arial", 12, "bold"), width=23,state="readonly" )
        c_dt["value"] = ("Select", "MEDICINE", "NEUROLOGISTS", "PEDIATRICIANS", "CARDIOLOGISTS", "SURGEONS", "PHYSIATRIST")
        c_dt.current( 0 )
        c_dt.grid( row=1, column=1 )

        self.text_search = StringVar()
        txts = ttk.Entry( tablefram, textvariable=self.text_search, width=18, font=("arial", 13, "bold") )
        txts.grid( row=1, column=2, padx=2 )

        btnsearch = Button( tablefram, command=self.search, text="Search", font=("arial", 8, "bold"), bg="black", fg="gold", width=10 )
        btnsearch.place( x=150, y=90 )

        btnshowall = Button( tablefram, command=self.fetch_data,text="Show All", font=("arial", 8, "bold"), bg="black", fg="gold", width=10 )
        btnshowall.place( x=250, y=90 )

        # ***************Show data Table************************
        details_table = LabelFrame( tablefram, bd=2, relief=RIDGE )
        details_table.place( x=0, y=140, width=500, height=300 )

        scroll_x = ttk.Scrollbar( details_table, orient=HORIZONTAL )
        scroll_y = ttk.Scrollbar( details_table, orient=VERTICAL )

        self.cust_ditals_table = ttk.Treeview( details_table, column=("name", "type"), xscrollcommand=scroll_x, yscrollcommand=scroll_y )
        scroll_x.pack( side=BOTTOM, fill=X )
        scroll_y.pack( side=RIGHT, fill=Y )

        scroll_x.config( command=self.cust_ditals_table.xview )
        scroll_y.config( command=self.cust_ditals_table.yview )
        self.cust_ditals_table.heading( "name", text="Doctor Name" )
        self.cust_ditals_table.heading( "type", text="Doctor Type" )
        self.cust_ditals_table["show"] = "headings"
        self.cust_ditals_table.column( "name", width=100 )
        self.cust_ditals_table.column( "type", width=100 )
        self.cust_ditals_table.pack( fill=BOTH, expand=1 )
        self.fetch_data()

    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select * from doctorlist" )
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

        qury = ("select * from doctorlist where Doctortype=%s ")
        value = (self.text_search.get(), )
        my_cursor.execute( qury, value )
        rows = my_cursor.fetchall()
        if len( rows ) != 0:
            self.cust_ditals_table.delete( *self.cust_ditals_table.get_children() )
            for i in rows:
                self.cust_ditals_table.insert( "", END, values=i )

            conn.commit()
        conn.close()

if __name__ == '__main__':
    root: Tk = Tk()
    obj = PatientseeDoctorlist( root )
    root.mainloop()
