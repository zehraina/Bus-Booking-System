from tkinter import*
from tkinter.messagebox import *


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
    Label(root,text="bus ticket",font='Arial 12 bold').grid(row=2,column=0,columnspan=5)
    Label(frame,text="passenger:",font='Arial 10 bold').grid(row=3,column=0,padx=100)
    # Label(frame,text="Ina",font='Arial 10 bold').grid(row=3,column=1,padx=100)
    Label(frame,text="Gender:",font='Arial 10 bold').grid(row=3,column=1,padx=100)

    Label(frame,text="No Of Seat",font='Arial 10 bold').grid(row=4,column=0,padx=100)

    Label(frame,text="Phone:",font='Arial 10 bold').grid(row=4,column=1,padx=100)

    Label(frame,text="booking Ref.",font='Arial 10 bold').grid(row=5,padx=100)
    Label(frame,text="bus detail",font='Arial 10 bold').grid(row=5,column=1,padx=100)

    Label(frame,text="Travel on:",font='Arial 10 bold').grid(row=6,padx=100)
    Label(frame,text="booked on",font='Arial 10 bold').grid(row=6,column=1,padx=100)

    Label(frame,text="No. of seat:",font='Arial 10 bold').grid(row=7,padx=100)
    Label(frame,text="Boarding point:",font='Arial 10 bold').grid(row=7,column=1,padx=100)
    showinfo('success','seat booked....')
    root.mainloop()
    # import sqlite3
    # con=sqlite3.Connection("Database_211b140")
    # cur=con.cursor()








def main():
    import sqlite3
    con=sqlite3.connect('Database_211b140')
    cur=con.cursor()
    root=Tk()
    root.geometry("1600x1600")
    img=PhotoImage(file=".\\Bus.png")

    Label(root,image=img).grid(row=0,column=0,padx=550,columnspan=12)
    Label(root,text="ONLINE BUS BOOKING SYSTEM",font="Ariel 27 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=12)
    Label(root,text="Add Bus Details",font="Ariel 19 ",bg="snow",fg="dark green").grid(row=2,column=0,pady=20,columnspan=12)
    
    menu2=StringVar()
    menu2.set("Bus Type")
    Drop=OptionMenu(root,menu2,"2x2","AC 2x2","3x2","AC 3x2").grid(row=3,column=3,padx=20)
    
    Label(root,text="Bus id",font="Ariel 11").grid(row=3,column=1)
    Label(root,text="Capacity",font="Ariel 11").grid(row=3,column=4)
    Label(root,text="Fare(Rs.)",font="Ariel 11").grid(row=3,column=6)
    Label(root,text="Operator id",font="Ariel 11").grid(row=3,column=8)
    Label(root,text="Route id",font="Ariel 11").grid(row=3,column=10)

    capacityvar=IntVar()
    farevar=IntVar()
    r_idvar=IntVar()
    op_idvar=IntVar()
    b_idvar=IntVar()

    capacity=Entry(root, textvariable=capacityvar).grid(row=3,column=5)
    fare=Entry(root, textvariable=farevar).grid(row=3,column=7)
    operator_id=Entry(root, textvariable=op_idvar).grid(row=3,column=9)
    route_id=Entry(root, textvariable=r_idvar).grid(row=3,column=11)
    b_id=Entry(root, textvariable=b_idvar).grid(row=3,column=2)

    def save_details():
        
        cap1=capacityvar.get()
        fare1=farevar.get()
        r_id1=r_idvar.get()
        op_id1=op_idvar.get()
        b_id1=b_idvar.get()
        b_type1=menu2.get()
        
        if not cap1:
            showerror('Error','Please fill in all the details.')
        elif not fare1:
            showerror('Error','Please fill in all the details.')
        elif not r_id1:
            showerror('Error','Please fill in all the details.')
        elif not op_id1:    
            showerror('Error','Please fill in all the details.')
        elif not b_id1:     
            showerror('Error','Please fill in all the details.')
        elif not b_type1: 
            showerror('Error','Please fill in all the details.')
        else:
            cur.execute("CREATE TABLE IF NOT EXISTS BUS_DETAILS(bus_id number, r_id number, op_id number, b_type text, capacity number, fare number)")
            if cur.execute("INSERT INTO BUS_DETAILS VALUES (?,?,?,?,?,?)", (b_id1, r_id1, op_id1, b_type1, cap1, fare1)):
                showinfo('Information', 'Details saved successfully!')

            con.commit()
    Button(root,text="Add",font="Ariel 15 bold", command=save_details,fg="black",bg="lightgreen").grid(row=7,column=5,pady=25)
    Button(root,text="Edit",font="Ariel 15 bold",fg="black",bg="lightgreen").grid(row=7,column=6,pady=25)
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2).grid(row=7,column=7,pady=30)
    
    tick()
    # root.mainloop()
    
main()




    # cur.execute('')
    # c=con.execute('select p.name, p.seat, o.id, br.run_date, p.gender, p.phone, bs.fare, r.st_name FROM PASSENGER_details AS p, OPERATOR AS o, bus_details as bs, runs as br , route_details as r ORDER BY DESC')

    # print(c[0])
