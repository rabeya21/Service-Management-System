from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, Label, Tk
import fetchDBconn
from tkinter import SCROLL
import mysql.connector
import pymysql
import random
from tkinter import messagebox
import fetchDBconn

class SocialAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Details")
        self.root.geometry("1050x550+225+180")

        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        # *******Variabless*******
        self.var_cust_name = StringVar()
        self.var_clients_name = StringVar()
        self.var_mobail = StringVar()
        self.var_email = StringVar()
        self.var_id = StringVar()
        self.var_address  = StringVar()
        # ******tiTle***

        l1 = Label(self.root, text="Service Holder", font=("times in roman", 18, "bold"), bg="gray", fg="white",
                   bd=4, relief=RIDGE)
        l1.place(x=0, y=0, width=1050, height=40)

        # *******Level fram********
        labelframleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Service Holder Details",
                                   font=("times in roman", 12, "bold"), padx=2)
        labelframleft.place(x=5, y=50, width=400, height=525)

        # *******Levels and entries********
        lbl_mname = Label(labelframleft, text="Service Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=1, column=0, sticky=W)

        # mother name
        c_dt = ttk.Combobox(labelframleft, textvariable=self.var_clients_name, font=("arial", 12, "bold"), width=23,
                            state="readonly")
        c_dt["value"] = ("Health", "Property", "Financial Fund", "Harassment",)
        c_dt.current(0)
        c_dt.grid(row=1, column=1)

        cname = Label(labelframleft, text="Name", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=2, column=0, sticky=W)

        textcname = ttk.Entry(labelframleft, textvariable=self.var_cust_name, width=25, font=("arial", 13, "bold"))
        textcname.grid(row=2, column=1)

        lbl_mobailno = Label(labelframleft, text="Mobail Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobailno.grid(row=3, column=0, sticky=W)

        txtmobailno = ttk.Entry(labelframleft, textvariable=self.var_mobail, width=25, font=("arial", 13, "bold"))
        txtmobailno.grid(row=3, column=1)

        lbl_email = Label(labelframleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=4, column=0, sticky=W)

        txtemail = ttk.Entry(labelframleft, textvariable=self.var_email, width=25, font=("arial", 13, "bold"))
        txtemail.grid(row=4, column=1)

        lbl_id = Label(labelframleft, text="NID/Pass.No.", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id.grid(row=5, column=0, sticky=W)

        txtemail = ttk.Entry(labelframleft, textvariable=self.var_id, width=25, font=("arial", 13, "bold"))
        txtemail.grid(row=5, column=1)

        lbl_address = Label(labelframleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        txtaddress = ttk.Entry(labelframleft, textvariable=self.var_address, width=25, font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)

        #.........Buttons.......
        btn_fram = Frame(labelframleft, bd=2, relief=RIDGE)
        btn_fram.place(x=0, y=380, width=400)

        btnadd = Button(btn_fram, text="Add",bg="gray", fg="white", font=("arial", 12, "bold"),width=9)
        btnadd.grid(row=0, column=0)

        btnUpdate = Button(btn_fram, text="Update", bg="gray", fg="white", font=("arial", 12, "bold"), width=9)
        btnUpdate.grid(row=0, column=1)

        btnClear = Button(btn_fram, text="Clear", bg="gray", fg="white", font=("arial", 12, "bold"), width=9)
        btnClear.grid(row=0, column=2)

        btnDelete = Button(btn_fram, text="Delete", bg="gray", fg="white", font=("arial", 12, "bold"), width=9)
        btnDelete.grid(row=0, column=3)

        #btnExit = Button(btn_fram, text="Exit", bg="gray", fg="white", font=("arial", 12, "bold"), width=7)
        #btnExit.grid(row=0, column=4)

        # ********Table Fram Srarch System*********
        tablefram = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                               font=("arial", 12, "bold"), padx=2)
        tablefram.place(x=412, y=50, width=1150, height=525)

        lbl_cust_ref = Label(tablefram, text="Search", font=("arial", 12, "bold"), bg="Gray", fg="white")
        lbl_cust_ref.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        c_s = ttk.Combobox(tablefram, textvariable=self.search_var, font=("arial", 12, "bold"), width=18,
                           state="readonly")
        c_s["value"] = ("Name", "type","Mobile")
        c_s.current(0)
        c_s.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txts = ttk.Entry(tablefram, textvariable=self.text_search, width=18, font=("arial", 13, "bold"))
        txts.grid(row=0, column=2, padx=2)

        btnsearch = Button(tablefram, text="Search", font=("arial", 8, "bold"), bg="gray",fg="white", width=10)
        btnsearch.grid(row=0, column=3)

        btnshowall = Button(tablefram, text="Show All", font=("arial", 8, "bold"), bg="gray",fg="white", width=10)
        btnshowall.grid(row=0, column=5)

        # ******Show data Table*********
        details_table = LabelFrame(tablefram, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=600, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(details_table, column=("name","type", "mobail", "mail", "nid/pass.no", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_ditals_table.xview)
        scroll_y.config(command=self.cust_ditals_table.yview)

        self.cust_ditals_table.heading("name", text="Name")
        self.cust_ditals_table.heading("type", text="Type")
        self.cust_ditals_table.heading("mobail", text="Mobile")
        self.cust_ditals_table.heading("mail", text="Email")
        self.cust_ditals_table.heading("nid/pass.no", text="Org.ID")
        self.cust_ditals_table.heading("address", text="Address")

        self.cust_ditals_table["show"] = "headings"

        self.cust_ditals_table.column("type", width=100)
        self.cust_ditals_table.column("name", width=100)
        self.cust_ditals_table.column("mobail", width=100)
        self.cust_ditals_table.column("mail", width=100)
        self.cust_ditals_table.column("nid/pass.no", width=100)
        self.cust_ditals_table.column("address", width=100)

        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        #self.cust_ditals_table.bind("<ButtonRelease-1>", self.get_cursor)



if __name__ == "__main__":
    root = Tk()
    obj = SocialAdmin(root)
    root.mainloop()