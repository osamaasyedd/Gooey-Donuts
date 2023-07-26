import csv
from tkinter import *
from tkinter import Entry
from abc import ABC,abstractmethod

class Abstract(ABC): #abstract class
    @abstractmethod #decorator
    def window_tag(self): #abstract method
        pass


class Login_Page:
    User='abc'
    def window_tag(self):
        self.labl = Label(self.w1, text='Login Here ⇓',font='Roboto 10 bold',fg="white",bg="#40048c").grid(row=2, column=2)

    def credentials(self): #opens up Login Window
        self.w1 = Tk()
        self.w1.title('Gooey Donuts')
        self.w1.geometry('340x300+550+200')
        self.w1.configure(bg="#40048c")
        self.username = StringVar()
        self.password = StringVar()
        self.labl = Label(self.w1, text='Welcome to',font='Helevita 15',fg="white",bg="#40048c",height=1).grid(row=0, column=2)
        self.labl0 = Label(self.w1, text='GOOEY DONUTS',font=('Helvetica','15','italic','bold'),fg='#ff90ff',bg="#40048c",height=2).grid(row=1, column=2)
        self.labl1 = Label(self.w1, text='  USERNAME:',fg="white",bg="#40048c").grid(row=3, column=1)
        self.labl2 = Label(self.w1, text='  PASSWROD:',fg="white",bg="#40048c").grid(row=4, column=1)
        self.e1 = Entry(self.w1,textvariable=self.username).grid(row=3, column=2)
        self.e2 = Entry(self.w1, textvariable=self.password,show='*').grid(row=4, column=2)
        self.labl3 = Label(self.w1,bg="#40048c",height=3).grid(row=3, column=3)
        self.labl4 = Label(self.w1, text='(Lowercase)',fg="white",bg="#40048c").grid(row=3, column=3)
        self.labl5 = Label(self.w1,bg="#40048c",height=1).grid(row=5, column=3)
        self.b = Button(self.w1, text='Login', command=self.login).grid(row=6, column=2)
        self.b = Button(self.w1, text='Create an account', command=self.signup).grid(row=7, column=2)
        self.window_tag()
        self.w1.mainloop()
    

    def login(self): #called when Login button is pressed (checks user credentials from 'credentials' file)
        f = open("credentials.csv", mode='r+')
        r = csv.reader(f)
        l0 = []
        l1=[]
        l0.append(self.username.get())
        l0.append(self.password.get())
        Login_Page.User=l0[0]
        for row in r:
            l1.append(row)
        if l0 in l1:
            self.popUp1('Checking...','Login successful!')
        else:
            self.popUp('Error','Username and password doesn\'t match')
        
    def popUp(self,title,message): #opens up popup window for displaying the provided messsage
        r=Tk()
        r.title(title)
        r.geometry("250x100")
        r.configure(bg="#40048c")
        m=message
        lab=Label(r,text=m,fg="white",bg="#40048c").grid(row=2,column=2)
        b1=Button(r,text='OK',command=r.destroy).grid(row=3,column=2)
        r.mainloop()
        
    def popUp1(self,title,message):  #opens up popup window for displaying the provided messsage and destroys Login window
        r=Tk()
        r.title(title)
        r.geometry("230x100+600+300")
        r.configure(bg="#40048c")
        m=message
        lab=Label(r,text=m,fg="white",bg="#40048c").grid(row=2,column=2)
        b1=Button(r,text='OK',command=lambda:[r.destroy(),self.w1.destroy()]).grid(row=3,column=2)
        r.mainloop()
        

    def signup(self): #open up Sign Up window
        self.w2= Tk() 
        self.w2.title("Create an Account")
        self.w2.geometry("350x200")
        self.w2.configure(bg="#40048c")
        name= Label(self.w2, text='Username',fg="white",bg="#40048c").grid(row=2, column=1)
        password= Label(self.w2, text='Password',fg="white",bg="#40048c").grid(row=3, column=1)
        re_password= Label(self.w2, text='Re-Enter Password',fg="white",bg="#40048c").grid(row=4, column=1)
        email=Label(self.w2,text='Email',fg="white",bg="#40048c").grid(row=5, column=1)
        self.Name = Entry(self.w2)
        self.Name.grid(row=2, column=2)
        self.Password = Entry(self.w2,show='*')
        self.Password.grid(row=3, column=2)
        self.Re_password = Entry(self.w2,show='*')
        self.Re_password.grid(row=4, column=2)
        self.Email = Entry(self.w2)
        self.Email.grid(row=5, column=2)
        labl3 = Label(self.w2, text='(Lowercase)',fg="white",bg="#40048c").grid(row=2, column=3)
        labl4 = Label(self.w2, text='limit upto 7 characters',fg="white",bg="#40048c").grid(row=3, column=3)
        labl5 = Label(self.w2,bg="#40048c",height=1).grid(row=6, column=2)
        b1 = Button(self.w2, text='Sign Up', command=self.register).grid(row=7, column=2)
        self.w2.mainloop()
    
    def register(self): #called when Sign Up button is pressed (appends new user credentials to the 'credentails' file)
        user_info=[]
        user_info.append(self.Name.get())
        Pass=self.Password.get()
        Re_pass=self.Re_password.get()
        if len(Pass)<=7:
            if Pass==Re_pass:
                user_info.append(Pass)
            else:
                self.popUp('Error','Pass confirmation failed! Re-Enter pass')
        else:
            self.popUp('Error','Pass limit: upto 7 characters')
        f = open("credentials.csv", mode='a+',newline='')
        r = csv.writer(f)        
        r.writerow(user_info)
        f.close()
        self.popUp2('...','Registration Successful')

    def popUp2(self,title,message): #opens up popup window for displaying the provided messsage and destroys Sign Up window
        r=Tk()
        r.title(title)
        r.geometry("250x100")
        r.configure(bg="#40048c")
        m=message
        lab=Label(r,text=m,fg="white",bg="#40048c").grid(row=2,column=2)
        b1=Button(r,text='OK',command=lambda:[r.destroy(),self.w2.destroy()]).grid(row=3,column=2)
        r.mainloop()
    

