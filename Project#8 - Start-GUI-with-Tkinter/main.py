#import module
from tkinter import *
# creat root window
root = Tk()
# assign title and window dimension
root.title("Welcome to Tkinter")
root.geometry("350x200")
#menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File",menu=item)
root.config(menu= menu)

# add the label
lb = Label(root, text= "Are you newbie of Tkinker?")
lb.grid() # 0,0 coordinate
# add entry field
txt = Entry(root , width= 10)
txt.grid(column= 1 ,row= 0)
def clicked():
    res = "You wrote " + txt.get()
    lb.configure(text= res)

btn = Button(root, text= "Click me", fg= "red", command= clicked)
#set the button
btn.grid(column= 2, row= 0)
#excute the root
root.mainloop()
# run and you will get the window that time title and dimension as you assigned 