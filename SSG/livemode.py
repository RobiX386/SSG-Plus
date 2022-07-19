from fileinput import filename
import tkinter as tk
import configparser
import datetime
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

space= ' '
curentpath = os.getcwd() + "\presets"+"\\"

def livemodeFunc():
    from endurance import enduranceFunc
    from sprint import sprintFunc


    liveWindow = tk.Tk()
    liveWindow.config(bg=background)
    liveWindow.title("SSG+ Live")
    liveWindow.geometry("+300+100")
    # liveWindow.resizable(False, False)

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

    startStop = ctk.CTkButton(dataWrap, fg_color=buttonColor, text="Start/Stop \n event", text_color=textcolor, corner_radius=buttonRadius, height=60, text_font=(fontType, 16))
    startStop.pack(side=tk.TOP, pady=(15, 0))