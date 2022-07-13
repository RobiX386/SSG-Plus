import tkinter as tk
import configparser
import customtkinter as ctk

design = configparser.ConfigParser()
design.read("design.ini")

background=design.get("COLOR", "background")
foreground=design.get("COLOR", "foreground")
accent=design.get("COLOR", "accent")
textcolor=design.get("COLOR", "textcolor")
fontType=design.get("FONT", "fontFamily")
borderWidth=int(design.get("BORDER", "borderWidth"))
cornerRadius=int(design.get("BORDER", "cornerRadius"))
buttonColor=design.get("BUTTON", "buttonColor")
buttonRadius=int(design.get("BUTTON", "cornerRadius"))
hoverColor=design.get("BUTTON", "hoverColor")

def error(errortext):
    errorWindow = tk.Tk() 
    errorWindow.config(bg=background)
    errorWindow.geometry("+450+250")
    errorWindow.title("SSG+")
    errorFrame = ctk.CTkFrame(errorWindow, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    errorFrame.pack(expand=True, padx=25, pady=40)
    errorlabel = ctk.CTkLabel(errorFrame, text=errortext, fg_color=background, text_color=textcolor, text_font=(fontType, 18))
    errorlabel.pack(pady=20, padx=15)
    errorbutton = ctk.CTkButton(errorFrame, text="Close Window", fg_color=buttonColor, text_color="#cccccc", hover_color="red", corner_radius=buttonRadius, command = errorWindow.destroy)
    errorbutton.pack(pady=(10,20))