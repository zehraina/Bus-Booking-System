from tkinter import *
from tkinter.messagebox import *

def main():
    import sqlite3
    con=sqlite3.connect('Database_211b140')
    cur=con.cursor()
    root=Tk()
    root.geometry("1600x1600")
    img=PhotoImage(file=".\\Bus.png")

    Label(root,image=img).grid(row=0,column=0,padx=550,columnspan=12)
    Label(root,text="ONLINE BUS BOOKING SYSTEM",font="Ariel 27 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=12)
    Label(root,text="Add Bus Details",font="Ariel 19 ", bg="snow",fg="dark green").grid(row=2,column=0,pady=20,columnspan=12)
    
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
    # img2=PhotoImage(file=".\\Home.png")
    # Button(root,image=img2).grid(row=7,column=7,pady=30)
    def back2home():
        root.destroy()
        import options_screen
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2,command=back2home).grid(row=7,column=7)
    
    root.mainloop()
    
main()
