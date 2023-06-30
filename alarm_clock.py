from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock by Partha")
clock.geometry("400x200")
clock.configure(bg="black")     
time_format=Label(clock, text= "Note : Enter time in 24 hour format!!!", fg="red",bg="skyblue",font=("Arial",9,"bold"),borderwidth=3, relief="groove").place(x=100,y=160)
addTime = Label(clock,text = "Hour        Minutes     Seconds",font=60,bg="black",fg="Cyan").place(x = 120)
setYourAlarm = Label(clock,text = "Alarm Time : ",fg="Red",font=("Helevetica",10,"bold"),bg="Black").place(x=10, y=28)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15,fg="Blue").place(x=100,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15,fg="Blue").place(x=200,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15,fg="Blue").place(x=300,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =207,y=70)

clock.mainloop()