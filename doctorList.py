from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
#import mysql.connector
import pymysql
import random
from tkinter import messagebox
import fetchDBconn

from Tools.scripts.make_ctype import values

class DoctorList:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor information")
        self.root.geometry("1050x570+225+160")

        #**********************Variabless********************


        self.var_name = StringVar()

        self.ver_doctortype=StringVar()
        # ***************tiTle**********

        l1 = Label( self.root, text="Doctor List", font=("times in roman", 18, "bold"), bg="gray", fg="white",
                    bd=4, relief=RIDGE )
        l1.place( x=0, y=0, width=1050, height=50 )

        # ******************Level fram***********************
        labelframleft = LabelFrame( self.root, bd=2, relief=RIDGE, text="Doctors List",
                                    font=("times in roman", 12, "bold"), padx=2 )
        labelframleft.place( x=5, y=50, width=400, height=225 )

        # doctor name
        cname = Label( labelframleft, text="Doctor name", font=("arial", 12, "bold"), padx=2, pady=6 )
        cname.grid( row=2, column=0, sticky=W )

        textcname = ttk.Entry( labelframleft, textvariable=self.var_name, width=25, font=("arial", 13, "bold") )
        textcname.grid( row=2, column=1 )

        # doctor type
        lbl_mname = Label( labelframleft, text="Doctor Type", font=("arial", 12, "bold"), padx=2, pady=6 )
        lbl_mname.grid( row=5, column=0, sticky=W )

        c_dt = ttk.Combobox( labelframleft, textvariable=self.ver_doctortype, font=("arial", 12, "bold"), width=23,
                             state="readonly" )
        c_dt["value"] = (
        "Select", "MEDICINE", "NEUROLOGISTS", "PEDIATRICIANS", "CARDIOLOGISTS", "SURGEONS", "PHYSIATRIST")
        c_dt.current( 0 )
        c_dt.grid( row=5, column=1 )

        # ********************** Bottons****************
        #btn_fram = Frame( labelframleft, bd=2, relief=RIDGE )
        #btn_fram.place( x=0, y=120, height=35, width=400 )


        btnreset = Button( labelframleft, text="Reset",command=self.reset,  font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10 )
        btnreset.place(x=140,y=100,height=30)

        # *********************Table Fram Srarch System************************
        tablefram = LabelFrame( self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                font=("arial", 12, "bold"), padx=2 )
        tablefram.place( x=412, y=50, width=1150, height=525 )

        lbl_cust_ref = Label( tablefram, text="Search", font=("arial", 12, "bold"), bg="red", fg="white" )
        lbl_cust_ref.grid( row=0, column=0, sticky=W, padx=2 )

        self.search_var = StringVar()
        c_s = ttk.Combobox( tablefram, textvariable=self.search_var, font=("arial", 12, "bold"), width=18,state="readonly" )
        c_s["value"] = ("Doctorname", "Doctortype	")
        c_s.current( 0 )
        c_s.grid( row=0, column=1, padx=2 )

        self.text_search = StringVar()
        txts = ttk.Entry( tablefram, textvariable=self.text_search, width=18, font=("arial", 13, "bold") )
        txts.grid( row=0, column=2, padx=2 )

        btnsearch = Button( tablefram, text="Search",command=self.search, font=("arial", 8, "bold"), bg="black",fg="gold", width=10 )
        btnsearch.grid( row=0, column=3 )

        btnshowall = Button( tablefram, text="Show All",command=self.fetch_data, font=("arial", 8, "bold"), bg="black",fg="gold", width=10 )
        btnshowall.grid( row=0, column=5 )

        # ***************Show data Table************************
        details_table = LabelFrame( tablefram, bd=2, relief=RIDGE )
        details_table.place( x=40, y=80, width=500, height=300 )


        scroll_y = ttk.Scrollbar( details_table, orient=VERTICAL )

        self.cust_ditals_table = ttk.Treeview( details_table, column=("name", "type"),
                                               yscrollcommand=scroll_y )

        scroll_y.pack( side=RIGHT, fill=Y )

        scroll_y.config( command=self.cust_ditals_table.yview )
        self.cust_ditals_table.heading( "name", text="Doctor Name" )
        self.cust_ditals_table.heading( "type", text="Doctor Type" )
        self.cust_ditals_table["show"] = "headings"
        self.cust_ditals_table.column( "name", width=100 )
        self.cust_ditals_table.column( "type", width=100 )
        self.cust_ditals_table.pack( fill=BOTH, expand=1 )
        self.cust_ditals_table.bind( "<ButtonRelease-1>", self.get_cursor )
        self.fetch_data()


    def fetch_data(self):
        conn = pymysql.connect( host="localhost", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()
        my_cursor.execute( "select Doctorname,Doctortype from dregister" )
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
        self.var_name.set( row[0] )
        self.ver_doctortype.set(row[1])




    def reset(self):
        self.var_name.set( "" )


    def search(self):

        conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="doctorinfo" )
        my_cursor = conn.cursor()

        my_cursor.execute(" select Doctorname,Doctortype  from dregister where "+str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("",END,values=i)

            conn.commit()
        conn.close()

if __name__ == '__main__':
    root: Tk = Tk()
    obj = DoctorList(root)
    root.mainloop()
