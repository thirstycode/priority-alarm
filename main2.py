from datetime import datetime as dt
import time
import shutdown
import popup
import sound_play


def alarm_loop(year,month,date,hour,minute,priority,text):
    now = dt(year,month,date,hour,minute)
    while True:
            ifl = dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute)
            ifr = dt(dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute + 1)
            if ifl <= now < ifr:
                if priority == 1:
                    popup.popup(text)
                if priority == 2:
                    sound_play.sound_play(text)
                if priority == 3:
                    shutdown.shutdown()
                time.sleep(60)
            else :
                time.sleep(60)
