from tkinter import*

import calendar

def showCal():
    ng = Tk()
    ng.config(background= "white")
    ng.geometry("1000x1200")
    year = int(box_year.get())
    cal_content = calendar.calendar(year)
    #print(cal_content)
    #label for show calendar content
    cal = Label(ng,text = cal_content,font="Consolas 10 bold")
    ng.title("CALENDAR " + str(year))
    cal.grid(row = 10,column = 1, padx = 50)
    ng.mainloop()


#create the root
if __name__ == "__main__" :
    root = Tk()
    root.title("CALENDAR")
    root.config(background= "white")
    root.geometry("160x140")
    lb1 = Label(root,text= "Calender", bg= "dark gray",font=("times",28 , "bold"))
    lb2 = Label(root,text= "Enter year",bg="light green",font="times")
    box_year = Entry(root)
    bn1 = Button(root,text= "Show Calendar",fg="black",bg= "red",command= showCal) 
    # send command to show cal need def function show cal
    bn2 = Button(root,text= "Exit",fg= "black",bg= "red",command= exit)
    # grid placing item
    lb1.grid(row=1,column=1)
    lb2.grid(row=2,column=1)
    box_year.grid(row=3,column=1)
    bn1.grid(row=4,column=1)
    bn2.grid(row=5,column=1)

    root.mainloop()
