#import modules
from tkinter import *
import mysql.connector
from tkinter import messagebox
import math,random,os
import builtins
import importlib.util as iu

#class for front end ui
class Product:

    def  __init__ (self,root):

        #create object reference instance of database class as p
        p=Database()
        p.conn()

        self.root = root
        self.root.title("CUSTOMER MANAGEMENT")
        self.root.geometry("1260x640+50+50")
        self.root.config(bg="grey")

        cid=StringVar()
        cname=StringVar()
        cost=StringVar()
        date =StringVar()
        company=StringVar()
        contact=StringVar()
        mop=StringVar()
        bill=StringVar()

        '''lets call database methods to perform operations'''

        
        #function to close the frame
        def close():
            print("Product : close method called")
            close=messagebox.askyesno("CUSTOMER MANAGEMENT","ARE YOU SURE")
            if close>0:
                root.destroy()
                print("Product : close method finished\n")
                return


        #function to clear 
        def clear():
            print("Product : clear method called")
            self.txtcid.delete(0,END)
            self.txtcname.delete(0,END)
            self.txtcost.delete(0,END)
            self.txtdate .delete(0,END)
            self.txtcompany.delete(0,END)
            self.txtcontact.delete(0,END)
            self.txtmop.delete(0,END)
            self.txtbill.delete(0,END)
            print("Product : clear method finished")


        #function to save the details in db
        def insert():
            print("Product : insert method called")
            if (len(cid.get())!=0):
                p.insert(cid.get(),cname.get(),cost.get(),date.get(),
                         company.get(),contact.get(),mop.get(),bill.get())
                productList.delete(0,END)
                productList.insert(END,cid.get(),cname.get(),cost.get(),date.get(),
                         company.get(),contact.get(),mop.get(),bill.get())
                showInProductList()
            else:
                messagebox.askyesno("CUSTOMER MANAGEMENT","INSERT ID")
                
            print("Product : insert method finished\n")
            

        # function to show table data scroll list
        def showInProductList() :
            print("Product : showInProductList method called")
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END,row,str(""))
            print("Product : showInProductList method finished\n")

        

        def prodctRec(event):
            print("Product : prodctRec method called")
            global pd

            searchPd=productList.curselection()[0]
            pd=productList.get(searchPd)

            self.txtcid.delete(0,END)
            self.txtcid.insert(END,pd[0])
            
            self.txtcname.delete(0,END)
            self.txtcname.insert(END,pd[1])
            
            self.txtcost.delete(0,END)
            self.txtcost.insert(END,pd[2])
            
            self.txtdate .delete(0,END)
            self.txtdate .insert(END,pd[3])
            
            self.txtcompany.delete(0,END)
            self.txtcompany.insert(END,pd[4])
            
            self.txtcontact.delete(0,END)
            self.txtcontact.insert(END,pd[5])

            self.txtmop.delete(0,END)
            self.txtmop.insert(END,pd[6])

            self.txtbill.delete(0,END)
            self.txtbill.insert(END,pd[7])

            print("Product : prodctRec method finished")


        #function to delete the data from database table

        def delete():
            print("Product : delete method called")
            if (len(cid.get())!=0):
                p.delete(pd[0])
                clear()
                showInProductList()
            print("Product : delete method finished\n")

        #search record from database table
        def search():
            print("Product : search method called")
            productList.delete(0,END)
            for row in p.search(cid.get(),cname.get(),cost .get(),date.get(),
                         company.get(),contact.get(),mop.get(),bill.get()):
                productList.insert(END,row,str(""))

            print("Product : search method finished")



        #function to update the record
        def update():
            print("Product : update method called")
            if (len(cid.get())!=0):
                #print("pd[0]",pd[p])
                p.delete(pd[0])
            if (len(cid.get())!=0):
                p.insert(cid.get(),cname.get(),cost .get(),date.get(),
                         company.get(),contact.get(),mop.get(),bill.get())
                productList.delete(0,END)
            productList.insert(END,(cid.get(),cname.get(),cost.get(),date.get(),
                         company.get(),contact.get(),mop.get(),bill.get()))
            print("Product : update method finished\n")



        def openbill():
            
            v=os.getcwd()
            present="no"
            for i in os.listdir(""+v+"\\Bill\\"):
                if i.split(".")[0]==bill.get():
                    f1=open(""+v+"\\Bill\\"+str(i),"r")                 
                    window=Tk()
                    window.title("Bill")
                    window.geometry("440x350+450+240")
                    billframe=Frame(window,bd=10,relief=GROOVE)
                    billframe.place(width=440,height=350)
                    bill_title=Label(billframe,text="BILL ",
                                 font="arial 15 ",bd=7,relief=GROOVE).pack(fill=X)
                    scrol_y=Scrollbar(billframe,orient=VERTICAL)
                    self.textarea=Text(billframe,yscrollcommand=scrol_y.set)
                    scrol_y.pack(side=RIGHT,fill=Y)
                    scrol_y.config(command=self.textarea.yview)
                    self.textarea.pack(fill=BOTH,expand=1)
                    self.textarea.delete('1.0',END)
                    for d in f1:
                        self.textarea.insert(END,d)
                    f1.close()
                    present="yes"
            if present=="no":
                messagebox.showerror("Error","Invalid Bill No")
                
             


             
           

        ''' create frame '''
        mainframe= Frame(self.root,bg="grey")
        mainframe.grid()

        headframe =Frame(mainframe,bd=1,padx=50,pady=10,bg='black',relief=RIDGE)
        headframe.pack(side=TOP)

        self.ITitle = Label(headframe, font=('arial',50,'bold'), fg='grey',
                             text='Customer Management',bg='black')
        self.ITitle.grid()

        operationframe=Frame(mainframe,bd=5,width=1300,height=60,padx=50,pady=20,bg='grey',
                             relief=RIDGE)
        operationframe.pack(side=BOTTOM)

        bodyframe=Frame(mainframe,bd=5,width=1290,height=400,padx=30,pady=20,bg='black',
                             relief=RIDGE)
        bodyframe.pack(side=BOTTOM)

        leftbody= LabelFrame(bodyframe,bd=5,width=600,height=380,padx=20,pady=10,bg='grey',
                             relief=RIDGE, font=('arial',15,'bold') ,text='CUSTOMER DETAILS')
        leftbody.pack(side=LEFT)

        rightbody= LabelFrame(bodyframe,bd=5,width=400,height=380,padx=20,pady=10,bg='grey',
                             relief=RIDGE, font=('arial',15,'bold') ,
                              text='DATA')
        rightbody.pack(side=RIGHT)
        

        ''' add widgets to left body '''

        self.labelcid=Label(leftbody, font=('arial',15,'bold'),text="Customer Id :",padx=2,
                            bg='grey',fg='black')
        self.labelcid.grid(row=0,column=0,sticky=W)
        self.txtcid = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                            textvariable=cid,width=30)
        self.txtcid.grid(row=0,column=1,sticky=W)

        self.labelcname=Label(leftbody, font=('arial',15,'bold'),text="Customer Name :",padx=2,
                            bg='grey',fg='black')
        self.labelcname.grid(row=1,column=0,sticky=W)
        self.txtcname = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                              textvariable=cname,width=30)
        self.txtcname.grid(row=1,column=1,sticky=W)


        self.labelcost=Label(leftbody, font=('arial',15,'bold'),text="Cost :",padx=2,
                            bg='grey',fg='black')
        self.labelcost.grid(row=2,column=0,sticky=W)
        self.txtcost = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                             textvariable=cost,width=30)
        self.txtcost.grid(row=2,column=1,sticky=W)
        

        self.labeldate =Label(leftbody, font=('arial',15,'bold'),text="Date of order :",padx=2,
                            bg='grey',fg='black')
        self.labeldate .grid(row=3,column=0,sticky=W)
        self.txtdate  = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                              textvariable=date ,width=30)
        self.txtdate .grid(row=3,column=1,sticky=W)
        

        self.labelcompany=Label(leftbody, font=('arial',15,'bold'),text="Company :",padx=2,
                            bg='grey',fg='black')
        self.labelcompany.grid(row=4,column=0,sticky=W)
        self.txtcompany = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                                textvariable=company,width=30)
        self.txtcompany.grid(row=4,column=1,sticky=W)
        

        self.labelcontact=Label(leftbody, font=('arial',15,'bold'),text="Contact :",padx=2,
                            bg='grey',fg='black')
        self.labelcontact.grid(row=5,column=0,sticky=W)
        self.txtcontact = Entry(leftbody,font=('arial',15,'bold'),bg='white',
                                textvariable=contact,width=30)
        self.txtcontact.grid(row=5,column=1,sticky=W)

        self.labelmof=Label(leftbody,font=('arial',15,'bold'),text="Mode of payment :",padx=2,
                            bg='grey',fg='black',pady=2)
        self.labelmof.grid(row=6,column=0,sticky=W)
        self.txtmop = Entry(leftbody,font=('arial',15,'bold'),bg='white',textvariable=mop,
                            width=30)
        self.txtmop.grid(row=6,column=1,sticky=W)
        
        self.labelbill=Label(leftbody,font=('arial',15,'bold'),text="BILL NO.[NULL] :",padx=2,
                            bg='grey',fg='black',pady=2)
        self.labelbill.grid(row=7,column=0,sticky=W)
        self.txtbill = Entry(leftbody,font=('arial',15,'bold'),bg='white',textvariable=bill,
                             width=30)
        self.txtbill.grid(row=7,column=1,sticky=W)
        
        '''self.labelpC3=Label(leftbody,padx=2,pady=2)
        self.labelpC3.grid(row=8,column=0,sticky=W)
        
        self.labelpC4=Label(leftbody,padx=2,pady=2)
        self.labelpC4.grid(row=9,column=0,sticky=W)
        
        self.labelpC5=Label(leftbody,padx=2,pady=2)
        self.labelpC5.grid(row=10,column=0,sticky=W)'''


        #scrollbar
        scroll=Scrollbar(rightbody)
        scroll.grid(row=0,column=1,sticky='ns')
        
        productList=Listbox(rightbody,width=55,height=16,font=('arial',12,'bold'),
                            yscrollcommand=scroll.set)
        
        #called above created prodctRec function from init
        productList.bind('<<ListboxSelect>>',prodctRec)
        productList.grid(row=0,column=0,padx=8)
        
        scroll.config(command=productList.yview)



        #add the buttons
        
        self.buttonSaveData=Button(operationframe,text='SAVE',font=('arial',18,'bold'),
                               height=1,width=10,bd=4,command=insert)
        self.buttonSaveData.grid(row=0,column=0)
        
        self.buttonShow=Button(operationframe,text='SHOW',font=('arial',18,'bold'),
                               height=1,width=10,bd=4,command=showInProductList)
        self.buttonShow.grid(row=0,column=1)
        
        self.buttonClear=Button(operationframe,text='CLEAR',font=('arial',18,'bold'),
                                height=1,width=10,bd=4,command=clear)
        self.buttonClear.grid(row=0,column=2)
        
        self.buttonDelete=Button(operationframe,text='DELETE',font=('arial',18,'bold'),
                                 height=1,width=10,bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=3)
        
        self.buttonUpdate=Button(operationframe,text='UPDATE',font=('arial',18,'bold'),
                                 height=1,width=10,bd=4,command=update)
        self.buttonUpdate.grid(row=0,column=4)
        
        self.buttonSearch=Button(operationframe,text='SEARCH',font=('arial',18,'bold'),
                                 height=1,width=10,bd=4,command=search)
        self.buttonSearch.grid(row=0,column=5)
        
        self.buttonClose=Button(operationframe,text='CLOSE',font=('arial',18,'bold'),
                                height=1,width=10,bd=4,command=close)
        self.buttonClose.grid(row=0,column=6)


        self.buttonbill=Button(leftbody,text='OPEN BILL',font=('arial',18,'bold'),
                                height=1,width=10,bd=4,command=openbill)
        self.buttonbill.grid(row=8,column=1)

        

