import tkinter as tk
import configparser
import datetime
from turtle import width
import webbrowser
import os
import customtkinter as ctk
from errorFile import error
import sys
from tkinter import N, ttk


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
buttonLightColor=design.get("BUTTON", "lightColor")
entryBorderColor=design.get("ENTRY", "borderColor")
entryFg=design.get("ENTRY", "foreground")
placeholderColor=design.get("ENTRY", "placeholderColor")
entryTextColor=design.get("ENTRY", "textcolor")
navbarColor=design.get("NAVBAR", "navbarColor")
navButtonColor=design.get("NAVBAR", "navButtons")
navDisabledColor=design.get("NAVBAR", "navDisabled")

eventnumber=1
space= ' '
curentpath = os.getcwd() + "/presets"+"//"
eventpath = os.getcwd() + "/events"+"//"

def eventsFunc():
    from sprint import sprintFunc
    from livemode import livemodeFunc
    from endurance import enduranceFunc

    eventsWindow = tk.Tk()
    eventsWindow.title("SSG+ Select Events")
    eventsWindow.attributes("-topmost", "true")
    eventsWindow.config(bg=background)
    eventsWindow.resizable(False, False)
    eventsWindow.geometry("760x700")

    def update():
        global eventnumber
        eventlistread = configparser.ConfigParser()
        eventfilename = eventpath + "events.ini"
        eventlistread.read(eventfilename)
        filename = eventpath+eventlistread.get("EVENTS",str(eventnumber)) +".ini"
        eventread = configparser.ConfigParser()
        eventread.read(filename)

        readname = eventread.get("NAME","name")
        if len(readname)>12:

            readnamelist = readname.split()
            listlength = len(readnamelist)/2
            readnamelist.insert(listlength,"\n")
            print(1)
            eventNameLabel.configure(text="test")



    navBar = ctk.CTkFrame(eventsWindow, width=600, height=50, fg_color=navbarColor, corner_radius=0)
    navBar.pack(side=tk.TOP, fill=tk.X)

    buttonWrap = ctk.CTkFrame(navBar, fg_color=navbarColor, width=360)
    buttonWrap.pack(expand=False, pady=(0, 2))

    sprintButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Sprint", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[sprintFunc(), eventsWindow.destroy()])
    sprintButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    enduranceButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Endurance", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[enduranceFunc(), eventsWindow.destroy()])
    enduranceButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    liveButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Live", fg_color=navDisabledColor, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), state=tk.DISABLED, corner_radius=buttonRadius, command=lambda:[livemodeFunc(), eventsWindow.destroy()])
    liveButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    eventsWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    eventsWrap.pack(side=tk.LEFT, pady=20, padx=7, fill=tk.Y)

    eventsBox = ctk.CTkFrame(eventsWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    eventsBox.pack(fill=tk.Y, padx=10, pady=(15, 0), expand=True)

    for i in range (0, 6):
        event = ctk.CTkButton(eventsBox, text=("buton" + str(i)), fg_color=buttonLightColor, corner_radius=0, width=240, height=60, hover_color=hoverColor, text_font=(fontType, 15), text_color="white", command=update)
        if i == 0: 
            event.pack(pady=(20, 7), padx=15)
            continue
        event.pack(padx=15, pady=7)

    eventList = ctk.CTkLabel(eventsWrap, text="EVENTS LIST", width=0, text_color=accent, text_font=(fontType, 15), fg_color=background)
    eventList.place(x=149, y=0, anchor=N)

    eventsButtonWrap = ctk.CTkFrame(eventsWrap, fg_color=background)
    eventsButtonWrap.pack(side=tk.TOP, pady=(10, 0))

    topWrap = ctk.CTkFrame(eventsButtonWrap, fg_color=background)
    topWrap.pack()

    createEvent = ctk.CTkButton(topWrap, fg_color=accent, text_color=background, width=110, height=50, text="Create\nevent", text_font=(fontType, 15), hover_color=navDisabledColor, corner_radius=buttonRadius)
    createEvent.pack(side=tk.LEFT, padx=10, pady=(10, 0))

    loadEvent = ctk.CTkButton(topWrap, fg_color=accent, text_color=background, width=110, height=50, text="Load\nevent", text_font=(fontType, 15), hover_color=navDisabledColor, corner_radius=buttonRadius)
    loadEvent.pack(side=tk.LEFT, padx=10, pady=(10, 0))

    bottomWrap = ctk.CTkFrame(eventsButtonWrap, fg_color=background)
    bottomWrap.pack()

    startEvent = ctk.CTkButton(bottomWrap, text="Start\nEvent", fg_color=accent, text_color=background, text_font=(fontType, 15), width=110, height=50, hover_color=navDisabledColor, corner_radius=buttonRadius)
    startEvent.pack(side=tk.LEFT, padx=10, pady=(10, 0))

    settings = ctk.CTkButton(bottomWrap, text="More\nSettings", fg_color=accent, text_color=background, text_font=(fontType, 15), width=110, height=50, hover_color=navDisabledColor, corner_radius=buttonRadius)
    settings.pack(side=tk.LEFT, padx=10, pady=(10, 0))

    reWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    reWrap.pack(side=tk.LEFT, expand=True, fill=tk.Y)
    
    eventNameWrap = ctk.CTkFrame(reWrap, fg_color=background)
    eventNameWrap.pack(pady=(19, 20))

    eventNameBox = ctk.CTkFrame(eventNameWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    eventNameBox.pack(pady=(15, 0))

    eventName = ctk.CTkLabel(eventNameWrap, fg_color=background, text="EVENT NAME", width=0, text_font=(fontType, 15), text_color=accent)
    eventName.place(x=100, y=0, anchor=N)

    eventNameLabel = tk.Label(eventNameBox, text="24h of \n LeMans S15", bg=background)
    eventNameLabel.pack(padx=30, pady=20)

    raceDataWrap = ctk.CTkFrame(reWrap, fg_color=background)
    raceDataWrap.pack(padx=0, pady=(0, 21), expand=True, fill=tk.Y)

    raceDataBox = ctk.CTkFrame(raceDataWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    raceDataBox.pack(pady=(15, 0), expand=True, fill=tk.Y)

    #RACE DATA CONTENTS

    fuelTankButton = ctk.CTkButton(raceDataBox, text="Fuel Tank \n capacity \n 75L", fg_color=buttonLightColor, corner_radius=0, text_font=(fontType, 15), width=180, height=70)
    fuelTankButton.pack(padx=10, pady=(20, 7))

    fuelConsButton = ctk.CTkButton(raceDataBox, text="Fuel \n consumption \n 3.5L/Lap", fg_color=buttonLightColor, corner_radius=0, text_font=(fontType, 15), width=180, height=70)
    fuelConsButton.pack(padx=10, pady=7)

    DTButton = ctk.CTkButton(raceDataBox, text="D.T. Time \n 32 sec", fg_color=buttonLightColor, corner_radius=0, text_font=(fontType, 15), width=180, height=70)
    DTButton.pack(padx=10, pady=7)

    refuelButton = ctk.CTkButton(raceDataBox, text="Refuel Time \n capacity \n 35 sec", fg_color=buttonLightColor, corner_radius=0, text_font=(fontType, 15), width=180, height=70)
    refuelButton.pack(padx=10, pady=7)

    refuelTimeButton = ctk.CTkButton(raceDataBox, text="Tyre Change \n  Time  \n 28 sec", fg_color=buttonLightColor, corner_radius=0, text_font=(fontType, 15), width=180, height=70)
    refuelTimeButton.pack(padx=10, pady=7)

    raceData = ctk.CTkLabel(raceDataWrap, text="RACE DATA", fg_color=background, text_font=(fontType, 15), width=0, text_color=accent)
    raceData.place(y=0, x=105, anchor=N)

    deWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    deWrap.pack(side=tk.LEFT, fill=tk.Y, padx=7)

    driverListWrap = ctk.CTkFrame(deWrap, fg_color=background)
    driverListWrap.pack(padx=0, pady=(22, 10), fill=tk.Y, expand=True)

    driverListBox = ctk.CTkFrame(driverListWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    driverListBox.pack(pady=(15, 0), fill=tk.Y, expand=True)

    for i in range (0, 4): 
        driver = ctk.CTkButton(driverListBox, text=("buton" + str(i)), fg_color=buttonLightColor, corner_radius=0, width=180, height=76, hover_color=hoverColor, text_font=(fontType, 15), text_color="white", command=eventsWindow.destroy)
        if i == 0: 
            driver.pack(pady=(20, 7), padx=15)
            continue
        driver.pack(padx=15, pady=7)
        pass

    raceData = ctk.CTkLabel(raceDataWrap, text="RACE DATA", fg_color=background, text_font=(fontType, 15), width=0, text_color=accent)
    raceData.place(y=0, x=105, anchor=N)

    driverList = ctk.CTkLabel(driverListWrap, text="DRIVER LIST", fg_color=background, text_color=accent, text_font=(fontType, 15), width=0)
    driverList.place(x=110, y=0, anchor=N)

    eventInfoWrap = ctk.CTkFrame(deWrap, height=100, width=60, fg_color=background)
    eventInfoWrap.pack(padx=7, pady=(10, 22))

    eventInfoBox = ctk.CTkFrame(eventInfoWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    eventInfoBox.pack(pady=(15, 0))

    #EVENT INFO CONTENTS

    dateButton = ctk.CTkButton(eventInfoBox, text="Date: \n 25/7/2022 \n 12:03", fg_color=buttonLightColor, corner_radius=0, width=180, height=60, hover_color=hoverColor, text_font=(fontType, 15), text_color="white", command=eventsWindow.destroy)
    dateButton.pack(padx=10, pady=(15, 7))

    startingDriver = ctk.CTkButton(eventInfoBox, text="Starting Driver:\nFernando Alonso", fg_color=buttonLightColor, corner_radius=0, width=180, height=60, hover_color=hoverColor, text_font=(fontType, 15), text_color="white", command=eventsWindow.destroy)
    startingDriver.pack(pady=7)

    eventInfo = ctk.CTkLabel(eventInfoWrap, fg_color=background, text="EVENT INFO", text_font=(fontType, 15), text_color=accent)
    eventInfo.place(x=100, y=0, anchor=N)
