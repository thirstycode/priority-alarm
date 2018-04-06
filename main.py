# <--------https://github.com/thirstycode/priority-alarm------>
# <--------alarm working from terminal ------ added gui in main_gui.py file---->

# import nececssary modules
from datetime import datetime as dt
# from support.dateget import (date,month,year,hour,minute)
import time

from support import shutdown
from support import popup
from support import sound_play

# inputs of all required things
# <---note ----- no conditional applied for wrong date ------ TODO----->
year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
date = int(input("Enter Date : "))
hour = int(input("Enter Hour : "))
minute = int(input("Enter Minute : "))
priority = input("Enter priority \n '1' for popup alert \n '2' for sound play \n '3' for shutdown \n Enter : ")
priority = int(priority)


now = dt(year,month,date,hour,minute)
popuptext = "Alarm description"
soundtext = "Sound Text"
# if priority == 1 :
#     popuptext = input("Text To Be Inserted In Popup : ")
# if priority == 2 :
#     soundtext = input("Text To Be Inserted In Popup : ")
# if priority == 3 :
#     shutdown
while True:
        ifl = dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute)
        ifr = dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute + 1)
        if ifl <= now < ifr:
            if priority == 1:
                popup.popup(popuptext)
            if priority == 2:
                sound_play.sound_play(soundtext)
            if priority == 3:
                shutdown.shutdown()
            time.sleep(60)
        else :
            time.sleep(60)
