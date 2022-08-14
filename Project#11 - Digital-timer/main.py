from tkinter import*
import time
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time counter")

hour = StringVar()
minute = StringVar()
second = StringVar()
flag = StringVar()

hour.set("00")
minute.set("00")
second.set("00")
flag.set("1")
#use entry to get input from user

hour_user = Entry(root,width=3,font=("Arial",18,""),textvariable=hour)
hour_user.place(x=80,y=20) # Hr:MM:SS , ##:##:##
hour_label = Label(root,text="HH",font=("arial 18 bold"))
hour_label.place(x=80,y=50)
minute_user = Entry(root,width=3,font=("Arial",18,""),textvariable=minute)
minute_user.place(x=130,y=20) #+50 pixel to the left
minute_label = Label(root,text="MM",font=("arial 18 bold"))
minute_label.place(x=125,y=50)
second_user = Entry(root,width=3,font=("Arial",18,""),textvariable=second)
second_user.place(x=180,y=20) #+50 pixel to the left
second_label = Label(root,text="SS",font=("arial 18 bold"))
second_label.place(x=180,y=50)
#Create condition accect the input from user
def submit():
    try :
        #Convert to sec
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please Input the right value")
        temp = -1
    while temp >-1 : #check second from the user is not minus
        #display portion
        min_show,sec_show = divmod(temp,60) #output = min(//60) , sec (% 60)
        hour_show = 0 #create variable
        if min_show > 60:
            hour_show, min_show = divmod(min_show,60) # hour (//60 min) min (%min60)
        hour.set("{0:2d}".format(hour_show)) # add hour_show to hour with 2 digit
        minute.set("{0:2d}".format(min_show))
        second.set("{0:2d}".format(sec_show))

        
        #Time out message box
        if(temp == 0):
            messagebox.showinfo("Time Countdown","Time's up")
        # update every thing every 1 sec (use sleep function)
        root.update()
        time.sleep(1)
        temp -=1
        

# Button for submit / start
btn = Button(root,text= "Set Timer", bd="5",command= submit) 
#press button make it run on fucntion submit
#locate btn
btn.place(x=125,y=150)
'''
btn_pause = Button(root,text="Pause",bd="5",command= flag.set("0"))
btn_pause.place(x=100,y=180)
btn_resume = Button(root,text="Resume",bd="5",command= flag.set("1"))
btn_resume.place(x=150,y=180)
'''

# run = 1 (run) , = 0 pause
# stop = clear


root.mainloop()

