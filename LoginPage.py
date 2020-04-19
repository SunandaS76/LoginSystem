import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as ms
#to connect with database named quit
with sqlite3.connect('quit.db') as db :
    c = db.cursor() #to execute sql
c.execute('CREATE TABLE IF NOT EXISTS monu(username TEXT NOT NULL, password TEXT NOT NULL)')
c.execute('CREATE TABLE IF NOT EXISTS registration1(Name TEXT NOT NULL, email TEXT NOT NULL, location TEXT NOT NULL, Gender TEXT NOT NULL)')
db.commit()
db.close()
class uniuqe :
    pass

class final:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_re_password = StringVar()
        self.full_name = StringVar()
        self.email_id = StringVar()
        self.location = StringVar()
        self.gender = StringVar()
        self.master = master
        self.widgets()
        #print(self.username.get())

    def login(self):
        with sqlite3.connect('quit.db') as db :
            c = db.cursor()

        find_user = ('SELECT * FROM monu WHERE username=? and password=?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if not self.username.get() :
            if not self.password.get():
                ms.showerror('oops!','please enter username and password')
        elif result :
            self.frame.pack_forget()
            self.first_page_after_login()
        else :
            ms.showerror('Oops!','USERNAME OR PASSWORD WRONG')

    def new_user_(self):
        with sqlite3.connect('quit.db') as db :
            c = db.cursor() #to execute sql

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM monu WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])
        if not self.n_username.get() :
            ms.showerror('oops!','please enter username')
        elif not self.n_password.get():
            ms.showerror('oops!','please enter password')
        elif not self.n_re_password.get():
            ms.showerror('oops!','please renter the password')

        elif c.fetchall():
            ms.showerror('Error!','Username already exist. Try another one.')
        elif not self.n_password.get() == self.n_re_password.get():
           #print(self.n_password.get(),' ',self.n_re_password.get())
           ms.showerror('Error!','Password and Repassword is not matching ')


        else:
          ms.showinfo('Success!','Account Created!')
          insert = 'INSERT INTO monu(username,password) VALUES(?,?)'
          c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
          db.commit()
          self.log()
        #Create New Account
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
            self.frame4.pack_forget()
            self.log()

    def log1(self):
        self.full_name.set("")
        self.email_id.set("")
        self.location.set("")
        self.gender.set("")
        self.frame4.pack()



    def p1(self):
        self.username.set('')
        self.password.set('')
        self.frame3.pack_forget()
        self.tree.pack_forget()
        self.head['text']='LOGIN'
        self.head['fg'] = "White"
        self.frame.pack()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.frame2.pack_forget()
        self.head['text']='LOGIN'
        self.head['fg'] = "White"
        self.frame.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.n_re_password.set('')
        self.frame.pack_forget()
        self.head['text'] = 'Create Account '
        self.head['fg'] = "White"
        self.frame2.pack()

    def first_page_after_login(self):
        self.head['text'] = " ADMIN "
       #self.head['text']=self.password.get()
        self.head['fg'] = "White"
        self.frame3 = Frame(self.master,padx =40,pady = 10)
        head2 = Label(self.frame3,text=self.username.get(),font=('',15)).grid(row=0,column=1)
        Label(self.frame3,text= 'LOTUS IT HUB ',font=('',20)).grid(row=1,column=1)
        Button(self.frame3,text = 'LOGOUT',font=('',10),command=self.p1).grid(row=1,column=15)
        self.frame3.pack()
        self.display()

    def display(self):
        with sqlite3.connect('quit.db') as db:
            c=db.cursor()
        c.execute('SELECT Name,email,location,Gender from registration1')
        self.tree=ttk.Treeview(root, column=("","","",""))
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="EMAIL")
        self.tree.heading("#3", text="Location")
        self.tree.heading("#4", text="Address")
        self.tree.pack()
        rows = c.fetchall()
        i=0
        for row in rows:
            print(row) # it print all records in the database
            self.tree.insert("",END,values=row)

    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10,bg="Royal Blue",fg="White")
        self.head.pack()
        self.frame = Frame(self.master,padx =150,pady = 100)
        l1=Label(self.frame,text = 'Username: ',font = ('',20)).grid(sticky = W)
        e1=Entry(self.frame,textvariable = self.username,font = ('',15),bg="Light Pink").grid(row=0,column=1)
        l2=Label(self.frame,text = 'Password: ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame,textvariable = self.password,font = ('',15),show = '*',bg="Light Pink").grid(row=1,column=1)
        #Label(self.frame,text=self.password).grid(row=5,column=1)
        b1=Button(self.frame,text = ' Login ',bd = 3 ,font = ('',15),command=self.login).grid(row=3,column=0)
        b2=Button(self.frame,text = ' Create Account ',bd=3,font = ('',15),command=self.cr).grid(row=3,column=1)
        b3=Button(self.frame,text= ' Registration Form ',bd=3,font = ('',15),command=self.registration).grid(row=4,column=1)
        self.frame.pack()

        self.frame2 = Frame(self.master,padx =150,pady = 100)
        l3=Label(self.frame2,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        e3=Entry(self.frame2,textvariable = self.n_username,font = ('',15),bg="Light Pink").grid(row=0,column=1)
        l4=Label(self.frame2,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        e4=Entry(self.frame2,textvariable = self.n_password,font = ('',15),show = '*',bg="Light Pink").grid(row=1,column=1)
        l5=Label(self.frame2,text = 'Confirm password: ',font = ('',20)).grid(sticky = W)
        e5=Entry(self.frame2,textvariable = self.n_re_password,font=('',15),show = '*',bg="Light Pink").grid(row=2,column = 1)
        b3=Button(self.frame2,text = 'Create Account',font = ('',15),bd=3,padx=5,pady=5,command=self.new_user_).grid()
        b4=Button(self.frame2,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command = self.log).grid(row=3,column=1)

    def registration(self):
        self.frame.pack_forget()
        self.frame4 = Frame(self.master,padx =50,pady = 50)
        self.frame4.pack()
        self.head = Label(self.frame4,text = ' REGISTRATION FORM ',font = ('',25),fg="White",pady=50,padx=10,bg = 'Royal Blue')
        l1=Label(self.frame4,text = 'FULL NAME : ',font = ('',20)).grid(sticky = W)
        e1=Entry(self.frame4,textvariable =self.full_name,font = ('',15),bg="Light Pink").grid(row=0,column=1)
        l2=Label(self.frame4,text = 'EMAIL : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame4,textvariable =self.email_id ,font = ('',15),bg="Light Pink").grid(row=1,column=1)
        l2=Label(self.frame4,text = 'GENDER : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame4,textvariable =self.gender ,font = ('',15),bg="Light Pink").grid(row=2,column=1)
        l2=Label(self.frame4,text = 'LOCATION : ',font = ('',20)).grid(sticky = W)
        e2=Entry(self.frame4,textvariable =self.location ,font = ('',15),bg="Light Pink").grid(row=3,column=1)
        Button(self.frame4,text = ' SUBMIT ',bd = 3 ,font = ('',20),command=self.submit_data).grid(row=4,column=1)



root = Tk(screenName='Lotus IT Hub')
root.configure(background="Royal Blue")
final(root)
root.mainloop()
