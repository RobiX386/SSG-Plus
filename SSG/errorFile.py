import tkinter as tk
import configparser

design = configparser.ConfigParser()
design.read("design.ini")

background=design.get("COLOR", "background")
foreground=design.get("COLOR", "foreground")
accent=design.get("COLOR", "accent")
textcolor=design.get("COLOR", "textcolor")
fontType=design.get("FONT", "fontFamily")

def error(errortext):
    errorWindow = tk.Tk() 
    errorWindow.config(bg=background)
    errorWindow.geometry("200x200+450+250")
    errorWindow.title("SSG+")
    errorFrame = tk.Frame(errorWindow, bg=background, highlightbackground=accent, highlightthickness=1)
    errorFrame.pack(expand=True, padx=15, pady=20)
    errorlabel = tk.Label(errorFrame, text = errortext, fg= "white", bg=background)
    errorlabel.config(font=(18))
    errorlabel.pack(pady=20, padx=15)
    errorbutton = tk.Button(errorFrame, text="Close Window", bg=foreground, fg="#cccccc", activebackground="red", activeforeground="white", command = errorWindow.destroy)
    errorbutton.pack(pady=(10,20))