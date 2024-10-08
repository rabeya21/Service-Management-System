from tkinter import SCROLL
import mysql.connector
import pymysql
import random
from tkinter import messagebox
import fetchDBconn

from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector

class SocialUser:
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

        l1 = Label(self.root, text="Service Recipient", font=("times in roman", 18, "bold"), bg="black", fg="white",
                   bd=4, relief=RIDGE)
        l1.place(x=0, y=0, width=1050, height=40)

        # *******Level fram********
        labelframleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Service Recipient Details",
                                   font=("times in roman", 12, "bold"), padx=2)
        labelframleft.place(x=5, y=50, width=400, height=525)

        # *******Levels and entries********
        lbl_mname = Label(labelframleft, text="Service Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mname.grid(row=1, column=0, sticky=W)

        # mother name
        c_dt = ttk.Combobox(labelframleft, textvariable=self.var_clients_name, font=("arial", 12, "bold"), width=23,
                            state="readonly")
        c_dt["value"] = ("--Select--","Health", "Bload Bank", "Financial Fund", "Harassment",)
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

        lbl_id = Label(labelframleft, text="ID Number", font=("arial", 12, "bold"), padx=2, pady=6)
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

        btnadd = Button(btn_fram, text="Add",command=self.add_data,bg="black", fg="white", font=("arial", 12, "bold"),width=9)
        btnadd.grid(row=0, column=0)

        btnUpdate = Button(btn_fram, text="Update",command=self.update,bg="black", fg="white", font=("arial", 12, "bold"), width=9)
        btnUpdate.grid(row=0, column=1)

        btnClear = Button(btn_fram, text="Clear",command=self.clear, bg="black", fg="white", font=("arial", 12, "bold"), width=9)
        btnClear.grid(row=0, column=2)

        btnDelete = Button(btn_fram, text="Delete",command=self.delete, bg="black", fg="white", font=("arial", 12, "bold"), width=9)
        btnDelete.grid(row=0, column=3)



        # ********Table Fram Srarch System*********
        tablefram = LabelFrame(self.root, bd=2, relief=RIDGE, text="     View Details    ",
                               font=("arial", 12, "bold"), padx=2)
        tablefram.place(x=412, y=50, width=1150, height=525)


        # ******Show data Table*********
        details_table = LabelFrame(tablefram, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=600, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_ditals_table = ttk.Treeview(details_table, column=("type","name", "mobail", "mail", "idnumber", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_ditals_table.xview)
        scroll_y.config(command=self.cust_ditals_table.yview)

        self.cust_ditals_table.heading("type", text="Type")
        self.cust_ditals_table.heading("name", text="Name")
        self.cust_ditals_table.heading("mobail", text="Mobile")
        self.cust_ditals_table.heading("mail", text="Mail")
        self.cust_ditals_table.heading("idnumber", text="ID Number")
        self.cust_ditals_table.heading("address", text="Address")

        self.cust_ditals_table["show"] = "headings"



        self.cust_ditals_table.column("type", width=100)
        self.cust_ditals_table.column("name", width=100)
        self.cust_ditals_table.column("mobail", width=100)
        self.cust_ditals_table.column("mail", width=100)
        self.cust_ditals_table.column("idnumber", width=100)
        self.cust_ditals_table.column("address", width=100)

        self.cust_ditals_table.pack(fill=BOTH, expand=1)
        self.cust_ditals_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cust_name.get()=="" or self.var_clients_name.get()=="":
            messagebox.showerror("Error","all fields are required to fill")
        else:
         conn = pymysql.connect(host="localhost", user="root", password="", database="services_details")
         cur = conn.cursor()
         cur.execute("insert into services_details.services values (%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_clients_name.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_mobail.get(),
                                                                            self.var_email.get(),
                                                                            self.var_id.get(),
                                                                            self.var_address.get()))

         conn.commit()
         self.fetch_data()
         conn.close()
         messagebox.showinfo("success","Record has been inserted")

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="services_details" )
        cur = conn.cursor()
        cur.execute("select * from services")
        rows = cur.fetchall()
        if len( rows ) != 0:
            self.cust_ditals_table.delete(*self.cust_ditals_table.get_children())
            for i in rows:
                self.cust_ditals_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, ev):
        cursor_row = self.cust_ditals_table.focus()
        contant = self.cust_ditals_table.item( cursor_row )
        row = contant["values"]

        self.var_cust_name.set(row[0])
        self.var_clients_name.set(row[1])
        self.var_mobail.set(row[2])
        self.var_email.set(row[3])
        self.var_id.set(row[4])
        self.var_address.set(row[5])

    def clear(self):
        self.var_cust_name.set("")
        self.var_clients_name.set("")
        self.var_mobail.set("")
        self.var_email.set("")
        self.var_id.set("")
        self.var_address.set("")

    #def update(self):
        #if self.var_id.get() == "":
            #messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)

        #else:
            #try:
               #conn =pymysql.connect(host="localhost", user="root", password="", database="services_details")
                #cur = conn.cursor()
                #cur.execute("update services set type=%s,name=%s,mobile=%s,mail=%s,address=%s where idnumber=%s",
                                                                                  #(self.var_cust_name.get(),
                                                                                   #self.var_clients_name.get(),
                                                                                   #self.var_mobail.get(),
                                                                                   #self.var_email.get(),
                                                                                   #self.var_address.get(),
                                                                                   #self.var_id.get()))
                #cur.execute("update services set type=%s,name=%s,mobile=%s,mail=%s,address=%s where idnumber=%s",(self.var_cust_name.get(),
                                                                                                   # self.var_clients_name.get(),
                                                                                                   # self.var_mobail.get(),
                                                                                                    #self.var_email.get(),
                                                                                                    #self.var_address.get(),
                                                                                                    #self.var_id.get()))

               # conn.commit()
               # self.fetch_data()
               # self.clear()
                #conn.close()
                #messagebox.showinfo("success","Record has been inserted")
            #except Exception as es:
                #messagebox.showwarning("Warning", f"Something is wrong : {str(es)} ", parent=self.root)

    def update(self):

        conn = pymysql.connect(host="localhost", user="root", password="",
                               database="services_details")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "UPDATE services SET type= %s, name = %s, mobail = %s, mail = %s, nid /pass.no = %s, address= %s WHERE name = %s ",(
                                                                                self.var_cust_name.get(),
                                                                                self.var_mobail.get(),
                 self.var_email.get(),
                 self.var_address.get(),
                 self.var_id.get(),
                 self.var_clients_name.get()))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("success", "Record has been inserted")



    def delete(self):

        mDelete = messagebox.askyesno("Service Recipient", "Do you want delete Service Recipient information delete?",
                                      parent=self.root)
        if mDelete > 0:
            conn = pymysql.connect(host="localhost", user="root", password="", database="services_details")
            my_cursor = conn.cursor()
            query = "delete from showservices where name=%s "
            value = (self.var_cust_name.get(),)
            my_cursor.execute(query, value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


if __name__ == '__main__':
    root = Tk()
    app = SocialUser(root)
    root.mainloop()
