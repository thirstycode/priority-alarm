# <--------https://github.com/thirstycode/priority-alarm------>
# <-------TODO---- good looking gui ------>
from tkinter import *
import time
from datetime import datetime as dt
import main2

# tkinter 
win = Tk()
win.title("Priority Alarm")

# required lists
OPTIONS_YEAR = [2018,2019,2020]
OPTIONS_MONTH = ["January","February","March","April","May","June","July","August","September","October","November","December"]
OPTIONS_DATE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
OPTIONS_HOUR = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
OPTIONS_MINUTE = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
priorities = [
    ("PopUp Window",1),
    ("SoundPlay Of Alarm",2),
    ("Shutdown Your Computer",3),
]


# required variables
output1 = StringVar()
variable_year = StringVar(win)
variable_year.set(dt.now().year)
variable_month = StringVar(win)
variable_month.set(OPTIONS_MONTH[dt.now().month-1])
variable_date = StringVar(win)
variable_date.set(dt.now().day)
variable_hour = StringVar(win)
variable_hour.set(dt.now().hour)
variable_minute = StringVar(win)
variable_minute.set(dt.now().minute)
variable_priority= IntVar()
variable_priority.set(2)
priorities = [
    ("PopUp Window",1),
    ("SoundPlay Of Alarm",2),
    ("Shutdown Your Computer",3),
]

def set_alarm():
    w2 = Label(win,text="Alarm Saved ! Now Close This Window !")
    # w2.pack()
    w2.grid(row=12,column=0,columnspan=2)


w = Label(win,text="To Set Your Alarm With Priority Tasks")
w.grid(row=0,column=0,columnspan=2)
w2 = Label(win,text="Year : ")
w2.grid(row=1,column=0)
d1 = OptionMenu(win,variable_year, *OPTIONS_YEAR)
d1.grid(row=1,column=1)
w3 = Label(win,text="Month : ")
w3.grid(row=2,column=0)
d2 = OptionMenu(win,variable_month, *OPTIONS_MONTH)
d2.grid(row=2,column=1)
w4 = Label(win,text="Date : ")
w4.grid(row=3,column=0)
d3 = OptionMenu(win,variable_date, *OPTIONS_DATE)
d3.grid(row=3,column=1)
w5 = Label(win,text="Hour : ")
w5.grid(row=4,column=0)
d4 = OptionMenu(win,variable_hour, *OPTIONS_HOUR)
d4.grid(row=4,column=1)
w6 = Label(win,text="Minute : ")
w6.grid(row=5,column=0)
d5 = OptionMenu(win,variable_minute, *OPTIONS_MINUTE)
d5.grid(row=5,column=1)
button = Button(win, text="Set Alarm", command=set_alarm)
button.grid(row=11,column=0,columnspan=2)

Label(win,
         text="""Choose Your Priority : """,
         justify = LEFT,
         padx = 20).grid(row=6,column=0,columnspan=2)
rowc=7
for val, priority in enumerate(priorities):
    Radiobutton(win,text=priority,padx = 20,variable=variable_priority,value=val+1).grid(row=rowc,column=0)
    rowc +=1

w7 = Label(win,text="Alarm Title : ")
w7.grid(row=10,column=0)
Input_box = Entry(win , textvariable = output1)
Input_box.grid(row=10,column=1)

win.mainloop()

main2.alarm_loop(int(variable_year.get()),int(OPTIONS_MONTH.index(variable_month.get()) +1),int(variable_date.get()),int(variable_hour.get()),int(variable_minute.get()),int(variable_priority.get()),output1.get())
