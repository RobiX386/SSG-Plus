import tkinter as tk
import configparser
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

events = configparser.ConfigParser()
events.read("eventsfile.ini")

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

space= ' '
curentpath = os.getcwd() + "\presets"+"\\"



def waitFunc(eventFile):
    from livemode import livemodeFunc

    event = configparser.ConfigParser()
    event.read(eventFile)

    driverList = event.options("DRIVERS")

    event = configparser.ConfigParser()
    event.read(eventFile)
    startingDriver = event.get("EVENTINFO", "startingdriver")

    waitRoom = tk.Tk()
    waitRoom.geometry("+300+100")
    waitRoom.title("SSG+ Event Countdown")
    waitRoom.resizable(False, False)
    waitRoom.config(bg=background)
    
    def changeTime():
        timeWindow = tk.Toplevel(waitRoom)
        timeWindow.geometry("+300+100")
        timeWindow.title("SSG+ Change Event Time")
        timeWindow.resizable(False, False)
        timeWindow.config(bg=background)

        # changeTime = ckt.CTkLabel(timeWindow, time )

    waitRoomLabel = ctk.CTkLabel(waitRoom, text="Time until event starts", text_font=(fontType, 20), text_color=textcolor, fg_color=background)
    waitRoomLabel.pack(expand=True, pady=30)

    countdownWrap = ctk.CTkFrame(waitRoom, border_color=accent, fg_color=background, border_width=borderWidth, corner_radius=cornerRadius)
    countdownWrap.pack(expand=True, padx=50)

    countDownLabel = ctk.CTkLabel(countdownWrap, text="Time until event starts: ", text_color=textcolor, text_font=(fontType, 30), fg_color=background)
    countDownLabel.pack(expand=True, padx=20, pady=10)

    countDown = ctk.CTkLabel(countdownWrap, text="7:25:22", text_font=(fontType, 40), fg_color=background, text_color=textcolor)
    countDown.pack(expand=True, padx=20, pady=10)

    def changeStartingDriver():
        changeWindow = tk.Toplevel(waitRoom)
        changeWindow.config(bg=background)
        changeWindow.geometry("+300+100")
        changeWindow.title("SSG+ Starting Driver")
        changeWindow.resizable(False, False)

        selectStartingDriver = ctk.CTkLabel(changeWindow, fg_color=background, text_color=mainTextColor, text_font=(fontType, 18), text="Select Starting Driver")
        selectStartingDriver.pack(pady=20)

        selectDriverWrap = ctk.CTkFrame(changeWindow, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
        selectDriverWrap.pack(pady=10)

        def writeData(x):
            event.set("EVENTINFO", "startingdriver", x)
            
            with open(eventFile, "w") as config_file:
                event.write(config_file)
            changeWindow.destroy()

        for x in driverList:
            driver = ctk.CTkButton(selectDriverWrap, fg_color=buttonColor, text_color=textcolor, text=x, corner_radius=buttonRadius, command=lambda:writeData(x))
            driver.pack(padx=10, pady=7)

    startingDriverText = "Starting Driver:\n" + startingDriver

    startingDriverLabel = ctk.CTkLabel(waitRoom, text=startingDriverText, fg_color=background, text_color=textcolor, text_font=(fontType, 14))
    startingDriverLabel.pack(expand=True, pady=10)

    # buttonWrap = ctk.CTkFrame(waitRoom, fg_color=background)
    # buttonWrap.pack(pady=(10, 20))

    swapDriver = ctk.CTkButton(waitRoom, text="Swap Driver", width=100, height=60, fg_color=buttonColor, text_color=textcolor, text_font=(fontType, 13), hover_color=hoverColor, command=changeStartingDriver)
    swapDriver.pack(padx=10, side=tk.LEFT)

    # delayButton = ctk.CTkButton(buttonWrap, text="Change \n Start Time", text_color=textcolor, text_font=(fontType, 13), width=100, height=60, hover_color=hoverColor, fg_color=buttonColor)
    # delayButton.pack(padx=10, side=tk.LEFT)