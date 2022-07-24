import configparser
from datetime import datetime,timedelta
import tkinter as tk
import customtkinter as ctk

design = configparser.ConfigParser()
design.read("design.ini")

background=design.get("COLOR", "background")
foreground=design.get("COLOR", "foreground")
accent=design.get("COLOR", "accent")
textcolor=design.get("COLOR", "textcolor")
fontType=design.get("FONT", "fontFamily")
buttonColor=design.get("BUTTON", "buttonColor")

class StintInfo:
    racelength_h = 0
    racelength_m = 2
    laptime = 10
    fueltank = 50
    fuelcons = 10
    refueltime = 5
    tyrechangetime = 2
    dttime = 3
    stintpertyre = 1
    refuellitertime = 0
    fuelleft = 0
    tyrestint = 0
    racelength = 0
    timeleft = 0
    stinttime = 0
    lapcount = 0
    stintcount = 0

info = StintInfo
lasttime = 0
timeChange = timedelta(seconds=info.laptime)

def liveInitFunc():
    global lastTime 
    lastTime = datetime.now()
    lastTime = lastTime.replace(microsecond=0)
    print(lastTime)

    lmWindow = tk.Tk()

    info.refuellitertime=int((info.refueltime/info.fueltank)*100)/100
    info.fuelleft = info.fueltank
    info.tyrestint = info.stintpertyre
    racelength = info.racelength_h*3600 + info.racelength_m*60
    info.timeleft = racelength   
    info.stinttime = int(info.fueltank/info.fuelcons) * info.laptime + info.dttime + info.refueltime + info.tyrechangetime

    def curentTime():
        time = datetime.now()
        time = time.replace(microsecond=0)
        return time

    def verifyTime():
        global lastTime,timeChange
        if curentTime() == lastTime+timeChange:
            lastTime += timeChange
            print(curentTime())
            return (1)
        else:
            return (2) 

    def liveLastStintFunc():
        rasp = verifyTime()
        if rasp == 1:
            if info.timeleft>info.laptime:
                info.fuelleft -= info.fuelcons
                info.timeleft -= info.laptime
                info.lapcount += 1
                conversion = str(timedelta(seconds=info.timeleft))
                if len(conversion) > 9:
                    conversion=conversion[:-4]
                textoutput="Lap : "+str(info.lapcount)+"| Time left :"+str(conversion)+"| Fuel left : "+str(round(info.fuelleft, 2))
                print(textoutput)       
                lmWindow.after(1000,lambda: liveLastStintFunc())
            else:
                info.fuelleft -= info.fuelcons
                info.timeleft -= info.laptime
                info.lapcount += 1
                textoutput="Lap : "+str(info.lapcount)+"| Fuel left : "+str(round(info.fuelleft, 2))+"| Race Finished!"
                print(textoutput)
        else:
            lmWindow.after(1000,liveLastStintFunc)

    def liveLapFunc():
        rasp = verifyTime()
        if rasp == 1:
            print("")
            if info.fuelleft>=info.fuelcons*2 :
                info.fuelleft -= info.fuelcons
                info.timeleft -= info.laptime
                info.timeleft = int(info.timeleft*100)/100
                info.lapcount += 1
                conversion = str(timedelta(seconds=info.timeleft))
                if len(conversion)>8:
                    conversion = conversion[:-5]
                textoutput = "Lap : "+str(info.lapcount)+" | Time left : "+str(conversion)+" | Fuel left : "+str(round(info.fuelleft, 2))
                print(textoutput)
                lmWindow.after(1000,liveLapFunc())
            else:
                info.fuelleft -= info.fuelcons
                info.timeleft -= info.laptime
                info.timeleft -= info.dttime
                info.timeleft -= info.refueltime
                info.lapcount += 1

                if info.tyrestint<2:
                    info.tyrestint = info.stintpertyre
                    info.timeleft -= info.tyrechangetime
                elif info.tyrestint>1:
                    info.tyrestint -= 1
                
                conversion = str(timedelta(seconds=info.timeleft))
                if len(conversion)>8:
                    conversion = conversion[:-5]
                textoutput="PIT THIS LAP | Lap : " +str(info.lapcount)+" | Time left : "+str(conversion)+" | Fuel wasted : "+str(round(info.fuelleft, 2))
                print(textoutput)
                info.fuelleft = info.fueltank
                lmWindow.after(1000,liveStintFunc)
        else:
            lmWindow.after(1000,liveLapFunc)

    def liveStintFunc():
        
        if info.timeleft>info.stinttime :
            info.stintcount += 1
            textoutput="\n\nStint #"+str(info.stintcount)
            print(textoutput)
            liveLapFunc()
        else:
            lapsleft = int(info.timeleft/info.laptime)+1
            info.fuelleft = info.fuelcons * lapsleft
            info.timeleft = info.timeleft - int(info.refuellitertime*info.fuelleft) - info.dttime
            info.stintcount += 1
            textoutput="\nStint #"+str(info.stintcount)
            liveLastStintFunc()

    liveStintFunc()
    lmWindow.mainloop()

liveInitFunc()

