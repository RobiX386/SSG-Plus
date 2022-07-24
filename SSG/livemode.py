import tkinter as tk
import configparser
from datetime import datetime,timedelta
import webbrowser
import os
import customtkinter as ctk
from errorFile import error
import sys

class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()
#Supressing known exceptions
#colors&&fonts

design = configparser.ConfigParser()
design.read("design.ini")

background=design.get("COLOR", "background")
foreground=design.get("COLOR", "foreground")
accent=design.get("COLOR", "accent")
textcolor=design.get("COLOR", "textcolor")
mainTextColor=design.get("COLOR", "maincolor")
fontType=design.get("FONT", "fontFamily")
borderWidth=int(design.get("BORDER", "borderWidth"))
cornerRadius=int(design.get("BORDER", "cornerRadius"))
buttonColor=design.get("BUTTON", "buttonColor")
buttonRadius=int(design.get("BUTTON", "cornerRadius"))
hoverColor=design.get("BUTTON", "hoverColor")
entryBorderColor=design.get("ENTRY", "borderColor")
entryFg=design.get("ENTRY", "foreground")
placeholderColor=design.get("ENTRY", "placeholderColor")
entryTextColor=design.get("ENTRY", "textcolor")
navbarColor=design.get("NAVBAR", "navbarColor")
navButtonColor=design.get("NAVBAR", "navButtons")
navDisabledColor=design.get("NAVBAR", "navDisabled")

class StintInfo:
    racelength_h = 2
    racelength_m = 0
    laptime = 5
    fueltank = 75
    fuelcons = 5
    refueltime = 10
    tyrechangetime = 10
    dttime = 20
    stintpertyre = 2
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

space= ' '
curentpath = os.getcwd() + "\presets"+"\\"

def livemodeWait():
    waitRoom = tk.Tk()
    waitRoom.geometry("+300+100")
    waitRoom.title("SSG+ Event Countdown")
    waitRoom.resizable(False, False)
    waitRoom.config(bg=background)
    
    waitRoomLabel = ctk.CTkLabel(waitRoom, text="Time until event starts", text_font=(fontType, 20), text_color=textcolor, fg_color=background)
    waitRoomLabel.pack(expand=True, pady=30)

    countdownWrap = ctk.CTkFrame(waitRoom, border_color=accent, fg_color=background, border_width=borderWidth, corner_radius=cornerRadius)
    countdownWrap.pack(expand=True, padx=50)

    countDownLabel = ctk.CTkLabel(countdownWrap, text="Time until event starts: ", text_color=textcolor, text_font=(fontType, 30), fg_color=background)
    countDownLabel.pack(expand=True, padx=20, pady=10)

    countDown = ctk.CTkLabel(countdownWrap, text="7:25:22", text_font=(fontType, 40), fg_color=background, text_color=textcolor)
    countDown.pack(expand=True, padx=20, pady=10)

    startingDriverText = "Starting Driver:\n" + "Max Verstappen"

    startingDriverLabel = ctk.CTkLabel(waitRoom, text=startingDriverText, fg_color=background, text_color=textcolor, text_font=(fontType, 13))
    startingDriverLabel.pack(expand=True, pady=10)

    swapDriver = ctk.CTkButton(waitRoom, text="Swap Driver", width=100, height=40, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 13), hover_color=hoverColor)
    swapDriver.pack(expand=True, pady=(10, 20))

    

