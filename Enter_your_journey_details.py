from tkinter import*
from tkinter.messagebox import *
def main():
    
    
    from datetime import date
    today=date.today()
    import sqlite3
    # import bus_ticket
    con=sqlite3.Connection("Database_211b140")
    cur=con.cursor()
    root=Tk()
    root.geometry("1600x1600")
    img=PhotoImage(file=".\\Bus.png")
    Label(root,image=img).grid(row=0,column=0,padx=550,columnspan=12)
    Label(root,text="ONLINE BUS BOOKING SYSTEM",font="Ariel 27 bold",bg="light blue",fg="red4").grid(row=1,column=0,columnspan=12)
    Label(root,text="Enter Journey Details",font="Ariel 19 ",bg="chartreuse2",fg="dark green").grid(row=2,column=0,pady=20,columnspan=12)
    Label(root,text="To",font="Ariel 11 bold").grid(row=3,column=0)
    
    to_var=StringVar()
    date_var=StringVar()
    global from_var
    from_var=StringVar()
    Entry(root, textvariable=to_var).grid(row=3,column=1)
    Label(root,text="From",font="Ariel 11 bold").grid(row=3,column=2)
    Entry(root, textvariable=from_var).grid(row=3,column=3)
    Label(root,text="Date",font="Ariel 11 bold").grid(row=3,column=4)
    Entry(root, textvariable=date_var).grid(row=3,column=5)
    #BUS SELECTION BY PASSENGER
    def fun2():
        # Label(root,text="Select Bus",font="Ariel 13",fg="dark green").grid(row=4,column=1)
        Radiobutton(root,text="Select Bus",font="Ariel 13 ",fg="dark green").grid(row=4,column=1)
        Label(root,text="Operator",font="Ariel 13 ",fg="dark green").grid(row=4,column=2)
        Label(root,text="Bus Type",font="Ariel 13 ",fg="dark green").grid(row=4,column=3)
        Label(root,text="Available/Capacity",font="Ariel 13 ",fg="dark green").grid(row=4,column=4)
        Label(root,text="Fare",font="Ariel 13 ",fg="dark green").grid(row=4,column=5)
        #BUS CHOICES AVAILABLE
        bus_select=IntVar()
        

        Label(root,text=bus_select.get(),font="Ariel 13 ",fg="blue2").grid(row=7,column=5)
        
        # def show_details_from_other_tables():
        global t
        global show_boarding
        t=to_var.get()
        show_boarding=from_var.get()
        t='"'+t+'"'
        
        cur.execute('select o.name, b.b_type, b.capacity, b.fare FROM BUS_DETAILS AS b, OPERATOR AS o, ROUTE_DETAILS AS r  WHERE o.id=b.op_id AND b.r_id=r.r_id AND  r.st_name='+ t)
        # a=cur.execute('select o.name, b.b_type, b.capacity, b.fare FROM BUS_DETAILS AS b, OPERATOR AS o, ROUTE_DETAILS AS r  WHERE  r.st_name="Guna"')
        a=cur.fetchall()
        # print(a)
        for r in a:
            show_name=r[0]
            show_btype=r[1]
            show_capacity=r[2]
            show_fare=r[3]
        # Label(root,text="Select Bus",font="Ariel 13",fg="dark green").grid(row=5,column=1)
        Label(root,text=show_name,font="Ariel 13 ",fg="dark green").grid(row=5,column=2)
        Label(root,text=show_btype,font="Ariel 13 ",fg="dark green").grid(row=5,column=3)
        Label(root,text=show_capacity,font="Ariel 13 ",fg="dark green").grid(row=5,column=4)
        Label(root,text=show_fare,font="Ariel 13 ",fg="dark green").grid(row=5,column=5)
        
        def fun3():
            global namevar
            namevar=StringVar()
            seatsvar=IntVar()
            phonevar=IntVar()
            agevar=IntVar()
            
            Label(root,text="Fill Passenger Details to book the bus ticket",font="Ariel 20 bold",bg="light blue",fg="red4").grid(row=7,column=4)
            Label(root,text="Name",font="Ariel 11 bold").grid(row=8,column=0)
            Entry(root, textvariable=namevar).grid(row=8,column=1)
            gender_menu= StringVar()
            gender_menu.set("Gender")
            Drop=OptionMenu(root,gender_menu,"MALE","FEMALE","OTHER").grid(row=8,column=2)
            Label(root,text="No. of seats",font="Ariel 11 bold").grid(row=8,column=3)
            Entry(root, textvariable=seatsvar).grid(row=8,column=4)
            Label(root,text="Phone",font="Ariel 11 bold").grid(row=8,column=5)
            Entry(root, textvariable=phonevar).grid(row=8,column=6)
            Label(root,text="Age",font="Ariel 11 bold").grid(row=8,column=7)
            Entry(root, textvariable=agevar).grid(row=8,column=8)
            
            def book_seat():
                
                global name1
                global gender1
                global seat1
                global ph1
                global age1
                global date1
                name1=namevar.get()
                gender1=gender_menu.get()
                seat1=seatsvar.get()
                ph1=phonevar.get()
                age1=agevar.get()
                date1=date_var.get()
                d=seat1*show_fare
                d=str(d)
                cur.execute("CREATE TABLE IF NOT EXISTS PASSENGER(name text, gender text, seat number, phone number, age number)")
                if (age1<=0 or age1>=100 or len(str(ph1))!=10):
                    showerror('Error', 'Please enter a valid age/phone number.')
                global res
                res=con.execute('select  b.capacity FROM BUS_DETAILS AS b, OPERATOR AS o, ROUTE_DETAILS AS r  WHERE o.id=b.op_id AND b.r_id=r.r_id AND  r.st_name='+ t)
                res=res.fetchall()
                
                
                if (res[0][0]>=seat1):
                    cur.execute("INSERT INTO PASSENGER VALUES (?,?,?,?,?)", (name1, gender1, seat1, ph1, age1))  
                    showinfo('Fare confirmed', 'Amount to be paid is:'+d )
                    con.commit()
                    global flag
                    flag=-1
                else:
                    showerror('Error', 'Please enter a valid number of seats.')
                
          
            Button(root,text="Book seat",command=book_seat,font="Ariel 11 bold",fg="black",bg="green2").grid(row=9,column=8)

        Button(root,text="Proceed To Book",command=fun3,font="Ariel 11 bold",fg="black",bg="green2").grid(row=6,column=8)
            
    Button(root,text="SHOW BUS",command=fun2,font="Ariel 11 bold",fg="black",bg="green2").grid(row=3,column=6)

        
    def back2home():
        root.destroy()
        import options_screen
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2,command=back2home).grid(row=3,column=7)
    
    def go_to_bus_ticket():
        root.destroy()
        import bus_ticket

    root.mainloop()
    def tick():
        
        root=Tk()

        root.title('page_2')
        # print(name1)
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file='.\\Bus.png')
        Label(root,image=img).grid(row=0,columnspan=5,padx=w//3+100)
        Label(root,text="Online Bus Booking System",font='Arial 18 bold',bg='light blue',fg='red').grid(row=1,columnspan=5,pady=30)
        frame=Frame(root,relief="groove",bd=5)
        frame.grid(row=3,columnspan=5)
        
        showname=name1
        showgender=gender1
        showseat=str(seat1)
        showphone=str(ph1)
        bookingred=1
        # showboarding=show_boarding
    
        showdate=date1
        
        Label(root,text="bus ticket",font='Arial 12 bold').grid(row=2,column=0,columnspan=5)
        Label(frame,text="passenger:"+showname,font='Arial 10 bold').grid(row=3,column=0,padx=100)
        # Label(frame,text="Ina",font='Arial 10 bold').grid(row=3,column=1,padx=100)
        
        Label(frame,text="Gender:"+showgender,font='Arial 10 bold').grid(row=3,column=1,padx=100)

        Label(frame,text="No Of Seat"+showseat,font='Arial 10 bold').grid(row=4,column=0,padx=100)

        Label(frame,text="Phone:"+showphone,font='Arial 10 bold').grid(row=4,column=1,padx=100)

        Label(frame,text="booking Ref.",font='Arial 10 bold').grid(row=5,padx=100)
        Label(frame,text="bus detail",font='Arial 10 bold').grid(row=5,column=1,padx=100)

        Label(frame,text="Travel on:"+showdate,font='Arial 10 bold').grid(row=6,padx=100)
        Label(frame,text="booked on"+str(today),font='Arial 10 bold').grid(row=6,column=1,padx=100)

        Label(frame,text="No. of seat:"+showseat,font='Arial 10 bold').grid(row=7,padx=100)
        # Label(frame,text="Boarding point:"+showboarding,font='Arial 10 bold').grid(row=7,column=1,padx=100)
        Label(frame,text="Boarding point:"+show_boarding,font='Arial 10 bold').grid(row=7,column=1,padx=100)
        showinfo('success','seat booked....')
        val=res[0][0]-seat1
        # print(val)
        cur.execute(f"UPDATE  BUS_DETAILS SET capacity={val} WHERE capacity="+str(res[0][0]) )
        con.commit()
        # cur.execute(f"UPDATE TABLE BUS_DETAISLS SET capacity={val} WHERE ")ṇ

    if (flag==-1):
        
        tick()
    
main()
