from tkinter import *
from tkinter.messagebox import *

def main():
    import sqlite3
    con=sqlite3.connect('Database_211b140')
    cur=con.cursor()
    # import sqlite3
    # con=sqlite3.Connection('Database_211b140')
    # cur=con.cursor()
    root=Tk()
    root.geometry("1600x1600")
    img=PhotoImage(file=".\\Bus.png")
    Label(root,image=img).grid(row=0,column=0,padx=550,columnspan=12)
    Label(root,text="ONLINE BUS BOOKING SYSTEM",font="Ariel 27 bold",bg="light blue",fg="red").grid(row=1,column=0,columnspan=12)
    Label(root,text="Add Bus Operator Details",font="Ariel 19 ",bg="snow",fg="dark green").grid(row=2,column=0,pady=20,columnspan=12)


    Label(root,text="Operator id",font="Ariel 11").grid(row=3,column=0)
    Label(root,text="Name",font="Ariel 11").grid(row=3,column=2)
    Label(root,text="Address",font="Ariel 11").grid(row=3,column=4)
    Label(root,text="Phone",font="Ariel 11").grid(row=3,column=6)
    Label(root,text="Email",font="Ariel 11").grid(row=3,column=8)
    # Label(root,text="Email",font="Ariel 11").grid(row=3,column=8)


    idvar=IntVar()
    namevar=StringVar()
    addressvar=StringVar()
    contactvar=IntVar()
    emailvar=StringVar()

        

    identry=Entry(root, textvariable=idvar).grid(row=3,column=1)
    nameentry=Entry(root,textvariable=namevar).grid(row=3,column=3)
    addressentry=Entry(root,textvariable=addressvar).grid(row=3,column=5)
    contactentry=Entry(root,textvariable=contactvar).grid(row=3,column=7)
    emailentry=Entry(root, textvariable=emailvar).grid(row=3,column=9)

    
    def save_details():
        id1=idvar.get()
        name1=namevar.get()
        address1=addressvar.get()
        contact1=contactvar.get()
        email1=emailvar.get()
       
        if not id1:
            showerror('Error','Please fill in all the details.')
            
        if not name1:
            
            showerror('Error','Please fill in all the details.')
        if not address1:
            showerror('Error','Please fill in all the details.')
        if not contact1:
            showerror('Error','Please fill in all the details.')
        if not email1:
            showerror('Error','Please fill in all the details.')

        else:    
            cur.execute("""create table IF NOT EXISTS OPERATOR(id number ,name text , address text , contact number,  email text)""")
            if(cur.execute("INSERT INTO OPERATOR VALUES (?,?,?,?,?)",(id1, name1, address1, contact1, email1))):
                showinfo('Information', 'Details added.')

                con.commit()
        # cur.execute("INSERT INTO OPERATOR VALUES (?,?,?,?,?)",(id1, name1, address1, contact1, email1))
        # cur.execute("INSERT INTO OPERATOR VALUES (1, "k", "jhjhj", 8989, "yyuu");")

        # con.commit()
    # def fn():
    #     AddToOperatorDetails(op_id, op_name,op_address,op_phone,op_email)
    Button(root,text="Add",font="Ariel 11 bold", command=save_details,fg="black",bg="green2").grid(row=7,column=4,pady=25)
    Button(root,text="Edit",font="Ariel 11 bold",fg="black",bg="green2").grid(row=7,column=5,pady=25)
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2).grid(row=7,column=6,pady=30)

    root.mainloop()
main()