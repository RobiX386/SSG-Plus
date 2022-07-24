import tkinter as tk
import configparser
from livemode import livemodeFunc
from endurance import enduranceFunc
from sprint import sprintFunc
from events import eventsFunc
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
userName=design.get("USER", "name")

#V2.1 Color update

startWindow = tk.Tk()
startWindow['bg']=background
startWindow.title("SSG+")
startWindow.geometry("+500+200")
startWindow.resizable(False, False)

def changeName():

    def iniWrite():
        with open('design.ini', 'w') as configfile:
            design.write(configfile)

    nameWindow = tk.Tk()
    nameWindow.config(bg=background)
    nameWindow.title("SSG+ Change User Name")
    nameWindow.geometry("+500+200")
    nameWindow.resizable(False, False)
    
    chooseNameLabel = ctk.CTkLabel(nameWindow, fg_color=background, text_color=textcolor, text="Name", text_font=(fontType, 18))
    chooseNameLabel.pack(side=tk.TOP, expand=True, pady=(30, 0))

    nameValue = ctk.CTkEntry(nameWindow, width=171, height=27, text_font=(fontType, 14), placeholder_text="Your name", placeholder_text_color=placeholderColor, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor)
    nameValue.pack(side=tk.TOP, expand=True, pady=50, padx=30)

    nameSubmit = ctk.CTkButton(nameWindow, text="Next", height=40, width=80, fg_color=foreground, text_color=textcolor, text_font=(fontType, 14), hover_color=hoverColor, corner_radius=buttonRadius, command=lambda:[design.set("USER", "name", nameValue.get()), iniWrite(), nameWindow.destroy()])
    nameSubmit.pack(side=tk.TOP, expand=True, pady=(0, 30))


canvas = tk.Canvas(startWindow, width = 300, height = 150, bg=background, highlightbackground=background)      
canvas.pack(pady=(40,0))
img = tk.PhotoImage(file="SSG.png")     
canvas.create_image(150,75, image=img) 

greeting = ctk.CTkButton(startWindow, text="Hello, " + userName, text_font=(fontType, 18), text_color=mainTextColor, fg_color=background, hover_color=hoverColor, command=changeName)
greeting.pack(side=tk.TOP, pady=(30, 0))

endurance = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Endurance", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=lambda:[enduranceFunc(), startWindow.destroy()])
endurance.pack(side=tk.LEFT, expand=True, padx=15, pady=(50, 90))

sprint = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Sprint", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=lambda:[sprintFunc(), startWindow.destroy()])
sprint.pack(side=tk.LEFT, expand=True, padx=15, pady=(50, 90))

live = ctk.CTkButton(startWindow, text_font=(fontType, 15), text="Live", height=62, width=171, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, border_width=0, corner_radius=cornerRadius, command=lambda:[eventsFunc(), startWindow.destroy()])
live.pack(side=tk.LEFT, expand=True, padx=15, pady=(50, 90))

startWindow.mainloop()