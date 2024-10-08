from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import fetchDBconn
import mysql.connector
import pymysql
class Victims:
    def __init__(self, root):
        self.root = root
        self.root.title(" Crime victims")
        self.root.geometry("1550x800+0+0")
        self.postal = StringVar()
        self.types = StringVar()
        self.name = StringVar()
        self.Age = StringVar()
        self.Address = StringVar()
        self.vd = StringVar()
        self.ap = StringVar()
        l1 = Label(self.root, text="Apply for Crime victims ", font=("times in roman", 18, "bold"), bg="black",
                   fg="white",
                   bd=4, relief=RIDGE)
        l1.place(x=0, y=0, width=1380, height=50)
        DataFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="victims Information",
                                   font=("times in roman", 15, "bold"), fg="black", padx=2)
        DataFrameLeft.place(x=5, y=50, width=470, height=525)
        lb1Namepo = Label(DataFrameLeft, text="Lawyer Postal Code: ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lb1Namepo.grid(row=0, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="Lawyer Postal Code:", font=("times new roman", 12, "bold"),
                       textvariable=self.postal, width=35)
        lb5txt.grid(row=0, column=1)
        btn_fetch_data = Button(DataFrameLeft,command=self.fatch_id, text="Show", font=("arial", 9, "bold"),
                                bg="black", fg="white", width=12)
        btn_fetch_data.place(x=390, y=3, width=80, height=28)
        lb1Namepa = Label(DataFrameLeft, text="Name :", font=("times new roman", 12, "bold"), padx=2)
        lb1Namepa.grid(row=1, column=0, sticky=W)
        lb1txt = Entry(DataFrameLeft, text="Name :", font=("times new roman", 12, "bold"),
                       textvariable=self.name, width=35)
        lb1txt.grid(row=1, column=1)
        lb1Namepapn = Label(DataFrameLeft, text="Age :", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1Namepapn.grid(row=2, column=0, sticky=W)
        lb2txt = Entry(DataFrameLeft, text="Age :", font=("times new roman", 12, "bold"), textvariable=self.Age,
                       width=35)
        lb2txt.grid(row=2, column=1)
        lb1Namepape = Label(DataFrameLeft, text="Address :", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lb1Namepape.grid(row=3, column=0, sticky=W)
        lb3txt = Entry(DataFrameLeft, text="Address", font=("times new roman", 12, "bold"), textvariable=self.Address,
                       width=35)
        lb3txt.grid(row=3, column=1)
        lb1Namedoc = Label(DataFrameLeft, text="Type Of Crime :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lb1Namedoc.grid(row=4, column=0)
        comNamedoc = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.types,
                                  width=33)
        comNamedoc["values"] = (
            "Antisocial behaviour.", "Burglary", "Childhood abuse", "Crime abroad",
            "Cyber crime and online fraud", "Domestic abuse", "Fraud")
        comNamedoc.grid(row=4, column=1)

        lb1Namec = Label(DataFrameLeft, text="Violence Details ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lb1Namec.grid(row=5, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="Violence Details:", font=("times new roman", 12, "bold"), textvariable=self.vd,
                       width=35)
        lb5txt.grid(row=5, column=1)
        lb1Namecity = Label(DataFrameLeft, text="Payment", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lb1Namecity.grid(row=6, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="Payment:", font=("times new roman", 12, "bold"), textvariable=self.ap,
                       width=35)
        lb5txt.grid(row=6, column=1)
        btnupdate = Button(DataFrameLeft, text="Bill", font=("arial", 9, "bold"), bg="black",
                           fg="white", width=12)
        btnupdate.grid(row=10, column=0, padx=1, sticky=W)

        #==========button


        buttonFrame =Frame(DataFrameLeft, bd=2, relief=RIDGE)
        buttonFrame.place(x=5, y=340, width=412, height=52)



        btnadd = Button(buttonFrame,command=self.adddata(), text="Submit", font=("arial", 9, "bold"), bg="black",
                        fg="white", width=12)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate = Button(buttonFrame, text="Update", font=("arial", 9, "bold"), bg="black",
                           fg="white", width=12)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete = Button(buttonFrame, text="Delete", font=("arial", 9, "bold"), bg="black",
                           fg="white", width=12)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset = Button(buttonFrame , text="Reset", font=("arial", 9, "bold"), bg="black",
                          fg="white", width=12)
        btnreset.grid(row=0,column=3,padx=1)

        tablefram = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                               font=("arial", 12, "bold"), padx=2)
        tablefram.place(x=495, y=280, width=860, height=460)

        lbl_cust_ref = Label(tablefram, text="Search", font=("arial", 12, "bold"), bg="black", fg="white")
        lbl_cust_ref.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        c_s = ttk.Combobox(tablefram, textvariable=self.search_var, font=("arial", 12, "bold"), width=18,
                           state="readonly")
        c_s["value"] = ("Name", "Type", "Age")
        c_s.current(0)
        c_s.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txts = ttk.Entry(tablefram, textvariable=self.text_search, width=18, font=("arial", 13, "bold"))
        txts.grid(row=0, column=2, padx=2)

        btnsearch = Button(tablefram, text="Search", font=("arial", 8, "bold"), bg="green",
                           fg="white", width=10)
        btnsearch.grid(row=0, column=3)

        btnshowall = Button(tablefram, text="Show All", font=("arial", 8, "bold"), bg="black",
                            fg="white", width=10)
        btnshowall.grid(row=0, column=5)
        details_table = LabelFrame(tablefram, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=700, height=200)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(details_table,
                                              column=("Name", "Age", "Address", "type", "v", "p"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_ditals_table.xview)
        scroll_y.config(command=self.cust_ditals_table.yview)

        self.cust_ditals_table.heading("Name", text="Name")
        self.cust_ditals_table.heading("Age", text="Age ")
        self.cust_ditals_table.heading("Address", text=" Address")
        self.cust_ditals_table.heading("type", text="Type Of Crime ")
        self.cust_ditals_table.heading("v", text="Violence Details")
        self.cust_ditals_table.heading("p", text="Payment")

        self.cust_ditals_table["show"] = "headings"

        self.cust_ditals_table.column("Name", width=100)
        self.cust_ditals_table.column("Age", width=100)
        self.cust_ditals_table.column("Address", width=100)
        self.cust_ditals_table.column("type", width=100)
        self.cust_ditals_table.column("v", width=100)
        self.cust_ditals_table.column("p", width=100)

        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        #self.cust_ditals_table.bind("<ButtonRelease-1>", self.get_cursor)
        #self.fetch_data()
    def fatch_id(self):
        if self.postal.get()=="":
            messagebox.showerror("Error","please Enter postal code",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                           database="detailslawyer")
            my_cursor = conn.cursor
            query =(" select name from lawyer where postal=%s")
            values = (self.postal.get(),)
            my_cursor.execute(query, values)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This Doctor not found", parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdatafram = Frame(self.root, bd=4, relief=RIDGE, padx=6)
                showdatafram.place(x=500, y=50, width=500, height=180)

                # doctor type
                lblName = Label(showdatafram, text="Name ", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # Phone No.
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select types from lawyer where postal=%s ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblMobile = Label(showdatafram, text="type of lawyer :", font=("arial", 12, "bold"))
                lblMobile.place(x=0, y=30)
                lbl1 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl1.place(x=90, y=30)

                # Name.
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select phone from lawyer where postal=%s =%s ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblMobile = Label(showdatafram, text="Phone :", font=("arial", 12, "bold"))
                lblMobile.place(x=0, y=60)

                lbl2 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=60)

                # Week.
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select email from lawyer where postal=%s  ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblWeek = Label(showdatafram, text="Email :", font=("arial", 12, "bold"))
                lblWeek.place(x=0, y=90)

                lbl3 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=90)

                # time Start
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select hours from lawyer where postal=%s  ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblTs = Label(showdatafram, text="Chamber Opening time:", font=("arial", 12, "bold"))
                lblTs.place(x=0, y=120)

                lbl4 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=120)

                # time End
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select company from lawyer where postal=%s   ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblTe = Label(showdatafram, text="Chamber Ending time :", font=("arial", 12, "bold"))
                lblTe.place(x=0, y=160)

                lbl5 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=160)

                # Chember
                # time End
                conn = mysql.connector.connect(host="localhost", user="root", password="mouri1234",
                                               database="detailslawyer")
                my_cursor = conn.cursor()
                query = ("select city from lawyer where postal=%s   ")
                value = (self.postal.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAdd = Label(showdatafram, text="Weeks :", font=("arial", 12, "bold"))
                lblAdd.place(x=0, y=170)

                lbl6 = Label(showdatafram, text=row, font=("arial", 12, "bold"))
                lbl6.place(x=90, y=170)
    def adddata(self):
        if self.postal.get() == "" or self.types.get() == "":
            messagebox.showerror( "Error", "Al fields are required",parent=self.root )


        else:
            conn = mysql.connector.connect( host="localhost", user="root", password="mouri1234",
                                            database="detailslawyer" )
            my_cursor = conn.cursor()
            my_cursor.execute( "insert into victim values(%s,%s,%s,%s,%s,%s,%s,%s)",
                               (self.name.get(), self.Age.get(), self.Address.get(), self.vd.get(), self.ap.get()) )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo( "Success", "Customer has been added",parent=self.root )




if __name__ == '__main__':
    root: Tk = Tk()
    obj = Victims( root )
    root.mainloop()
