import tkinter as tk
import customtkinter as ctk
import configparser
from tkcalendar import Calendar
import os

eventpath = os.getcwd() + "/events"+"//"

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


inputWindow = tk.Tk()
inputWindow['bg']=background
inputWindow.title("SSG+ Input Window")
inputWindow.geometry("1050x620-400+0")

def writeData():
    file = configparser.ConfigParser()
    filename=eventpath+nameValue.get()+".ini"
    try:
        open(filename, "x")
        file.read(filename)
    except:
        print()
    
    file.add_section("DRIVERS")
    if driver1Value.get() != '':
        templaptime=int(driver1MinValue.get())*60+int(driver1SecValue.get())
        file.set("DRIVERS",str(driver1Value.get()),str(templaptime))
    if driver2Value.get() != '':
        templaptime=int(driver2MinValue.get())*60+int(driver2SecValue.get())
        file.set("DRIVERS",str(driver2Value.get()),str(templaptime))
    if driver3Value.get() != '':
        templaptime=int(driver3MinValue.get())*60+int(driver3SecValue.get())
        file.set("DRIVERS",str(driver3Value.get()),str(templaptime))
    if driver4Value.get() != '':
        templaptime=int(driver4MinValue.get())*60+int(driver4SecValue.get())
        file.set("DRIVERS",str(driver4Value.get()),str(templaptime))

    file.add_section("RACEDATA")
    file.set("RACEDATA",'fueltank',inputfueltankvalue.get())
    file.set("RACEDATA",'fuelcons',inputfuelconsvalue.get())
    file.set("RACEDATA",'dttime',inputdriveTimevalue.get())
    file.set("RACEDATA",'refueltime',inputRefuelTimeValue.get())
    file.set("RACEDATA",'tyrechangetime',inputTyreChangeValue.get())

    file.add_section("NAME")
    file.set("NAME",'name',nameValue.get())

    file.add_section("RACEINFO")
    file.set("RACEINFO","date",raceCalendar.get_date())
    file.set("RACEINFO",'time',hourValue.get())
    file.set("RACEINFO",'startingdriver',startingValue.get())

    with open(filename, "w") as config_file:
        file.write(config_file)
    
    inputWindow.destroy()


inputTitle = ctk.CTkLabel(inputWindow, text="Input your preset's data", fg_color=background, text_color=textcolor, text_font=(fontType, 18))
inputTitle.pack(side=tk.TOP, pady=30)

dataWrap = ctk.CTkFrame(inputWindow, fg_color=background)
dataWrap.pack(expand=True, padx=25, pady=20, side=tk.LEFT)

