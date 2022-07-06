import tkinter as tk
import configparser
from endurance import enduranceFunc
from sprint import sprintFunc

#colors & fonts 

design = configparser.ConfigParser()
design.read("design.ini")

background=design.get("COLOR", "background")
foreground=design.get("COLOR", "foreground")
accent=design.get("COLOR", "accent")
textcolor=design.get("COLOR", "textcolor")
buttonColor=design.get("COLOR", "buttonColor")
fontType=design.get("FONT", "fontFamily")


#V2.1 Color update

startWindow = tk.Tk()
startWindow['bg']=background
startWindow.title("SSG+")
startWindow.geometry("500x400+500+200")

def sprintCommands():
    sprintFunc()
    startWindow.destroy()

def enduranceCommands():
    enduranceFunc()
    startWindow.destroy()

canvas = tk.Canvas(startWindow, width = 300, height = 150, bg=background, highlightbackground=background)      
canvas.pack(pady=(60,0))      
img = tk.PhotoImage(file="SSG.png")      
canvas.create_image(150,75, image=img) 

endurance = tk.Button(startWindow, text="Endurance", height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1, command=enduranceCommands)
endurance.config(font=(fontType,15))
endurance.pack(expand=True)

sprint = tk.Button(startWindow, text="Sprint", height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1, command=sprintCommands)
sprint.config(font=(fontType, 15))
sprint.pack(expand=True)

startWindow.mainloop()