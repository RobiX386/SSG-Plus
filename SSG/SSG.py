import tkinter as tk
import configparser
from livemode import livemodeFunc
from endurance import enduranceFunc
from sprint import sprintFunc
import customtkinter as ctk

#colors & fonts 

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

#V2.1 Color update

startWindow = tk.Tk()
startWindow['bg']=background
startWindow.title("SSG+")
startWindow.geometry("500x400+500+200")
startWindow.resizable(False, False)

def sprintCommands():
    sprintFunc()
    startWindow.destroy()

def enduranceCommands():
    enduranceFunc()
    startWindow.destroy()

def liveCommands():
    livemodeFunc()
    startWindow.destroy()


canvas = tk.Canvas(startWindow, width = 300, height = 150, bg=background, highlightbackground=background)      
canvas.pack(pady=(60,0))      
img = tk.PhotoImage(file="SSG.png")      
canvas.create_image(150,75, image=img) 

endurance = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Endurance", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=enduranceCommands)
endurance.pack(expand=True)

sprint = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Sprint", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=sprintCommands)
sprint.pack(expand=True)

live = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Live", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=liveCommands)
live.pack(expand=True)

startWindow.mainloop()