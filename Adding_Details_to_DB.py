from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211b140\\Desktop\\Project\\Bus")
img=PhotoImage(file=".\\Bus.png")
Label(root, image=img).grid(row=0, column=0, padx=700, columnspan=7)
Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=0, padx=300, columnspan=7)
Label(root, text="Adding Details to DataBase", font='Arial 17 bold', bg="white", fg="Green").grid(row=2, column=0, padx=300, columnspan=7, pady=40)

def new_op():
    root.destroy()
    import Adding_Bus_Operator_Detail

def new_bus():
    root.destroy()
    import add_bus_detail
    
def new_route():
    root.destroy()
    import Add_Bus_ROute_Details
    
def new_run():
    root.destroy()
    import Add_Bus_Running_Details
    

Button(root, text="New Operator",command=new_op, font='Arial 18 bold', fg='Black', bg="LightGreen").grid(row=3, column=1)
Button(root, text="New Bus", command=new_bus, font='Arial 18 bold',  fg='Black',bg="tomato").grid(row=3, column=2)
Button(root, text="New Route", command=new_route, font='Arial 18 bold', fg='Black',bg="DeepSkyBlue2").grid(row=3, column=3)
Button(root, text="New Run", command=new_run, font='Arial 18 bold', fg='Black',bg="PeachPuff4").grid(row=3, column=4)


# Button(root, text="New Route",font='Arial 10 bold', fg='Black').grid(row=3, column=3)
# Button(root, text="New Bus",font='Arial 10 bold', fg='Black').grid(row=3, column=3)

root.mainloop()