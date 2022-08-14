from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox #Library module of easy message box

from time import strftime

root = Tk()
root.title("Digtal Clock")

def time():
    time_clock = strftime("%H:%M:%S %p") #Hour : Minute : Second AM/PM
    lb.config(text = time_clock)
    lb.after(1000, time) # update time every 1000ms = 1 sec

#locate the clock
lb = Label(root,font = "arial 40 bold",background= "Black",foreground= "white")
lb.pack(anchor = "center")
time()
#need to def function time() for getting the time and place it on the label

root.mainloop()
