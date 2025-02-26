from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="universal_blowers")
mycursor = mydb.cursor()
if mydb:
    print("Connection Established Successfully")
else:
    print("Connection Error")



def Register():
    username = userent.get()
    password = passent.get()
    insert = "Insert into user(username,password) values(%s,%s)"
    if username!="" and password!="":
        values = (username,password)
        mycursor.execute(insert,values)
        mydb.commit()
        messagebox.showinfo("Register Page", "Registered Successfully")
        userent.delete(0,"end")
        passent.delete(0,"end")
    else:
        if(username== "" or password== ""):
            messagebox.askokcancel("Register Page", "Please Fill All Details")

def Show_pass():
    if(showcb_var.get()==1):
        passent.config(show='')
    else:
        passent.config(show='*')

def Login():
    allpasswords =[]
    username = userent.get()
    password = passent.get()
    sql_query = "Select * FROM user WHERE username ='%s' AND password ='%s'" % (username, password)
    mycursor.execute(sql_query)
    myresults = mycursor.fetchall()
    for row in myresults:
        for x in row:
            allpasswords.append(x)          
    if (username and password) in allpasswords:
        messagebox.showinfo("Login Page", "Logged In Successfully")

        for widgets in frame.winfo_children():
            widgets.destroy()
        Mainapp()
    else:
        messagebox.askokcancel("Login Page", "Incorrect Username Or Password")

