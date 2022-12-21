from tkinter import*
from tkinter.messagebox import*


def main():
    import sqlite3
    con=sqlite3.connect('Database_211b140')
    cur=con.cursor()
    root=Tk()
    w,h=root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    # img=PhotoImage(file="C:\\Users\\211b140\\Desktop\\Project\\Bus")
    img=PhotoImage(file=".\\Bus.png")


    Label(root, image=img).grid(row=0, column=0, padx=600, columnspan=7)
    Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=0, padx=100, columnspan=7)
    Label(root, text="Add Bus Route Details", font='Arial 16 bold', fg='Green').grid(row=2, column=0, padx=100, columnspan=7, pady=40)

    Label(root, text="Route ID", font='Arial 10 bold').grid(row=3, column=1, sticky=E)
    Label(root, text="Station Name", font='Arial 10 bold').grid(row=3, column=2, sticky=E)
    Label(root, text="Station ID", font='Arial 10 bold').grid(row=3, column=3, sticky=E)
    
    r_idvar=IntVar()
    st_namevar=StringVar()
    st_idvar=IntVar()
    
    Entry(root, textvariable=r_idvar).grid(row=3, column=2, sticky=W)
    Entry(root, textvariable=st_namevar).grid(row=3, column=3, sticky=W)
    Entry(root, textvariable=st_idvar).grid(row=3, column=4, sticky=W)
    
    # r_id1=r_idvar.get()
    # st_name1=st_namevar.get()
    # st_id1=st_idvar.get()
        
    def save_details():
        r_id1=r_idvar.get()
        st_name1=st_namevar.get()
        st_id1=st_idvar.get()
        
        cur.execute("""create table IF NOT EXISTS ROUTE_DETAILS(r_id number , st_name text, st_id number )""")
        if(cur.execute("INSERT INTO ROUTE_DETAILS(r_id,st_name, st_id) VALUES (?,?,?)",(r_id1, st_name1, st_id1))):
            showinfo('Information', 'Details added.')
            con.commit()
        
    def delete_details():
        # if not r_id1:
            
            
        # cur.execute('DELETE FROM ROUTE_DETAILS WHERE r_id=%s', data=[r_id1])
        # con.commit()
        pass

    Button(root, text="Add Route",font='Arial 18 bold', command=save_details,fg='Black', bg="LightGreen").grid(row=3, column=3, padx=10, columnspan=4)
    Button(root, text="Delete Route",font='Arial 18 bold',command=delete_details, fg='red', bg="LightGreen").grid(row=3, column=5)
    def back2home():
        
        root.destroy()
        import options_screen
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2,command=back2home).grid(row=3,column=6)

    root.mainloop()
    
main()