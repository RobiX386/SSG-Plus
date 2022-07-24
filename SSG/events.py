import tkinter as tk
import configparser
import datetime
from turtle import width
import webbrowser
import os
import customtkinter as ctk
from errorFile import error
import sys
from tkinter import ttk


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

space= ' '
curentpath = os.getcwd() + "/presets"+"//"

def eventsFunc():
    from sprint import sprintFunc
    from livemode import livemodeFunc
    from endurance import enduranceFunc

    eventsWindow = tk.Tk()
    eventsWindow.title("SSG+ Select Events")
    eventsWindow.attributes("-topmost", "true")
    eventsWindow.geometry("500x500")
    eventsWindow.config(bg=background)
    eventsWindow.resizable(False, False)

    navBar = ctk.CTkFrame(eventsWindow, width=600, height=50, fg_color=navbarColor, corner_radius=0)
    navBar.pack(side=tk.TOP, fill=tk.X)

    buttonWrap = ctk.CTkFrame(navBar, fg_color=navbarColor, width=360)
    buttonWrap.pack(expand=False, pady=(0, 2))

    sprintButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Sprint", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[sprintFunc(), eventsWindow.destroy()])
    sprintButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    enduranceButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Endurance", fg_color=navDisabledColor, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, state=tk.DISABLED, command=lambda:[enduranceFunc(), eventsWindow.destroy()])
    enduranceButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    liveButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Live", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[livemodeFunc(), eventsWindow.destroy()])
    liveButton.pack(expand=False, side=tk.LEFT, padx=20, pady=10)

    eventsWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    eventsWrap.pack(side=tk.LEFT)

    eventsBox = ctk.CTkFrame(eventsWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    eventsBox.pack(expand=False)

    eventsCanvas = tk.Canvas(eventsBox)
    eventsCanvas.pack(side=tk.LEFT)

    eventsScroll = ttk.Scrollbar(eventsBox, orient="vertical", command=eventsCanvas.yview)
    eventsScroll.pack(side=tk.RIGHT, fill=tk.Y)

    eventsCanvas.configure(yscrollcommand=eventsScroll.set, scrollregion=lambda:eventsBox.bbox("all"))

    eventsCanvas.bind("<Configure>")

    buttonWrap = tk.Frame(eventsCanvas)
    buttonWrap.pack(padx=30)

    for i in range (0, 50):
        event = ctk.CTkButton(buttonWrap, text=("buton" + str(i)), fg_color="red", text_color="white")
        event.pack()

    buttonWrap = ctk.CTkFrame(eventsWrap, fg_color=background)
    buttonWrap.pack(side=tk.TOP, pady=10)

    createEvent = ctk.CTkButton(buttonWrap, fg_color=buttonColor, text_color=textcolor, width=70, height=40, text="Create \n event", text_font=(fontType, 13), hover_color=hoverColor, corner_radius=buttonRadius)
    createEvent.pack(side=tk.LEFT, padx=10)

    loadEvent = ctk.CTkButton(buttonWrap, fg_color=buttonColor, text_color=textcolor, width=70, height=40, text="Load \n event", text_font=(fontType, 13), hover_color=hoverColor, corner_radius=buttonRadius)
    loadEvent.pack(side=tk.LEFT, padx=10)

    reWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    reWrap.pack(side=tk.LEFT)

    raceDataWrap = ctk.CTkFrame(reWrap, fg_color=background)
    raceDataWrap.pack()

    raceDataBox = ctk.CTkFrame(raceDataWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    raceDataBox.pack()

    #RACE DATA CONTENTS

    eventNameWrap = ctk.CTkFrame(reWrap, fg_color=background)
    eventNameWrap.pack()

    eventNameBox = ctk.CTkFrame(eventNameWrap, fg_color=background, border_width=borderWidth, border_color=accent, corner_radius=cornerRadius)
    eventNameBox.pack()

    eventName = ctk.CTkLabel(eventNameBox, text="24h of \n LeMans S15", fg_color=background)
    eventName.pack(padx=10, pady=30)

    deWrap = ctk.CTkFrame(eventsWindow, fg_color=background)
    deWrap.pack(side=tk.LEFT)

    driverListWrap = ctk.CTkFrame(deWrap, height=350, width=60, fg_color=background)
    driverListWrap.pack(padx=10, pady=10)

    driverListBox = ctk.CTkFrame(driverListWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    driverListBox.pack(expand=False)

    # for i in range(0, 5):
    #     test = ctk.CTkButton(driverListBox, width=100, height=50, fg_color=buttonColor text="Fernando \n Alonso \n 1:24", corner_radius=buttonRadius)
    #     test.pack(pady=5, padx=10)

    eventInfoWrap = ctk.CTkFrame(deWrap, height=100, width=60, fg_color=background)
    eventInfoWrap.pack(padx=10, pady=10)

    eventInfoBox = ctk.CTkFrame(eventInfoWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    eventInfoBox.pack()
