from tkinter import*
from tkinter.messagebox import *

def main():
    
    import sqlite3
    con=sqlite3.connect('Database_211b140')
    cur=con.cursor()
    root=Tk()
    w,h=root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    #img=PhotoImage(file="C:\\Users\\211b140\\Desktop\\Project\\Bus")
    img=PhotoImage(file=".\\Bus.png")
    Label(root, image=img).grid(row=0, column=0, padx=600, columnspan=7)
    Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=0, padx=100, columnspan=7)
    Label(root, text="Add Bus Running Details", font='Arial 16 bold', fg='Green').grid(row=2, column=0, padx=100, columnspan=7, pady=40)

    Label(root, text="Bus ID", font='Arial 10 bold').grid(row=3, column=1, sticky=E)
    Label(root, text="Running Date", font='Arial 10 bold').grid(row=3, column=2, sticky=E)
    Label(root, text="Seat Available", font='Arial 10 bold').grid(row=3, column=3, sticky=E)
    
    b_idvar=IntVar()
    running_datevar=StringVar()
    seat_availvar=IntVar()
    
    Entry(root, textvariable=b_idvar).grid(row=3, column=2, sticky=W)
    Entry(root, textvariable=running_datevar).grid(row=3, column=3, sticky=W)
    Entry(root, textvariable=seat_availvar).grid(row=3, column=4, sticky=W)
    
    # id1=b_idvar.get()
    # running_date=running_datevar.get()
    # seat_avail=seat_availvar.get()

    def save_details():
        
        id1=b_idvar.get()
        running_date=running_datevar.get()
        seat_avail=seat_availvar.get()
        
        if not id1: 
            showerror('Error','Please fill in all the details.')
        if not running_date: 
            showerror('Error','Please fill in all the details.')
        if not seat_avail: 
            showerror('Error','Please fill in all the details.')
        else:
            cur.execute("""create table IF NOT EXISTS runs(b_id number ,run_date text , seat_availability number)""")
            if cur.execute("INSERT INTO RUNS VALUES (?,?,?)",(id1, running_date, seat_avail)):
                
                showinfo('Information', 'Details saved successfully!')

                con.commit()
            
    def delete_details():
        # cur.execute('DELETE FROM RUNS WHERE b_id={}, run_date={}, seat_availability={}').format(id1, running_date, seat_avail)
        pass
        
    Button(root, text="Add Run",font='Arial 18 bold', command= save_details,fg='Black', bg="LightGreen").grid(row=3, column=3, padx=10, columnspan=4)
    Button(root, text="Delete Run",font='Arial 18 bold',command=delete_details, fg='Black', bg="LightGreen").grid(row=3, column=5)

    def back2home():
        
        root.destroy()
        import options_screen
    img2=PhotoImage(file=".\\Home.png")
    Button(root,image=img2,command=back2home).grid(row=3,column=6)
    # def fn():
        
    root.mainloop()
    
main()