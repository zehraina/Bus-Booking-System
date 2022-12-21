from tkinter import*
from tkinter.messagebox import *
root=Tk()
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

img=PhotoImage(file=".\\Bus.png")


Label(root, image=img).grid(row=0, column=0, padx=600, columnspan=13)

Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg="light blue", fg='red').grid(row=1, column=6,columnspan=3)
Label(root, text="Name: Ina Zehra", font='Arial 18 bold', fg='navy').grid(row=4, column=7,pady=40)
Label(root, text="En. No: 211B140", font='Arial 18 bold',  fg='navy').grid(row=6, column=7,pady=40)
Label(root, text="Mobile: +91 7007445234", font='Arial 18 bold', fg='navy').grid(row=8, column=7,pady=40)

Label(root, text="Submitted to: Dr. Mahesh Kumar", font='Arial 30 bold', bg="light blue", fg='red').grid(row=9, column=7,pady=50)


Label(root, text="Project based learning", font='Arial 18 bold', fg='red').grid(row=10, column=7)

def close():
    root.destroy()
    import options_screen
root.after(4500, close)
showinfo('Greet', 'Welcome!')
root.mainloop()