def Mainapp():
    window.state('zoomed')
    window.title("Universal Blowers and Fabrications")

    logo=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\logo.png")
    logolbl = Label(frame, image=logo, width=100, height=100, bg="#78dbf9")
    logolbl.grid(row=0, column=0, columnspan=2)

    wlcm_lbl=Label(frame, text="Welcome to Universal Blowers and Fabrications", width=40, height=4, bg="#78dbf9", font=("Candara", 18, "bold"))
    wlcm_lbl.grid(row=0, column=2, columnspan=4, pady=40)

    a=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\a.png")
    b1=Button(frame, image = a, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b1.grid(row=4, column=1)
    l1=Label(frame,text ="Industrial Fans/Blowers", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l1.grid(row=5,column=1,pady=20)

    b=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\b.png")
    b2=Button(frame, image = b, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b2.grid(row=4, column=2)
    l2=Label(frame,text ="Axial Flow Fan", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l2.grid(row=5,column=2)

    c=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\c.png")
    b3=Button(frame, image = c, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b3.grid(row=4, column=3)
    l3=Label(frame,text ="Dust Collector", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l3.grid(row=5,column=3)

    d=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\d.png")
    b4=Button(frame, image = d, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b4.grid(row=4, column=4)
    l4=Label(frame,text ="Scrubbers", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l4.grid(row=5,column=4)

    e=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\e.png")
    b5=Button(frame, image = e, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b5.grid(row=4, column=5)
    l5=Label(frame,text ="Turbine Blowers", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l5.grid(row=5,column=5)

    f=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\f.png")
    b6=Button(frame, image = f, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b6.grid(row=4, column=6)
    l6=Label(frame,text ="Air Handling Units", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l6.grid(row=5,column=6)

    g=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\g.png")
    b7=Button(frame, image = g, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b7.grid(row=6, column=1,pady=20)
    l7=Label(frame,text ="Cooling Coils", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l7.grid(row=7,column=1)

    h=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\h.png")
    b8=Button(frame, image = h, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b8.grid(row=6, column=2)
    l8=Label(frame,text ="Steam Coils", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l8.grid(row=7,column=2)

    i=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\i.png")
    b9=Button(frame, image = i, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b9.grid(row=6, column=3)
    l9=Label(frame,text ="Hot Water Coils", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l9.grid(row=7,column=3)

    j=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\j.png")
    b10=Button(frame, image = j, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b10.grid(row=6, column=4)
    l10=Label(frame,text ="Electric Heater", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l10.grid(row=7,column=4)

    k=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\k.png")
    b11=Button(frame, image = k, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b11.grid(row=6, column=5)
    l11=Label(frame,text ="Air Filters", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l11.grid(row=7,column=5)

    l=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\l.png")
    b12=Button(frame, image = l, width=100, height=100, bg="#cde5e4", command=MachineInfo)
    b12.grid(row=6, column=6)
    l12=Label(frame,text ="Air Washers", width=20, height=2, bg="#78dbf9", font=("Candara", 10, "bold"))
    l12.grid(row=7,column=6)
        
    frame.mainloop()

def MachineInfo():
    def Calculate():
        cap=float(cap_var.get())
        qty=float(qty_ent.get())
        price=qty*cap
        gst=price*0.18
        tprice=gst+price
        price_ent.insert(0,tprice)
    def Clear():
        mach_dropdown.delete(0,END)
        cap_dropdown.delete(0,END)
        qty_ent.delete(0,END)
        price_ent.delete(0,END)
    def Submit():
        machines=mach_var.get()
        capacity=float(cap_var.get())
        quantity=float(qty_ent.get())
        tprice=float(price_ent.get())
        insert = "Insert into machine(machines,capacity,quantity,price) values(%s,%s,%s,%s)"
        values = (machines,capacity,quantity,tprice)
        mycursor.execute(insert,values)
        mydb.commit()
        messagebox.showinfo("Thank You", "Data Stored Successfully")


    top=Toplevel()
    top.configure(bg="#78dbf9")
    mac_lbl = Label(top, text="Machine Type:",bg="#78dbf9", font=("Candara", 14, "bold"))
    mac_lbl.grid(row=0, column=0, padx=10, pady=10)
    mach_var = StringVar()
    mach_dropdown = OptionMenu(top, mach_var, "Industrial Fans/Blowers", "Axial Flow Fan", "Dust Collector", "Scrubbers","Turbine Blowers","Air Handling Units","Cooling Coils","Steam Coils","Hot Water Coils","Cooling Coils","Electric Heater","Air Filters","Air Washers")
    mach_dropdown.configure(bg="#cde5e4")
    mach_dropdown.grid(row=0, column=1)

    cap_lbl = Label(top, text="Capacity (in ton):",bg="#78dbf9", font=("Candara", 14, "bold"))
    cap_lbl.grid(row=1, column=0, padx=10, pady=10)
    cap_var = StringVar()
    cap_dropdown = OptionMenu(top, cap_var, "1", "1.5", "2")
    cap_dropdown.configure(bg="#cde5e4")
    #cap_dropdown.insert(0,"1 kg = Rs.12000")
    cap_dropdown.grid(row=1, column=1)

    qty_lbl = Label(top, text="Quantity:",bg="#78dbf9", font=("Candara", 14, "bold"))
    qty_lbl.grid(row=2, column=0, padx=10, pady=10)
    qty_ent = Entry(top,bg="#cde5e4")
    qty_ent.configure(bg="#cde5e4")
    qty_ent.grid(row=2, column=1)

    price_lbl = Label(top, text="Price*:",bg="#78dbf9", font=("Candara", 14, "bold"))
    price_lbl.grid(row=3, column=0, padx=10, pady=10)
    price_ent = Entry(top,bg="#cde5e4")
    price_ent.grid(row=3, column=1)
    gst_lbl = Label(top, text="*18 % GST Applicable",bg="#78dbf9", font=("Candara", 11, "bold"))
    gst_lbl.grid(row=4, column=0)

    calc_bttn = Button(top, text="Calculate", bg="#0098fb",font=("Candara", 11, "bold"),width=10, height=1,command=Calculate)
    calc_bttn.grid(row=3, column=2,padx=10)
    clear_bttn = Button(top, text="Clear", bg="#0098fb",font=("Candara", 11, "bold"), width=10, height=2,command=Clear)
    clear_bttn.grid(row=5, column=0, padx=10, pady=10)
    supplier_var = StringVar()
    subm_bttn = Button(top, text="Submit", bg="#0098fb",font=("Candara", 11, "bold"), width=10, height=2,command=Submit)
    subm_bttn.grid(row=5, column=1)
#Login Window
window = Tk()
window.state('zoomed')
window.configure(bg="#78dbf9")
frame= Frame()
frame.configure(bg="#78dbf9")

window.title("Universal Blowers and Fabrications")

passent_str=tk.StringVar()
showcb_var=IntVar(value=0)

logo=PhotoImage(file="C:\\Users\\raulf\\Desktop\\Mini project\\logo.png")
logolbl = Label(frame, image=logo, width=100, height=100, bg="#78dbf9")
logolbl.grid(row=0, column=0, columnspan=2)

userlbl = Label(frame, text="Username:", width=20, height=2, font=("Candara", 12, "bold"), bg="#78dbf9")
userlbl.grid(row=1, column=0, pady=10)
passlbl = Label(frame, text="Password:", width=20, height=2, font=("Candara", 12, "bold"), bg="#78dbf9")
passlbl.grid(row=2,column=0,)

userent = Entry(frame, width=30, bg="#cde5e4")
userent.grid(row=1, column=1, padx=10)
passent = Entry(frame, width=30, show="*", textvariable=passent_str, bg="#cde5e4")
passent.grid(row=2, column=1, padx=10)

showcb = Checkbutton(frame,text='Show Password',variable=showcb_var,onvalue=1,offvalue=0, font=("Candara", 9), bg="#78dbf9",command=Show_pass)
showcb.grid(row=3, column=1, pady=10)

log_bttn = Button(frame, text="Login", width=10, height=2, font=("Candara", 11, "bold"), bg="#0098fb", fg="#FFFFFF", command=Login)
log_bttn.grid(row=8, column=0, pady=5)
reg_bttn = Button(frame, text="Register", font=("Candara", 11, "bold"), width=10, height=2, bg="#0098fb", fg="#FFFFFF",command=Register)
reg_bttn.grid(row=8, column=1, pady=5)
frame.pack()
window.mainloop()