def livemodeFunc():
    from endurance import enduranceFunc
    from sprint import sprintFunc


    liveWindow = tk.Tk()
    liveWindow.config(bg=background)
    liveWindow.title("SSG+ Live")
    liveWindow.geometry("+300+100")
    liveWindow.resizable(False, False)

    def liveInitFunc():
        global lastTime 
        lastTime = datetime.now()
        lastTime = lastTime.replace(microsecond=0)
        print(lastTime)


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
                    outputList.insert(tk.END,textoutput)       
                    liveWindow.after(1000,lambda: liveLastStintFunc())
                else:
                    info.fuelleft -= info.fuelcons
                    info.timeleft -= info.laptime
                    info.lapcount += 1
                    textoutput="Lap : "+str(info.lapcount)+"| Fuel left : "+str(round(info.fuelleft, 2))+"| Race Finished!"
                    outputList.insert(tk.END,textoutput)
            else:
                liveWindow.after(1000,liveLastStintFunc)

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
                    outputList.insert(tk.END,textoutput)
                    liveWindow.after(1000,liveLapFunc())
                else:
                    info.fuelleft -= info.fuelcons
                    info.timeleft -= info.laptime
                    info.lapcount += 1

                    if info.tyrestint==1:
                        info.tyrestint = info.stintpertyre
                        info.timeleft -= info.tyrechangetime
                    elif info.tyrestint>1:
                        info.tyrestint -= 1

                    textoutput="PIT THIS LAP | Lap : " +str(info.lapcount)+" | Time left : "+str(conversion)+" | Fuel wasted : "+str(round(info.fuelleft, 2))
                    outputList.insert(tk.END,textoutput)
                    info.fuelleft = info.fueltank
                    liveWindow.after(1000,liveStintFunc)
            else:
                liveWindow.after(1000,liveLapFunc)

        def liveStintFunc():
            
            if info.timeleft>info.stinttime :
                info.stintcount += 1
                textoutput="\n\nStint #"+str(info.stintcount)
                outputList.insert(tk.END,textoutput)
                liveLapFunc()
            else:
                lapsleft = int(info.timeleft/info.laptime)+1
                info.fuelleft = info.fuelcons * lapsleft
                info.timeleft = info.timeleft - int(info.refuellitertime*info.fuelleft) - info.dttime
                info.stintcount += 1
                textoutput="\nStint #"+str(info.stintcount)
                liveLastStintFunc()
        print("start")
        liveStintFunc()


    navBar = ctk.CTkFrame(liveWindow, width=600, height=50, fg_color=navbarColor, corner_radius=0)
    navBar.pack(side=tk.TOP, fill=tk.X)

    buttonWrap = ctk.CTkFrame(navBar, fg_color=navbarColor, width=360)
    buttonWrap.pack(expand=True, pady=(0, 2))

    sprintButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Sprint", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[sprintFunc(), liveWindow.destroy()])
    sprintButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    enduranceButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Endurance", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[enduranceFunc(), liveWindow.destroy()])
    enduranceButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    liveButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Live", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, state=tk.DISABLED, command=lambda:[livemodeFunc(), liveWindow.destroy()])
    liveButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    dataWrap = ctk.CTkFrame(liveWindow, fg_color=background)
    dataWrap.pack(side=tk.LEFT, padx=15, pady=20)

    timeBox = ctk.CTkFrame(dataWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    timeBox.pack(side=tk.TOP, pady=(0, 15))

    timeLeft = ctk.CTkLabel(timeBox, text="Time Left:",  text_color=mainTextColor, text_font=(fontType, 18))
    timeLeft.pack(side=tk.TOP, padx=10, pady=(10, 5), expand=True)

    timeValue = ctk.CTkLabel(timeBox, text="6:24:25", text_color=mainTextColor, text_font=(fontType, 16))
    timeValue.pack(side=tk.TOP, padx=10, pady=(0, 5), expand=True)

    buttonBox = ctk.CTkFrame(dataWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    buttonBox.pack(side=tk.TOP, pady=15)

    changeData = ctk.CTkButton(buttonBox, width=80, height=30, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 14), text="Change Data", hover_color=hoverColor)
    changeData.pack(expand=True, pady=(20, 10), padx=20)

    scvsc = ctk.CTkButton(buttonBox, width=80, height=30, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 14), text="SC/VSC", hover_color=hoverColor)
    scvsc.pack(expand=True, pady=(10, 20), padx=20)

    infoBox = ctk.CTkFrame(dataWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    infoBox.pack(side=tk.TOP, pady=15)

    lapsLeftWrap = ctk.CTkFrame(infoBox, fg_color=background)
    lapsLeftWrap.pack(pady=7, padx=2)

    lapsLeft = ctk.CTkLabel(lapsLeftWrap, text="Laps left \n in stint", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    lapsLeft.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(lapsLeftWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(lapsLeftWrap, text="13", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    stopsLeftWrap = ctk.CTkFrame(infoBox, fg_color=background)
    stopsLeftWrap.pack(pady=7, padx=2)

    stopsLeft = ctk.CTkLabel(stopsLeftWrap, text="Stops Left", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    stopsLeft.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(stopsLeftWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(stopsLeftWrap, text="3", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    lastStintWrap = ctk.CTkFrame(infoBox, fg_color=background)
    lastStintWrap.pack(pady=7, padx=2)

    lapsInLastStint = ctk.CTkLabel(lastStintWrap, text="Laps in \n last stint", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    lapsInLastStint.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(lastStintWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(lastStintWrap, text="3", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    outBox = ctk.CTkFrame(liveWindow, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    outBox.pack(side=tk.LEFT, pady=0, padx=(20, 15))

    outputScroll = tk.Scrollbar(outBox, width=10)
    outputScroll.pack(side=tk.RIGHT, fill=tk.Y, padx=4, pady=4)

    outputList = tk.Listbox(outBox, yscrollcommand=outputScroll.set, bg=background, fg=textcolor, bd=0,height=25, width=52, highlightbackground=background,selectbackground=foreground)
    #aici scrii datele pentru live mode
    outputList.pack(pady=4, padx=4)

    dataWrap = ctk.CTkFrame(liveWindow, fg_color=background)
    dataWrap.pack(side=tk.LEFT, padx=15, pady=20)

    timeBox = ctk.CTkFrame(dataWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    timeBox.pack(side=tk.TOP, pady=(0, 15))

    timeLeft = ctk.CTkLabel(timeBox, text="Time Left:",  text_color=mainTextColor, text_font=(fontType, 18))
    timeLeft.pack(side=tk.TOP, padx=10, pady=(10, 5), expand=True)

    timeValue = ctk.CTkLabel(timeBox, text="6:24:25", text_color=mainTextColor, text_font=(fontType, 16))
    timeValue.pack(side=tk.TOP, padx=10, pady=(0, 5), expand=True)

    buttonBox = ctk.CTkFrame(dataWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    buttonBox.pack(side=tk.TOP, pady=15)

    changeData = ctk.CTkButton(buttonBox, width=80, height=30, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 14), text="Change Data", hover_color=hoverColor)
    changeData.pack(expand=True, pady=(20, 10), padx=20)

    scvsc = ctk.CTkButton(buttonBox, width=80, height=30, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 14), text="SC/VSC", hover_color=hoverColor)
    scvsc.pack(expand=True, pady=(10, 20), padx=20)

    infoBox = ctk.CTkFrame(dataWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    infoBox.pack(side=tk.TOP, pady=15)

    lapsLeftWrap = ctk.CTkFrame(infoBox, fg_color=background)
    lapsLeftWrap.pack(pady=7, padx=2)

    lapsLeft = ctk.CTkLabel(lapsLeftWrap, text="Laps left \n in stint", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    lapsLeft.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(lapsLeftWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(lapsLeftWrap, text="13", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    stopsLeftWrap = ctk.CTkFrame(infoBox, fg_color=background)
    stopsLeftWrap.pack(pady=7, padx=2)

    stopsLeft = ctk.CTkLabel(stopsLeftWrap, text="Stops Left", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    stopsLeft.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(stopsLeftWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(stopsLeftWrap, text="3", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    lastStintWrap = ctk.CTkFrame(infoBox, fg_color=background)
    lastStintWrap.pack(pady=7, padx=2)

    lapsInLastStint = ctk.CTkLabel(lastStintWrap, text="Laps in \n last stint", text_font=(fontType, 14), fg_color=background, width=0, text_color=mainTextColor)
    lapsInLastStint.pack(side=tk.LEFT, expand=True)

    colon = ctk.CTkLabel(lastStintWrap, text=":", text_font=(fontType, 18), fg_color=background, width=0, text_color=mainTextColor)
    colon.pack(side=tk.LEFT, expand=True)

    number = ctk.CTkLabel(lastStintWrap, text="3", text_font=(fontType, 16), fg_color=background, width=0, text_color=mainTextColor)
    number.pack(side=tk.LEFT, expand=True)

    startStop = ctk.CTkButton(dataWrap, fg_color=buttonColor, text="Start/Stop \n event", text_color=textcolor, corner_radius=buttonRadius, height=60, text_font=(fontType, 16),command=liveInitFunc)
    startStop.pack(side=tk.TOP, pady=(15, 0))