# back end database operation
class Database:
    
    def conn(self):
        print("Database : connection method called")
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("create database if not exists inventory")
        cur.execute("use inventory")
        query="create table if not exists product1(cid int(10) primary key,\
          cname varchar(30),price char(20),date Date,company char(20),\
          contact varchar(11),mop char(20),bill varchar(4))"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished")

        


    def insert(self,cid,cname,cost,date ,company,contact,mop,bill):
        print("Database : insert method called")
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("use inventory")
        query="insert into product1 values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(cid,cname,cost,date ,company,contact,mop,bill))
        con.commit()
        con.close()
        print("Database : insert method finished")

    def show(self):
        print("Database : show method called")
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("use inventory")
        query="select * from product1"
        cur.execute(query)
        rows=cur.fetchall()
        con.commit()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self,cid):
        print("Database : delete method called",cid)
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("use inventory")
        cur.execute("delete from product1 where cid=%s",(cid,))
        con.commit()
        con.close()
        print(cid,"Database : delete method finished\n")

    def search(self,cid="",name="",price="",date="",company="",contact="",mop="",bill=""):                            
        print("Database : search method called")
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("use inventory")
        cur.execute("select * from product1 where cid=%s or cname=%s or \
            price=%s or date=%s or company=%s or contact=%s or mop=%s or bill=%s",
                    (cid,name,price,date,company,contact,mop,bill))
        row=cur.fetchall()
        con.close()
        print("Database : search method finished\n")
        return row

    def update(self,cid="",name="",price="",qty="",company="",contact="",mop="",bill=""):
        print("Database : update method called")
        con= mysql.connector.connect(host="localhost",user="root",passwd=z)
        cur=con.cursor()
        cur.execute("update product1 set cid=%s or cname=%s or \
            price=%s or date=%s or company=%s or contact=%s or mop=%s or bill=%s where cid=%s",
                    (cid,name,price,cost,date,company,contact,mop,bill,cid))
        con.commit()
        con.close()
        print("Database : update method finished\n")