class Inventory(Login_Page):
    def window_tag(self):
        self.labl = Label(self.w3, text='Go Nuts For Donuts!',font=('Helevita','13','italic','bold'),fg="white",bg="#40048c",height=2).grid(row=0, column=3)

    def store(self): #Opens the Store
        self.w3=Tk()
        self.w3.title("Gooey Donut Shop")
        self.w3.geometry("600x500+400+70")
        self.w3.configure(bg="#40048c")
        self.window_tag()

        #serial no
        lable=Label(self.w3,text=" ",bg="#40048c",font=("arial",13,"bold")).grid(row=0,column=0,sticky='W', padx=2, pady=2)                                   
        lab=Label(self.w3,text=" ",bg="#40048c",font=("arial",13,"bold")).grid(row=0,column=1,sticky='W', padx=2, pady=2)
        lab=Label(self.w3,text=" ",bg="#40048c",font=("arial",13,"bold")).grid(row=0,column=2,sticky='W', padx=2, pady=2)                                   
        lab0=Label(self.w3,text=" ",bg="#40048c",font=("arial",13,"bold")).grid(row=1,column=1,sticky='W', padx=2, pady=2)                                   
        lab1=Label(self.w3,text="1.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=2,column=1,sticky='W', padx=2, pady=2)
        lab2=Label(self.w3,text="2.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=3,column=1,sticky='W', padx=2, pady=2)
        lab3=Label(self.w3,text="3.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=4,column=1,sticky='W', padx=2, pady=2)
        lab4=Label(self.w3,text="4.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=5,column=1,sticky='W', padx=2, pady=2)
        lab5=Label(self.w3,text="5.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=6,column=1,sticky='W', padx=2, pady=2)
        lab6=Label(self.w3,text="6.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=7,column=1,sticky='W', padx=2, pady=2)
        lab7=Label(self.w3,text="7.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=8,column=1,sticky='W', padx=2, pady=2)
        lab8=Label(self.w3,text="8.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=9,column=1,sticky='W', padx=2, pady=2)
        lab9=Label(self.w3,text="9.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=10,column=1,sticky='W', padx=2, pady=2)
        lab10=Label(self.w3,text="10.",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=11,column=1,sticky='W', padx=2, pady=2)

        #flavors
        lab0=Label(self.w3,text="DONUT FLAVORS",fg="#ff90ff",bg="#40048c",font=("arial",13,"bold")).grid(row=1,column=2,
                                                                                            sticky='W', padx=2, pady=2)                                    
        lab1=Label(self.w3,text="Original/Plain",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=2,column=2,sticky='W', padx=2, pady=2)
        lab2=Label(self.w3,text="Sugar",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=3,column=2,sticky='W', padx=2, pady=2)
        lab3=Label(self.w3,text="Chocolate Iced",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=4,column=2,sticky='W', padx=2, pady=2)
        lab4=Label(self.w3,text="Strawberry Iced",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=5,column=2,sticky='W', padx=2, pady=2)
        lab5=Label(self.w3,text="Powdered",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=6,column=2,sticky='W', padx=2, pady=2)
        lab6=Label(self.w3,text="Coffee Roll",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=7,column=2,sticky='W', padx=2, pady=2)
        lab7=Label(self.w3,text="Jelly Filled",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=8,column=2,sticky='W', padx=2, pady=2)
        lab8=Label(self.w3,text="Sour Cream",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=9,column=2,sticky='W', padx=2, pady=2)
        lab9=Label(self.w3,text="Blueberry",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=10,column=2,sticky='W', padx=2, pady=2)
        lab10=Label(self.w3,text="Cotton Candy",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=11,column=2,sticky='W', padx=2, pady=2)

        
        #price
        lab0=Label(self.w3,text="PRICE",fg="#ff90ff",bg="#40048c",font=("arial",13,"bold")).grid(row=1,column=3,padx=2, pady=2)
        lab1=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold") ).grid(row=2,column=3, padx=2, pady=2)
        lab2=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=3,column=3, padx=2, pady=2)
        lab3=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=4,column=3,padx=2, pady=2)
        lab4=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=5,column=3, padx=2, pady=2)
        lab5=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=6,column=3, padx=2, pady=2)
        lab6=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold") ).grid(row=7,column=3, padx=2, pady=2)
        lab7=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=8,column=3, padx=2, pady=2)
        lab8=Label(self.w3,text="150/-" ,fg="white",bg="#40048c",font=("arial",12,"bold")).grid(row=9,column=3, padx=2, pady=2)
        lab9=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold") ).grid(row=10,column=3,padx=2, pady=2)
        lab10=Label(self.w3,text="150/-",fg="white",bg="#40048c",font=("arial",12,"bold") ).grid(row=11,column=3,padx=2, pady=2)
        
         #Entry  
        lab1=Label(self.w3,text="ENTER QUANTITY (Max 50)",fg="#ff90ff",bg="#40048c",font=("arial",13,"bold")).grid(row=1,column=4,
                                                                                            sticky='W', padx=2, pady=2)
        self.ent1=IntVar()
        self.ent2=IntVar()
        self.ent3=IntVar()
        self.ent4=IntVar()
        self.ent5=IntVar()
        self.ent6=IntVar()
        self.ent7=IntVar()
        self.ent8=IntVar()
        self.ent9=IntVar()
        self.ent10=IntVar()
        self.e1=Entry(self.w3, textvariable=self.ent1).grid(row=2,column=4)
        self.e2=Entry(self.w3, textvariable=self.ent2).grid(row=3,column=4)
        self.e3=Entry(self.w3, textvariable=self.ent3).grid(row=4,column=4)
        self.e4=Entry(self.w3, textvariable=self.ent4).grid(row=5,column=4)
        self.e5=Entry(self.w3, textvariable=self.ent5).grid(row=6,column=4)
        self.e6=Entry(self.w3, textvariable=self.ent6).grid(row=7,column=4)
        self.e7=Entry(self.w3, textvariable=self.ent7).grid(row=8,column=4)
        self.e8=Entry(self.w3, textvariable=self.ent8).grid(row=9,column=4)
        self.e9=Entry(self.w3, textvariable=self.ent9).grid(row=10,column=4)
        self.e10=Entry(self.w3, textvariable=self.ent10).grid(row=11,column=4)
        Button(self.w3, text='Add to Cart', command=self.add_to_cart).grid(row=12, column=4)
        Button(self.w3, text='Proceed to Checkout', command=self.destroyer1).grid(row=13, column=4)
        Button(self.w3, text='Previous Orders', command=self.Previous_orders).grid(row=14, column=4)
        self.w3.mainloop()

    def Previous_orders(self): #calls the show_Orders method of class Cart_history
        return Cart_history.show_Orders()

    def destroyer1(self): #destroys Store window and opens Cart window
        self.w3.destroy()
        return self.Cart_details()


    def add_to_cart(self): #Adds all the user selected items to the Cart and stores them in 'Cart.csv'
        c=[Login_Page.User]
        c.append(self.ent1.get())
        c.append(self.ent2.get())
        c.append(self.ent3.get())
        c.append(self.ent4.get())
        c.append(self.ent5.get())
        c.append(self.ent6.get())
        c.append(self.ent7.get())
        c.append(self.ent8.get())
        c.append(self.ent9.get())
        c.append(self.ent10.get())
        count=0
        #exception handling
        try: 
            validate_c=c[1:]
            for i in validate_c:
                if i>=50:
                    count+=1
            if count>0:
                raise ValueError(Login_Page.popUp(self,'Error','Invalid Value Error!'))
            f = open("Cart.csv", mode='w', newline='')
            w = csv.writer(f)
            w.writerow(c)
            f.close()
            Login_Page.popUp(self,'Loading...','Cart Updated!')
        except ValueError as e1:
            print (e1)    

    def Cart_details(self):  #opens up cart and allows for the change of purchasing items
        self.w4 = Tk()
        self.w4.title("Shopping Cart")
        self.w4.geometry("500x500+400+70")
        self.w4.configure(bg="#40048c")
        f=open("Cart.csv", 'r', newline='')
        a = csv.reader(f)
        self.c2=[]
        self.c3=[]
        for row in a:
            if row[0] == Login_Page.User:
                self.c2=row
                self.c3=row[1: ]
                break
            else:
                continue
        f.close()
        self.total=0
        for i in self.c3:
            self.total+=int(i)
        self.Total = self.total*150


        l = Label(self.w4, text= '            Your Cart', font=('Times New Roman', '15','bold'),fg="white",bg="#40048c").grid(row=0, column=0)
        l = Label(self.w4, text='',bg="#40048c").grid(row=0, column=1)
        l1 = Label(self.w4, text='  Original/Plain: ' + str(self.c3[0]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=1, column=0,sticky=(S,W))
        l2 = Label(self.w4, text='  Sugar: ' + str(self.c3[1]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=2, column=0,sticky=(S,W))
        l3 = Label(self.w4, text='  Chocolate Iced: ' + str(self.c3[2]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=3, column=0,sticky=(S,W))
        l4 = Label(self.w4, text='  Strawberry Iced: ' + str(self.c3[3]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=4, column=0,sticky=(S,W))
        l5 = Label(self.w4, text='  Powdered: ' + str(self.c3[4]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=5, column=0,sticky=(S,W))
        l6 = Label(self.w4, text='  Coffee Roll: ' + str(self.c3[5]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=6, column=0,sticky=(S,W))
        l7 = Label(self.w4, text='  Jelly Filled: ' + str(self.c3[6]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=7, column=0,sticky=(S,W))
        l8 = Label(self.w4, text='  Sour Cream: ' + str(self.c3[7]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=8, column=0,sticky=(S,W))
        l9 = Label(self.w4, text='  Blueberry: ' + str(self.c3[8]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=9, column=0,sticky=(S,W))
        l10 = Label(self.w4, text='  Cotton Candy: ' + str(self.c3[9]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=10, column=0,sticky=(S,W))
        l11 = Label(self.w4, text='  Total (Rs.): ', font=('Cambria', '11', 'bold'),fg="white",bg="#40048c",height=3).grid(row=12, column=0,sticky=(S,W))
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
        b1 = Button(self.w4, text='Edit Quantity', command=self.EditCart1).grid(row=1, column=1)
        b2 = Button(self.w4, text='Edit Quantity', command=self.EditCart2).grid(row=2, column=1)
        b3 = Button(self.w4, text='Edit Quantity', command=self.EditCart3).grid(row=3, column=1)
        b4 = Button(self.w4, text='Edit Quantity', command=self.EditCart4).grid(row=4, column=1)
        b5 = Button(self.w4, text='Edit Quantity', command=self.EditCart5).grid(row=5, column=1)
        b6 = Button(self.w4, text='Edit Quantity', command=self.EditCart6).grid(row=6, column=1)
        b7 = Button(self.w4, text='Edit Quantity', command=self.EditCart7).grid(row=7, column=1)
        b8 = Button(self.w4, text='Edit Quantity', command=self.EditCart8).grid(row=8, column=1)
        b9 = Button(self.w4, text='Edit Quantity', command=self.EditCart9).grid(row=9, column=1)
        b10 = Button(self.w4, text='Edit Quantity', command=self.EditCart10).grid(row=10, column=1)
        b0=Button(self.w4, text='Back to Store', command=self.destroyer2).grid(row=13, column= 0)
        bpayment = Button(self.w4, text='Place Order', command=self.place_order).grid(row=13, column=1)
        self.w4.mainloop()

    def place_order(self): #clears current cart and  transfers all the current cart data to 'Previous Orders.csv' 
        c_null=['None',0,0,0,0,0,0,0,0,0,0]
        c_new=[]
        with open ('Cart.csv','r',newline='') as x:
            for row in csv.reader(x):
                c_new=row
        with open('Previous Orders.csv','a+',newline='') as y:
            writer=csv.writer(y)
            writer.writerow(c_new)
        with open('Cart.csv','w',newline='') as z:
            writer=csv.writer(z)
            writer.writerow(c_null)
        Login_Page.popUp(self,'Loading...','Your order has been placed!')
            
    def destroyer2(self): #destroys Cart window and opens up Store window
        self.w4.destroy()
        return self.store()

    def EditCart1(self): #asks for the quantity change and updates the quantity
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update1).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart2(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update2).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart3(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update3).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart4(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update4).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart5(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update5).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart6(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update6).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart7(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update7).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart8(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update8).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart9(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update9).grid(row=2, column=1)
        self.root1.mainloop()
    def EditCart10(self):
        self.root1=Tk()
        self.root1.title('Update Cart')
        self.root1.geometry('250x100+550+200')
        self.root1.configure(bg="#40048c")
        self.entry=Entry(self.root1)
        self.entry.insert(END, 0)
        self.entry.grid(row=1,column=1)
        b= Button(self.root1, text='Update', command=self.call_Update10).grid(row=2, column=1)
        self.root1.mainloop()

    def call_Update1(self): #calls the UpdateCart method and updates the item labels as well as Total
        self.UpdateCart(1)
        l1 = Label(self.w4, text='  Original/Plain: ' + str(self.c3[0]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=1, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update2(self):
        self.UpdateCart(2)
        l2 = Label(self.w4, text='  Sugar: ' + str(self.c3[1]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=2, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update3(self):
        self.UpdateCart(3)
        l3 = Label(self.w4, text='  Chocolate Iced: ' + str(self.c3[2]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=3, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update4(self):
        self.UpdateCart(4)
        l4 = Label(self.w4, text='  Strawberry Iced: ' + str(self.c3[3]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=4, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update5(self):
        self.UpdateCart(5)
        l5 = Label(self.w4, text='  Powdered: ' + str(self.c3[4]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=5, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update6(self):
        self.UpdateCart(6)
        l6 = Label(self.w4, text='  Coffee Roll: ' + str(self.c3[5]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=6, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update7(self):
        self.UpdateCart(7)
        l7 = Label(self.w4, text='  Jelly Filled: ' + str(self.c3[6]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=7, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update8(self):
        self.UpdateCart(8)
        l8 = Label(self.w4, text='  Sour Cream: ' + str(self.c3[7]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=8, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update9(self):
        self.UpdateCart(9)
        l9 = Label(self.w4, text='  Blueberry: ' + str(self.c3[8]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=9, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)
    def call_Update10(self):
        self.UpdateCart(10)
        l10 = Label(self.w4, text='  Cotton Candy: ' + str(self.c3[9]), font=('Cambria 10'),fg="white",bg="#40048c").grid(row=10, column=0,sticky=(S,W))
        self.t=0
        for i in self.c3:
            self.t+=int(i)
        self.Total = self.t*150
        l12 = Label(self.w4, text=self.Total, font=('Cambria 10'),fg="white",bg="#40048c",height=4).grid(row=12, column=1)

    def UpdateCart(self,a): #updates the items quantity in the 'Cart.csv'
        b=self.entry.get()
        self.c3[a-1]=b
        self.c2[a] = b
        self.root1.destroy()
        f = open("Cart.csv", 'w', newline='')
        w = csv.writer(f)
        w.writerow(self.c2)
        f.close()
        
class Cart_history(Inventory): 
    def show_Orders(): #shows all the Previous Orders of user
        w5= Tk() 
        w5.title("Previous orders")
        w5.geometry("600x400")
        w5.configure(bg="white")
        with open ('Previous Orders.csv','r',newline='') as f:
            a = csv.reader(f)
            c4=[]
            for row in a:
                if row[0] == Login_Page.User:
                    c4.append(row[1: ])
        count=1
        for quantity in c4:
                a=quantity[0]
                b=quantity[1]
                c=quantity[2]
                d=quantity[3]
                e=quantity[4]
                f=quantity[5]
                g=quantity[6]
                h=quantity[7]
                i=quantity[8]
                j=quantity[9]
                Label(w5,text='Order '+str(count)+'                  ',font=("roboto",10,"bold"),fg="#40048c",bg="white").grid(row=0,column=count)
                Label(w5,text='Original/Plain: '+str(a),fg="#40048c",bg="white").grid(row=1,column=count,sticky='W')
                Label(w5,text='Sugar: '+str(b),fg="#40048c",bg="white").grid(row=2,column=count,sticky='W')
                Label(w5,text='Chocolate Iced: '+str(c),fg="#40048c",bg="white").grid(row=3,column=count,sticky='W')
                Label(w5,text='Strawberry Iced: '+str(d),fg="#40048c",bg="white").grid(row=4,column=count,sticky='W')
                Label(w5,text='Powdered: '+str(e),fg="#40048c",bg="white").grid(row=5,column=count,sticky='W')
                Label(w5,text='Coffee Roll: '+str(f),fg="#40048c",bg="white").grid(row=6,column=count,sticky='W')
                Label(w5,text='Jelly Filled: '+str(g),fg="#40048c",bg="white").grid(row=7,column=count,sticky='W')
                Label(w5,text='Sour Cream: '+str(h),fg="#40048c",bg="white").grid(row=8,column=count,sticky='W')
                Label(w5,text='Blueberry: '+str(i),fg="#40048c",bg="white").grid(row=9,column=count,sticky='W')
                Label(w5,text='Cotton Candy: '+str(j),fg="#40048c",bg="white").grid(row=10,column=count,sticky='W')
                count+=1
        w5.mainloop()
   

a=Login_Page()
a.credentials()
b=Inventory()
b.store()
