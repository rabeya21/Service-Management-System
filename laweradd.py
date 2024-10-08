from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import fetchDBconn
import mysql.connector
import pymysql


class AddLawyer:
    def __init__(self, root):

        self.root = root
        self.root.title("Add Lawyer")
        self.root.geometry("1550x800+0+0")
        self.postal = StringVar()
        self.types = StringVar()
        self.name = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.hours = StringVar()
        self.company = StringVar()
        self.city = StringVar()
        lbtitle = Label(self.root, bd=20, relief=RIDGE, text="Lawyer Information", fg="White", bg="Black",
                        font=("times new roman", 50, "bold"))
        lbtitle.pack(side=TOP, fill=X)
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)
        DataFrameLeft = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"),
                                   text="Lawyer Details")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"),text="Show Details of Lawyer")
        DataFrameRight.place(x=990, y=5, width=460, height=360)

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=450, width=1530, height=70)
        detframe = Frame(self.root, bd=20, relief=RIDGE)
        detframe.place(x=0, y=530, width=1270, height=160)

        # information gather
        lb1Namepo = Label(DataFrameLeft, text="ID: ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lb1Namepo.grid(row=0, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="ID", font=("times new roman", 12, "bold"),
                       textvariable=self.postal, width=35)
        lb5txt.grid(row=0, column=1)

        lb1Namedoc = Label(DataFrameLeft, text="Type Of Lawyer :", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lb1Namedoc.grid(row=1, column=0)
        comNamedoc = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), textvariable=self.types,
                                  width=33)
        comNamedoc["values"] = ("Personal Injury Lawyer", "Estate Planning Lawyer", "Bankruptcy Lawyer", "Intellectual Property Lawyer","Employment Lawyer", "Corporate Lawyer", "Immigration Lawyer", "Criminal Lawyer")
        comNamedoc.grid(row=1, column=1)
        lb1Namepa = Label(DataFrameLeft, text="Lawyer Name :", font=("times new roman", 12, "bold"), padx=2)
        lb1Namepa.grid(row=2, column=0, sticky=W)
        lb1txt = Entry(DataFrameLeft, text="Lawyer Name :", font=("times new roman", 12, "bold"),
                       textvariable=self.name, width=35)
        lb1txt.grid(row=2, column=1)
        lb1Namepapn = Label(DataFrameLeft, text="Contact :", font=("times new roman", 12, "bold"), padx=2, pady=4)
        lb1Namepapn.grid(row=3, column=0, sticky=W)
        lb2txt = Entry(DataFrameLeft, text="Contact:", font=("times new roman", 12, "bold"), textvariable=self.phone,
                       width=35)
        lb2txt.grid(row=3, column=1)
        lb1Namepape = Label(DataFrameLeft, text="E-mail :", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lb1Namepape.grid(row=4, column=0, sticky=W)
        lb3txt = Entry(DataFrameLeft, text="E-mail:", font=("times new roman", 12, "bold"), textvariable=self.email,
                       width=35)
        lb3txt.grid(row=4, column=1)
        lb1Namead = Label(DataFrameLeft, text="Chamber Opening Time: ", font=("times new roman", 12, "bold"), padx=2,
                          pady=6)
        lb1Namead.grid(row=5, column=0, sticky=W)
        lb4txt = Entry(DataFrameLeft, text="Chamber Opening Time:", font=("times new roman", 12, "bold"), textvariable=self.hours,
                       width=35)
        lb4txt.grid(row=5, column=1)

        lb1Namec = Label(DataFrameLeft, text="Chamber Ending Time: ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lb1Namec.grid(row=6, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="Chamber Ending Time:", font=("times new roman", 12, "bold"), textvariable=self.company,
                       width=35)
        lb5txt.grid(row=6, column=1)
        lb1Namecity = Label(DataFrameLeft, text="Week Days: ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lb1Namecity.grid(row=7, column=0, sticky=W)
        lb5txt = Entry(DataFrameLeft, text="Week Days:", font=("times new roman", 12, "bold"), textvariable=self.city,
                       width=35)
        lb5txt.grid(row=7, column=1)
        self.details = Text(DataFrameRight, font=("times new roman", 12, "bold"), width=23, height=16, padx=2,
                            pady=6)
        self.details.grid(row=0, column=0)

        #btnadd = Button(Buttonframe, text="Add", font=("arial", 8, "bold"), bg="black", fg="Purple", width=35)
        #btnadd.grid(row=0, column=0)

        btnup = Button(Buttonframe,command=self.update, text="Update", font=("arial", 8, "bold"), bg="black", fg="White", width=35)
        btnup.grid(row=0, column=1)
        btndlt = Button(Buttonframe,command=self.delete, text="Delete", font=("arial", 8, "bold"), bg="black", fg="White", width=35)
        btndlt.grid(row=0, column=2)


        btnclr = Button(Buttonframe, command=self.clear, text="Clear", font=("arial", 8, "bold"), bg="black",
                       fg="White", width=35)
        btnclr.grid(row=0, column=4)
        btnsh = Button(Buttonframe, command=self.exit, text="Exit", font=("arial", 8, "bold"), bg="black",
                       fg="White", width=35)
        btnsh.grid(row=0, column=3)

        scroll_x = ttk.Scrollbar(detframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detframe, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(detframe,
                                              column=("dname", "pname", "mobail", "mail", "date", "media", "do","city"),
                                              xscrollcommand=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_ditals_table.xview)
        scroll_y.config(command=self.cust_ditals_table.yview)

        self.cust_ditals_table.heading("dname", text="Id")
        self.cust_ditals_table.heading("pname", text=" Type Of Lawyer")
        self.cust_ditals_table.heading("mobail", text="Lawyer Name")
        self.cust_ditals_table.heading("mail", text="Phone No")
        self.cust_ditals_table.heading("date", text="E-mail")
        self.cust_ditals_table.heading("media", text="Chamber Opening Time")
        self.cust_ditals_table.heading("do", text="Chamber Ending Time")
        self.cust_ditals_table.heading("city", text="Week Days")

        self.cust_ditals_table["show"] = "headings"

        self.cust_ditals_table.column("dname", width=100)
        self.cust_ditals_table.column("pname", width=100)
        self.cust_ditals_table.column("mobail", width=100)
        self.cust_ditals_table.column("mail", width=100)
        self.cust_ditals_table.column("date", width=100)
        self.cust_ditals_table.column("media", width=100)
        self.cust_ditals_table.column("do", width=100)
        self.cust_ditals_table.column("city", width=100)
        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        self.cust_ditals_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #def adddata(self):
        #if self.postal.get() == "" or self.types.get() == "":
                #messagebox.showerror("Error", "Al fields are required")
       # else:
                #conn = mysql.connector.connect(host="localhost", user="root", password="",database="lawerinfo")
                #my_cursor = conn.cursor()
                #my_cursor.execute("insert into lawyer values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.postal.get(),self.types.get(),self.name.get(),self.phone.get(),self.email.get(),self.hours.get(),self.company.get(),self.city.get()))
                #conn.commit()
                #self.fetch_data()
                #conn.close()
                #messagebox.showinfo("Success", "Customer has been added")



    def update(self):

        conn = mysql.connector.connect(host="localhost", user="root", password="",
                                       database="lawerinfo")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "update laweradd set  lawyer=%s,f_name=%s,contact=%s,email=%s,timS=%s,timE=%s,week=%s where id=%s", (
                self.types.get(), self.name.get(), self.phone.get(), self.email.get(), self.hours.get(),
                self.company.get(),
                self.city.get(), self.postal.get()))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Updated", "lawyer details has been updated sucessfully", parent=self.root)

    def fetch_data(self):

        conn = mysql.connector.connect(host="localhost", user="root", password="",
                                           database="lawerinfo")
        my_cursor = conn.cursor()
        my_cursor.execute("select id,lawyer,f_name,contact,email,timS,timE,week from laweradd")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.cust_ditals_table.focus()
        content=self.cust_ditals_table.item(cursor_row)
        row=content["values"]
        self.postal.set(row[0])
        self.types.set(row[1])
        self.name.set(row[2])
        self.phone.set(row[3])
        self.email.set(row[4])
        self.hours.set(row[5])
        self.company.set(row[6])
        self.city.set(row[7])

    def show(self):
        self.txtadddata.insert(END,"postal Code:\t\t\t"+ self.postal.get() + "\n")
        self.txtadddata.insert(END, "Types of Lawyer:\t\t\t" + self.types.get() + "\n")
        self.txtadddata.insert(END, "Name:\t\t\t" + self.name.get() + "\n")
        self.txtadddata.insert(END, "Phone:\t\t\t" + self.phone.get() + "\n")
        self.txtadddata.insert(END, "E-mail:\t\t\t" + self.email.get() + "\n")
        self.txtadddata.insert(END, "Company:\t\t\t" + self.company.get() + "\n")

        self.txtadddata.insert(END, "City:\t\t\t" + self.city.get() + "\n")


    def delete(self):
        mDelete = messagebox.askyesno( "Lawyer Information", "Do you want delete Lawyer information delete?",parent=self.root )
        if mDelete > 0:
            conn = pymysql.connect( host="127.0.0.1", user="root", password="", database="lawerinfo" )
            my_cursor = conn.cursor()
            query = "delete from laweradd where id =%s "
            value = (self.postal.get(),)
            my_cursor.execute( query, value )

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def clear(self):
        self.postal.set("")
        self.types.set("")
        self.name.set("")
        self.phone.set("")
        self.email.set("")
        self.hours.set("")
        self.company.set("")
        self.city.set("")
    def exit(self):
        exit=messagebox.askyesno("Lawyer Information Page","Confirm you want to exit")
        if exit>0:
            root.destroy()
            return

if __name__ == '__main__':
    root: Tk = Tk()
    obj = AddLawyer( root )
    root.mainloop()
