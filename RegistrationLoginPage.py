import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as ms
#to connect with database named quit
with sqlite3.connect('quit.db') as db :
    c = db.cursor() #to execute sql
c.execute('CREATE TABLE IF NOT EXISTS registration1(Name TEXT NOT NULL, email TEXT NOT NULL, location TEXT NOT NULL, Gender TEXT NOT NULL)')
db.commit()
db.close()
class registration:

    def __init__(self,master):
        self.full_name = StringVar()
        self.email_id = StringVar()
        self.location = StringVar()
        self.gender = StringVar()
        self.master = master
        self.reg_page()

    def submit_data(self):
        with sqlite3.connect('quit.db') as db :
                c = db.cursor() #to execute sql

        if not self.full_name.get():
            ms.showerror(message="ENTER NAME")
        elif not self.email_id.get():
            ms.showerror(message="ENTER EMAIL ID")
        elif not self.location.get():
            ms.showerror(message="ENTER LOCATION")
        else :
            ms.showinfo(message="DATA SUBMITTED SUCCESSFULLY")
            insert = 'INSERT INTO registration1(Name,email,location,Gender) VALUES(?,?,?,?)'
            c.execute(insert,[(self.full_name.get()),(self.email_id.get()),(self.location.get()),(self.gender.get())])
            db.commit()
            self.display()
            self.log()

    def log(self):
        self.full_name.set("")
        self.email_id.set("")
        self.location.set("")
        self.gender.set("")
        self.frame3.pack()


    def reg_page(self):
        self.head = Label(self.master,text = ' REGISTRATION FORM ',font = ('',25),fg="White",pady=50,padx=10,bg = 'Royal Blue')
        self.head.pack()
        self.frame3 = Frame(self.master,padx =50,pady = 50)
        l1=Label(self.frame3,text = 'FULL NAME : ',font = ('',20)).grid(sticky = W)
        e1=Entry(self.frame3,textvariable =self.full_name,font = ('',15),bg="Light Pink").grid(row=0,column=1)
        l2=Label(self.frame3,text = 'EMAIL : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame3,textvariable =self.email_id ,font = ('',15),bg="Light Pink").grid(row=1,column=1)
        l2=Label(self.frame3,text = 'GENDER : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame3,textvariable =self.gender ,font = ('',15),bg="Light Pink").grid(row=2,column=1)
        l2=Label(self.frame3,text = 'LOCATION : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame3,textvariable =self.location ,font = ('',15),bg="Light Pink").grid(row=3,column=1)
        Button(self.frame3,text = ' SUBMIT ',bd = 3 ,font = ('',20),command=self.submit_data).grid(row=4,column=1)

        self.frame3.pack()
    def display(self):
        with sqlite3.connect('quit.db') as db:
            c=db.cursor()
        c.execute('SELECT Name,email,location,Gender from registration1')
        tree=ttk.Treeview(root, column=("","","",""))
        tree.heading("#1", text="Name")
        tree.heading("#2", text="EMAIL")
        tree.heading("#3", text="Location")
        tree.heading("#4", text="Address")
        tree.pack()
        rows = c.fetchall()
        i=0
        for row in rows:
            print(row) # it print all records in the database
            tree.insert("",END,values=row)
    def show_database(self):
        with sqlite3.connect('quit.db') as db :
                c = db.cursor() #to execute sql
        c.execute('SELECT * FROM registration1')

        rows = c.fetchall()

        for row in rows:

            print(row)

root = Tk()
f = registration(root)
mainloop()
f.show_database()