driversWrap = ctk.CTkFrame(dataWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
driversWrap.pack(padx=10, pady=(10, 19))

driver1Wrap = ctk.CTkFrame(driversWrap, fg_color=background)
driver1Wrap.pack(padx=10, pady=10)

driver1Label = ctk.CTkLabel(driver1Wrap, fg_color=background, text_color=textcolor, text="Driver 1", text_font=(fontType, 17))
driver1Label.pack(side=tk.LEFT)

driver1Value = ctk.CTkEntry(driver1Wrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Driver's Name", width=130, height=20, placeholder_text_color=placeholderColor)
driver1Value.pack(side=tk.LEFT)

timeWrap = ctk.CTkFrame(driver1Wrap, fg_color=background)
timeWrap.pack(side=tk.LEFT)

driver1MinValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Min", width=44, height=20, placeholder_text_color=placeholderColor)
driver1MinValue.pack(side=tk.LEFT, padx=5)

driver1SecValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Sec", width=44, height=20, placeholder_text_color=placeholderColor)
driver1SecValue.pack(side=tk.LEFT, padx=(0, 5))

driver2Wrap = ctk.CTkFrame(driversWrap, fg_color=background)
driver2Wrap.pack(padx=10, pady=10)

driver2Label = ctk.CTkLabel(driver2Wrap, fg_color=background, text_color=textcolor, text="Driver 2", text_font=(fontType, 17))
driver2Label.pack(side=tk.LEFT)

driver2Value = ctk.CTkEntry(driver2Wrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Driver's Name", width=130, height=20, placeholder_text_color=placeholderColor)
driver2Value.pack(side=tk.LEFT)

timeWrap = ctk.CTkFrame(driver2Wrap, fg_color=background)
timeWrap.pack(side=tk.LEFT)

driver2MinValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Min", width=44, height=20, placeholder_text_color=placeholderColor)
driver2MinValue.pack(side=tk.LEFT, padx=5)

driver2SecValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Sec", width=44, height=20, placeholder_text_color=placeholderColor)
driver2SecValue.pack(side=tk.LEFT, padx=(0, 5))


driver3Wrap = ctk.CTkFrame(driversWrap, fg_color=background)
driver3Wrap.pack(padx=10, pady=10)

driver3Label = ctk.CTkLabel(driver3Wrap, fg_color=background, text_color=textcolor, text="Driver 3", text_font=(fontType, 17))
driver3Label.pack(side=tk.LEFT)

driver3Value = ctk.CTkEntry(driver3Wrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Driver's Name", width=130, height=20, placeholder_text_color=placeholderColor)
driver3Value.pack(side=tk.LEFT)

timeWrap = ctk.CTkFrame(driver3Wrap, fg_color=background)
timeWrap.pack(side=tk.LEFT)

driver3MinValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Min", width=44, height=20, placeholder_text_color=placeholderColor)
driver3MinValue.pack(side=tk.LEFT, padx=5)

driver3SecValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Sec", width=44, height=20, placeholder_text_color=placeholderColor)
driver3SecValue.pack(side=tk.LEFT, padx=(0, 5))


driver4Wrap = ctk.CTkFrame(driversWrap, fg_color=background)
driver4Wrap.pack(padx=10, pady=10)

driver4Label = ctk.CTkLabel(driver4Wrap, fg_color=background, text_color=textcolor, text="Driver 4", text_font=(fontType, 17))
driver4Label.pack(side=tk.LEFT)

driver4Value = ctk.CTkEntry(driver4Wrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Driver's Name", width=130, height=20, placeholder_text_color=placeholderColor)
driver4Value.pack(side=tk.LEFT)

timeWrap = ctk.CTkFrame(driver4Wrap, fg_color=background)
timeWrap.pack(side=tk.LEFT)

driver4MinValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Min", width=44, height=20, placeholder_text_color=placeholderColor)
driver4MinValue.pack(side=tk.LEFT, padx=5)

driver4SecValue = ctk.CTkEntry(timeWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Sec", width=44, height=20, placeholder_text_color=placeholderColor)
driver4SecValue.pack(side=tk.LEFT, padx=(0, 5))

calendarWrap = ctk.CTkFrame(inputWindow, fg_color=background)
calendarWrap.pack(side=tk.LEFT)

raceCalendar = Calendar(dataWrap, foreground=accent, background=textcolor)
raceCalendar.config(font=15)
raceCalendar.pack(pady=10)

carWrap = ctk.CTkFrame(calendarWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
carWrap.pack(padx=10, pady=(20, 30))

fuelTankWrap = tk.Frame(carWrap, bg=background)
fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=86)

inputFuelTank = ctk.CTkLabel(fuelTankWrap, text="Fuel Tank Size", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
inputFuelTank.pack(side = tk.LEFT, padx=0)

inputfueltankvalue = ctk.CTkEntry(fuelTankWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Liters")
inputfueltankvalue.pack(side=tk.LEFT, padx=0)

fuelConsWrap = tk.Frame(carWrap, bg=background)
fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=3)

inputFuelCons = ctk.CTkLabel(fuelConsWrap, text="Fuel\nConsumption", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
inputFuelCons.pack(side=tk.LEFT, padx=0)

inputfuelconsvalue = ctk.CTkEntry(fuelConsWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="L/Lap")
inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=0)

DTWrap = tk.Frame(carWrap, bg=background)
DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=0)

inputDriveTime = ctk.CTkLabel(DTWrap, text="D.T. Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
inputDriveTime.pack(side=tk.LEFT, padx=0)

inputdriveTimevalue = ctk.CTkEntry(DTWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
inputdriveTimevalue.pack(side=tk.LEFT, padx=0)

refuelWrap = tk.Frame(carWrap, bg=background)
refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=0)

inputRefuelTime = ctk.CTkLabel(refuelWrap, text="Refuel Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
inputRefuelTime.pack(side=tk.LEFT, padx=0)

inputRefuelTimeValue = ctk.CTkEntry(refuelWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
inputRefuelTimeValue.pack(side=tk.LEFT, padx=0)

tyreWrap = tk.Frame(carWrap, bg=background)
tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=0)

inputTyreChange = ctk.CTkLabel(tyreWrap, text="Tyre Change \n Time ", text_color=textcolor, fg_color=background, text_font=(fontType, 15))
inputTyreChange.pack(side=tk.LEFT, padx=0)

inputTyreChangeValue = ctk.CTkEntry(tyreWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
inputTyreChangeValue.pack(padx=0, side=tk.LEFT)

dataSubmit = ctk.CTkButton(inputWindow, text="Submit", hover_color=hoverColor, fg_color=buttonColor, text_color=textcolor, height=61, width=108, text_font=(fontType, 15), corner_radius=buttonRadius,command=writeData)
dataSubmit.pack(side=tk.TOP, expand=True, pady=0)

eventWrap = ctk.CTkFrame(calendarWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
eventWrap.pack(pady=(0, 10))

nameWrap = ctk.CTkFrame(eventWrap, fg_color=background)
nameWrap.pack(padx=60, pady=10)

nameLabel = ctk.CTkLabel(nameWrap, text="Event name", fg_color=background, text_color=textcolor, text_font=(fontType, 17))
nameLabel.pack(side=tk.LEFT)

nameValue = ctk.CTkEntry(nameWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Events's Name", width=130, height=20, placeholder_text_color=placeholderColor)
nameValue.pack(side=tk.LEFT)

hourWrap = ctk.CTkFrame(eventWrap, fg_color=background)
hourWrap.pack(padx=10, pady=10)

hourLabel = ctk.CTkLabel(hourWrap, text="Starting Time", fg_color=background, text_color=textcolor, text_font=(fontType, 17))
hourLabel.pack(side=tk.LEFT)

hourValue = ctk.CTkEntry(hourWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="Start Time", width=130, height=20, placeholder_text_color=placeholderColor)
hourValue.pack(side=tk.LEFT)

startingWrap = ctk.CTkFrame(eventWrap, fg_color=background)
startingWrap.pack(pady=10)

startingLabel = ctk.CTkLabel(startingWrap, fg_color=background, text="Starting Driver", text_color=textcolor, text_font=(fontType, 17))
startingLabel.pack(side=tk.LEFT)

startingValue = ctk.CTkEntry(startingWrap, fg_color=entryFg, text_color=entryTextColor, border_color=entryBorderColor, placeholder_text="1/2/3/4 only No.", width=130, height=20, placeholder_text_color=placeholderColor)
startingValue.pack(side=tk.LEFT)

inputWindow.mainloop()