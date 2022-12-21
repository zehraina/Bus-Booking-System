from tkinter import*
from tkinter.messagebox import *
# from Enter_your_journey_details import*
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

import sqlite3
con=sqlite3.Connection("Database_211b140")
cur=con.cursor()

# cur.execute('')
# c=con.execute('select p.name, p.seat, o.id, br.run_date, p.gender, p.phone, bs.fare, r.st_name FROM PASSENGER_details AS p, OPERATOR AS o, bus_details as bs, runs as br , route_details as r ORDER BY DESC')

# print(c[0])
