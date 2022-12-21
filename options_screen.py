from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211b140\\Desktop\\Project\\Bus")
img=PhotoImage(file=".\\Bus.png")

Label(root, image=img).grid(row=0, column=0, padx=550, columnspan=12)
Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=0,columnspan=3, padx=500)
Label(root, text="For admins only", fg="red",font='Arial 12 bold').grid(row=3, column=0)

def book_seat():
    root.destroy()
    import Enter_your_journey_details

def check_booked_seat():
    root.destroy()
    import CHeck_your_booking
    
# def add_bus_details():
#     root.destroy()
#     import add_bus_detail
def go_to_db_add_options():
    root.destroy()
    import Adding_Details_to_DB
    # go_to_db_add_options()

Button(root, text="Seat Booking",command=book_seat, font='Arial 18 bold', fg='Black', bg="SpringGreen2").grid(row=2, column=0, pady=50,padx=40)
Button(root, text="Checked Booked Seat", command=check_booked_seat, font='Arial 18 bold', fg='Black', bg="Green3").grid(row=2, column=1, pady=50, padx=10)
Button(root, text="Add Bus Details",command=go_to_db_add_options, font='Arial 18 bold', fg='Black', bg="Green4").grid(row=2, column=2, pady=50,padx=40)

root.mainloop()
