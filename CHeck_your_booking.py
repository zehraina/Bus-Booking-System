from tkinter import*
import sqlite3
con=sqlite3.connect('Database_211b140')
cur=con.cursor()
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












root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211b140\\Desktop\\Project\\Bus")
img=PhotoImage(file=".\\Bus.png")


Label(root, image=img).grid(row=0, column=0, padx=700, columnspan=7)
Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=0, padx=300, columnspan=7)
Label(root, text="Check your booking", font='Arial 20 bold', bg="SpringGreen2", fg='forest green').grid(row=2, column=0, padx=300, columnspan=7, pady=40)
Label(root, text="Enter Your Mobile No.:", font='Arial 10 bold').grid(row=3, column=2, sticky=E)
Button(root, text="Check Booking",font='Arial 10 bold', fg='Black').grid(row=3, column=3)

ph_no=IntVar()
# str(ph_no)

# a=Entry(root).grid(row=3, column=3, sticky=W)
a=Entry(root,  textvariable=ph_no).grid(row=3, column=3, sticky=W)
print(ph_no.get())
# print(cur.execute('select name from passenger where phone='+ph).fetchall())
# print(ph)


root.mainloop()