v=os.getcwd()

c=(v+"\\")
sys.path.insert(0,c)

window=Tk()
window.resizable(width=False, height=False)
window.title("Password Required")
window.geometry("300x100+450+240")

name=Label(window,text="Enter Your MySql Password",
           font=('Helvetica',10,'bold')).place(x=65,y=5)
e=Entry(window,bd=4,show='*')
e.place(x=89,y=30)



def check():

    def popupmsg(msg):
        import tkinter as tk
        popup = tk.Tk()
        popup.resizable(width=False, height=False)
        popup.title("INSTRUCTIONS FOR USAGE")
        popup.geometry("1300x430+30+150")
        
        l = tk.Label(popup, text='INSTRUCTIONS FOR USAGE',bg='white',
                     fg='black', font='Harrington 18 bold')
        l.pack()

        c = tk.Canvas(popup,bg = "white",width="1000",height = "400")
        canvas_id = c.create_text(10, 10, anchor="nw")
        c.pack(fill="both")

        c.itemconfig(canvas_id, text=msg,font=(0,0,'bold'))
        c.insert(canvas_id, 100, " ")       
        
        
        
        b1 = tk.Button(popup, text="OK",font='times 0 bold',bd=3,width=4,
                       bg="white",command = popup.destroy).place(x=650,y=380)
        popup.mainloop()
    try:
        m=mysql.connector.connect(host="localhost",user="root",passwd=e.get())
        global z
        z=e.get()
        window.destroy()
                
        fl=open('Readme.txt','r')
        popupmsg(fl.read())
    

    
        
    except:
        messagebox.showinfo("It's Neccessary","Please Enter The Correct Password.")
        
        
def fun(a):
    if not a:
        messagebox.showinfo("It's Neccessary","Please Enter Your MySql Password.")
        
    else:
        if a=="(NULL)":
            builtins.pas = ''
            check()      
        else:
            builtins.pas = a
            check()

b=Button(window,text="Submit",command=lambda:fun(e.get()),bd=3,bg="white").place(x=125,y=60)
window.bind('<Return>',lambda x:fun(e.get()))
window.mainloop()    


if __name__ =='__main__':
    root =Tk()
    application = Product(root)
    root.mainloop()
        
