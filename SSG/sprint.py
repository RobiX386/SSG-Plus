from fileinput import filename
import tkinter as tk
import customtkinter as ctk
import configparser
import datetime
import webbrowser
import os

from matplotlib.pyplot import fill
from errorFile import error

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


def sprintFunc():
    from endurance import enduranceFunc
    from livemode import livemodeFunc

    sprintWindow = tk.Tk() 
    sprintWindow.config(bg=background)
    sprintWindow.title("SSG+ Sprint")
    sprintWindow.geometry("+350+100")
    sprintWindow.resizable(False, False)

    navBar = ctk.CTkFrame(sprintWindow, width=600, height=50, fg_color=navbarColor, corner_radius=0)
    navBar.pack(side=tk.TOP, fill=tk.X)

    buttonWrap = ctk.CTkFrame(navBar, fg_color=navbarColor, width=360)
    buttonWrap.pack(expand=True, pady=(0, 2))

    sprintButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Sprint", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, state=tk.DISABLED, command=lambda:[sprintFunc(), sprintWindow.destroy()])
    sprintButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    enduranceButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Endurance", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[enduranceFunc(), sprintWindow.destroy()])
    enduranceButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    liveButton = ctk.CTkButton(buttonWrap, width=80, height=20, text="Live", fg_color=accent, text_color=navButtonColor, hover_color=hoverColor, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda:[livemodeFunc(), sprintWindow.destroy()])
    liveButton.pack(expand=True, side=tk.LEFT, padx=20, pady=10)

    pcrWrap = tk.Frame(sprintWindow, bg=background) #presets && car info && race info
    pcrWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(10, 15))

    #PRESET START
    presets = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    presets.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(19, 15))

    presetsTitle = ctk.CTkLabel(pcrWrap, fg_color=background, text="Presets", text_font=(fontType, 18), text_color=mainTextColor, width=0)
    presetsTitle.place(x=173, y=5, anchor=tk.N)
    #CARINFO START

    carinfo = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    carinfo.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

    carinfoLabel = ctk.CTkLabel(pcrWrap, fg_color=background, text="#Car Info", text_font=(fontType, 18), text_color=mainTextColor, width=0)
    carinfoLabel.place(x=180, y=283, anchor=tk.N)

    tankWrap = tk.Frame(carinfo, bg=background)
    tankWrap.pack(fill=tk.X, side=tk.TOP, padx=2, pady=(25, 15))

    fuelTank = ctk.CTkLabel(tankWrap, text="Fuel Tank Size", text_font=(fontType, 18), text_color=mainTextColor, fg_color=background)
    fuelTank.pack(side = tk.LEFT, padx=(45, 15))

    fueltankvalue = ctk.CTkEntry(tankWrap, width=76, height=19, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="Liters", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    fueltankvalue.pack(pady=0, side=tk.LEFT)

    consWrap = tk.Frame(carinfo, bg=background)
    consWrap.pack(fill=tk.X, side=tk.TOP, padx=2, pady=15)

    fuelCons = ctk.CTkLabel(consWrap, text="Fuel Consumption", text_font=(fontType, 18), text_color=mainTextColor, fg_color=background)
    fuelCons.pack(side=tk.LEFT, padx=(24, 0))

    fuelconsvalue = ctk.CTkEntry(consWrap, width=76, height=19, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="L/Lap", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    fuelconsvalue.pack(side=tk.LEFT, pady=0)


    #RACE INFO

    raceinfo = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    raceinfo.pack(side=tk.TOP, fill=tk.X, pady=15)

    raceinfoLabel = ctk.CTkLabel(pcrWrap, text="#Race Info", text_font=(fontType, 18), text_color=mainTextColor, fg_color=background, width=40)
    raceinfoLabel.place(x=179, y=132, anchor=tk.N)

    lenghtWrap = tk.Frame(raceinfo, bg=background)
    lenghtWrap.pack(expand=True, side=tk.TOP, pady=(20, 15))

    racelenght = ctk.CTkLabel(lenghtWrap, text="Race Length", text_font=(fontType, 18), fg_color=background, text_color=mainTextColor)
    racelenght.pack(side=tk.LEFT, padx=(0, 20))

    racelenghtLapsValue = ctk.CTkEntry(lenghtWrap, width=40, height=19, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="Laps", placeholder_text_color=placeholderColor)
    racelenghtLapsValue.pack(side=tk.LEFT, padx=0)  

    laptimeWrap = tk.Frame(raceinfo, bg=background)
    laptimeWrap.pack(side=tk.TOP, expand=True, pady=15)

    laptime = ctk.CTkLabel(laptimeWrap, text="Lap Time", fg_color=background, text_color=mainTextColor, text_font=(fontType, 18))
    laptime.pack(side=tk.LEFT, padx=(30, 10), pady=0)

    lapMinValue = ctk.CTkEntry(laptimeWrap, width=40, height=19, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="min", placeholder_text_color=placeholderColor)
    lapMinValue.pack(side=tk.LEFT, padx=(0, 5))

    lapSecondsValue = ctk.CTkEntry(laptimeWrap, width=40, height=19, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    lapSecondsValue.pack(side=tk.LEFT, pady=0, padx=(5, 0))


    #buttons && pit info
    bprWrap = tk.Frame(sprintWindow, bg=background)
    bprWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(15, 20))

    #PIT INFO
    
    pitInfo = ctk.CTkFrame(bprWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    pitInfo.pack(fill=tk.X, side=tk.TOP, pady=(18, 10))

    pitInfoLabel = ctk.CTkLabel(bprWrap, fg_color=background, text_font=(fontType, 18), text="#Pit Info", text_color=mainTextColor, width=40)
    pitInfoLabel.place(x=140, y=2, anchor=tk.N)

    driveTimeWrap = tk.Frame(pitInfo, bg=background)
    driveTimeWrap.pack(padx=35,side=tk.TOP, expand=True, pady=(13, 13))

    driveTime = ctk.CTkLabel(driveTimeWrap, text="D.T. Time", text_font=(fontType, 18), fg_color=background, text_color=mainTextColor)
    driveTime.pack(side=tk.LEFT)

    driveTimeValue = ctk.CTkEntry(driveTimeWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    driveTimeValue.pack(side=tk.LEFT, padx=0)

    refuelWrap = tk.Frame(pitInfo, bg=background)
    refuelWrap.pack(padx=35,side=tk.TOP, expand=True, pady=12)

    refuelTime = ctk.CTkLabel(refuelWrap, fg_color=background, text_color=mainTextColor, text="Refuel Time", text_font=(fontType, 17))
    refuelTime.pack(side=tk.LEFT, padx=0)

    refuelTimeValue = ctk.CTkEntry(refuelWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    refuelTimeValue.pack(side=tk.LEFT, padx=0)

    tyreChangeWrap = tk.Frame(pitInfo, bg=background)
    tyreChangeWrap.pack(padx=35,side=tk.TOP, expand=True, pady=12)

    tyreChange = ctk.CTkLabel(tyreChangeWrap, text="Tyre Change \n Time ", text_font=(fontType, 15),  fg_color=background, text_color=mainTextColor)
    tyreChange.pack(side=tk.LEFT, padx=0)

    tyreChangeValue = ctk.CTkEntry(tyreChangeWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    tyreChangeValue.pack(padx=0, side=tk.LEFT)

    wearWrap = tk.Frame(pitInfo, bg=background)
    wearWrap.pack(padx=35,side=tk.TOP, expand=True, pady=(13, 10))

    wear = ctk.CTkLabel(wearWrap, text="Tyre Wear", fg_color=background, text_color=mainTextColor, text_font=(fontType, 18))
    wear.pack(side=tk.LEFT, padx=0)

    wearValue = ctk.CTkEntry(wearWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, text_color=entryTextColor)
    wearValue.pack(side=tk.LEFT, padx=0)

    #SELECT PRESET
    def carSelectwind():
        def trackSelectwind(car):
            def insertdata(track):
                #DATA INPUT
                inifilename=car+".ini"
                config = configparser.ConfigParser()
                config.read(inifilename)
                with open(inifilename, "w") as config_file:
                    config.write(config_file)
                
                keys = [
                    "fueltank",
                    "fuelcons",
                    "dttime",
                    "refueltime",
                    "tyrechangetime",
                    ]
                
                data = [ ]
                for key in keys:
                    value = (config.getfloat(track, key))
                    data.append(value)

                fueltankvalue.delete(0,tk.END)
                fueltankvalue.insert(0, data[0])
                fuelconsvalue.delete(0,tk.END)
                fuelconsvalue.insert(0, data[1])
                driveTimeValue.delete(0,tk.END)
                driveTimeValue.insert(0, data[2])
                refuelTimeValue.delete(0,tk.END)   
                refuelTimeValue.insert(0, data[3])
                tyreChangeValue.delete(0,tk.END)
                tyreChangeValue.insert(0, data[4])
                trackSelectWindow.destroy()

            #TRACK SELECT
            carSelectWindow.destroy()
                        
            trackSelectWindow = tk.Toplevel(sprintWindow)
            trackSelectWindow['bg']=background
            trackSelectWindow.title("SSG+")
            trackSelectWindow.geometry("+400+200")
            
            carConfig = configparser.ConfigParser()
            carConfig.read(car+".ini")
            trackList = carConfig.sections()

            trackSelectLabel = ctk.CTkLabel(trackSelectWindow, text="Select your track", fg_color=background, text_color=textcolor, text_font=(fontType, 18))
            trackSelectLabel.pack(side=tk.TOP, pady=(20, 0))

            trackSelectWrap = ctk.CTkFrame(trackSelectWindow, fg_color=background, border_color=accent, border_width=1)
            trackSelectWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

            for y in trackList: 
                trackfilename=y
                trackButtonName=y
                TrackSelect = ctk.CTkButton(trackSelectWrap, width=57, height=34, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, corner_radius=buttonRadius, text=trackButtonName, text_font=(fontType, 13), command= lambda trackfilename=trackfilename : insertdata(trackfilename))
                TrackSelect.pack(side=tk.TOP, pady=10, padx=20)
            
            trackSelectWindow.mainloop()
            
        #CAR SELECT
        
        carSelectWindow = tk.Toplevel(sprintWindow)
        carSelectWindow['bg']=background
        carSelectWindow.title("SSG+")
        carSelectWindow.geometry("+400+200")

        carSelectLabel = ctk.CTkLabel(carSelectWindow, text="Select the car", fg_color=background, text_color=textcolor, text_font=(fontType, 18))
        carSelectLabel.pack(side=tk.TOP, pady=(20,0))
        
        carSelecWrap = ctk.CTkFrame(carSelectWindow, fg_color=background, border_color=accent, border_width=borderWidth)
        carSelecWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()
        
        for x in carList: 
            carbuttonname=x
            carfilename=curentpath+x
            carselect = ctk.CTkButton(carSelecWrap, width=57, height=34, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, text=carbuttonname, text_font=(fontType, 13), corner_radius=buttonRadius, command=lambda carfilename=carfilename :trackSelectwind(carfilename))
            carselect.pack(side=tk.TOP, pady=10, padx=30)

        carSelectWindow.mainloop()

    #CREATE PRESET
    def createnewpreset():
        def filecheck(z):
            def choosetrackpreset():
                def tracksectioncheck(trackname):
                    def presetInputWindow():
                        def datainiwrite():
                            config.set(trackname, "fueltank", inputfueltankvalue.get())
                            fueltankvalue.delete(0,tk.END)
                            fueltankvalue.insert(0, inputfueltankvalue.get())
                            config.set(trackname, "fuelcons", inputfuelconsvalue.get())
                            fuelconsvalue.delete(0,tk.END)
                            fuelconsvalue.insert(0, inputfuelconsvalue.get())
                            config.set(trackname, "dttime", inputdriveTimevalue.get())
                            driveTimeValue.delete(0,tk.END)
                            driveTimeValue.insert(0, inputdriveTimevalue.get())
                            config.set(trackname, "refueltime", inputRefuelTimeValue.get())
                            config.set(trackname, "tyrechangetime", inputTyreChangeValue.get())   
                            tyreChangeValue.delete(0,tk.END)
                            tyreChangeValue.insert(0, inputTyreChangeValue.get())

                            inputWindow.destroy()

                            with open(carfilename, "w") as config_file:
                                config.write(config_file)
                            return 0

                        chooseTrackPresetWindow.destroy()
                        inputWindow = tk.Toplevel(sprintWindow)
                        inputWindow['bg']=background
                        inputWindow.title("SSG+ Input Window")
                        inputWindow.geometry("+400-200")


                        inputTitle = ctk.CTkLabel(inputWindow, text="Input your preset's data", fg_color=background, text_color=textcolor, text_font=(fontType, 18))
                        inputTitle.pack(side=tk.TOP, pady=30)

                        dataWrap = ctk.CTkFrame(inputWindow, border_color=accent, fg_color=background, border_width=1, corner_radius=cornerRadius)
                        dataWrap.pack(expand=True, padx=25, pady=(0, 25))

                        fuelTankWrap = tk.Frame(dataWrap, bg=background)
                        fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputFuelTank = ctk.CTkLabel(fuelTankWrap, text="Fuel Tank Size", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                        inputFuelTank.pack(side = tk.LEFT, padx=(20, 30))

                        inputfueltankvalue = ctk.CTkEntry(fuelTankWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Liters")
                        inputfueltankvalue.pack(side=tk.LEFT, padx=(0, 5))

                        fuelConsWrap = tk.Frame(dataWrap, bg=background)
                        fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputFuelCons = ctk.CTkLabel(fuelConsWrap, text="Fuel Consumption", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                        inputFuelCons.pack(side=tk.LEFT, padx=(0, 8))

                        inputfuelconsvalue = ctk.CTkEntry(fuelConsWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="L/Lap")
                        inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=(5, 5))

                        DTWrap = tk.Frame(dataWrap, bg=background)
                        DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputDriveTime = ctk.CTkLabel(DTWrap, text="D.T. Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                        inputDriveTime.pack(side=tk.LEFT, padx=(42, 22))

                        inputdriveTimevalue = ctk.CTkEntry(DTWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                        inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 5))

                        refuelWrap = tk.Frame(dataWrap, bg=background)
                        refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputRefuelTime = ctk.CTkLabel(refuelWrap, text="Refuel Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                        inputRefuelTime.pack(side=tk.LEFT, padx=(27, 56))

                        inputRefuelTimeValue = ctk.CTkEntry(refuelWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                        inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 5))

                        tyreWrap = tk.Frame(dataWrap, bg=background)
                        tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=15)

                        inputTyreChange = ctk.CTkLabel(tyreWrap, text="Tyre Change \n Time ", text_color=textcolor, fg_color=background, text_font=(fontType, 15))
                        inputTyreChange.pack(side=tk.LEFT, padx=(35, 55))

                        inputTyreChangeValue = ctk.CTkEntry(tyreWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                        inputTyreChangeValue.pack(padx=(0, 5), side=tk.LEFT)

                        dataSubmit = ctk.CTkButton(inputWindow, text="Submit", hover_color=hoverColor, fg_color=buttonColor, text_color=textcolor, height=61, width=108, text_font=(fontType, 15), corner_radius=buttonRadius, command=datainiwrite)
                        dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

                        inputWindow.mainloop()
                    
                    if len(str(trackpresetvalue.get())) < 2:
                        error("Car name is invalid")
                        exit()

                    config = configparser.ConfigParser()
                    config.read(carfilename)
                    config.add_section(trackname)
                    
                    with open(carfilename, "w") as config_file:
                        config.write(config_file)
                   
                    cartrackfilename = curentpath + z + "T.txt"
                    cartrackfile = open (cartrackfilename, "a")
                    cartrackfile.write(trackname+space)
                    cartrackfile.close()
                    presetInputWindow()
                    chooseTrackPresetWindow.destroy()

                
                createCarPreset.destroy()
                
                chooseTrackPresetWindow = tk.Toplevel(sprintWindow)
                chooseTrackPresetWindow['bg']=background
                chooseTrackPresetWindow.title("SSG+ Choose Track")
                chooseTrackPresetWindow.geometry("300x300+400+200")
                
                chooseTrackLabel = ctk.CTkLabel(chooseTrackPresetWindow, fg_color=background, text_color=textcolor, text="Choose a track for \nyour preset", text_font=(fontType, 18))
                chooseTrackLabel.pack(side=tk.TOP, expand=True)

                trackpresetvalue = ctk.CTkEntry(chooseTrackPresetWindow, width=171, height=27, text_font=(fontType, 14), placeholder_text="Track's name", placeholder_text_color=placeholderColor, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor)
                trackpresetvalue.pack(side=tk.TOP, expand=True)
                
                trackpresetsendbut = ctk.CTkButton(chooseTrackPresetWindow, text="Next", height=40, width=80, fg_color=foreground, text_color=textcolor, text_font=(fontType, 14), hover_color=hoverColor, corner_radius=buttonRadius, command=lambda:[tracksectioncheck(str(trackpresetvalue.get()).replace(" ", ""))])
                trackpresetsendbut.pack(side=tk.TOP, expand=True)
            
            if len(str(carpresetvalue.get())) < 2:
                error("Car name is invalid")
                exit()

            carfilename = curentpath + z + ".ini"
            
            try:
                open(carfilename, "x")
                carlistfile = open("CARS.txt", "a")
                carlistfile.write(z+space)
                choosetrackpreset()
            except:
                choosetrackpreset()


        createCarPreset = tk.Toplevel(sprintWindow)
        createCarPreset['bg']=background
        createCarPreset.title("SSG+ Create Preset")
        createCarPreset.geometry("300x300+400+200")

        selectCarLabel = ctk.CTkLabel(createCarPreset, fg_color=background, text_color=textcolor, text="Choose a car for \nyour preset", text_font=(fontType, 18))
        selectCarLabel.pack(side=tk.TOP, expand=True)
        
        carpresetvalue = ctk.CTkEntry(createCarPreset, width=171, height=27, text_font=(fontType, 14), placeholder_text="Car's name", placeholder_text_color=placeholderColor, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor)
        carpresetvalue.pack(side=tk.TOP, expand=True)

        carpresetsendbut = ctk.CTkButton(createCarPreset, text="Next", height=40, width=80, fg_color=foreground, text_color=textcolor, text_font=(fontType, 14), hover_color=hoverColor, corner_radius=buttonRadius, command=lambda:[filecheck(str(carpresetvalue.get()).replace(" ", ""))])
        carpresetsendbut.pack(side=tk.TOP, expand=True)

    #EDIT PRESET
    def editpresetcar():
        def editpresettrack(car):
            def presetInputWindow(trackname):
                def datainiwrite():
                    config = configparser.ConfigParser()
                    config.read(carfilename)
                    with open(carfilename, "w") as config_file:
                        config.write(config_file)
                    config.set(trackname, "fueltank", inputfueltankvalue.get())
                    fueltankvalue.delete(0,tk.END)
                    fueltankvalue.insert(0, inputfueltankvalue.get())
                    config.set(trackname, "fuelcons", inputfuelconsvalue.get())
                    fuelconsvalue.delete(0,tk.END)
                    fuelconsvalue.insert(0, inputfuelconsvalue.get())
                    config.set(trackname, "dttime", inputdriveTimevalue.get())
                    driveTimeValue.delete(0,tk.END)
                    driveTimeValue.insert(0, inputdriveTimevalue.get())
                    config.set(trackname, "refueltime", inputRefuelTimeValue.get())
                    config.set(trackname, "tyrechangetime", inputTyreChangeValue.get())   
                    tyreChangeValue.delete(0,tk.END)
                    tyreChangeValue.insert(0, inputTyreChangeValue.get())

                    inputWindow.destroy()

                    with open(carfilename, "w") as config_file:
                        config.write(config_file)
                    return 0

                editPresetTrackWindow.destroy()
                inputWindow = tk.Toplevel(sprintWindow)
                inputWindow['bg']=background
                inputWindow.title("SSG+ Input Window")
                inputWindow.geometry("+400-200")


                inputTitle = ctk.CTkLabel(inputWindow, text="Input your preset's data", fg_color=background, text_color=textcolor, text_font=(fontType, 18))
                inputTitle.pack(side=tk.TOP, pady=30)

                dataWrap = ctk.CTkFrame(inputWindow, border_color=accent, fg_color=background, border_width=1, corner_radius=cornerRadius)
                dataWrap.pack(expand=True, padx=25, pady=(0, 25))

                fuelTankWrap = tk.Frame(dataWrap, bg=background)
                fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputFuelTank = ctk.CTkLabel(fuelTankWrap, text="Fuel Tank Size", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                inputFuelTank.pack(side = tk.LEFT, padx=(20, 30))

                inputfueltankvalue = ctk.CTkEntry(fuelTankWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Liters")
                inputfueltankvalue.pack(side=tk.LEFT, padx=(0, 5))

                fuelConsWrap = tk.Frame(dataWrap, bg=background)
                fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputFuelCons = ctk.CTkLabel(fuelConsWrap, text="Fuel Consumption", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                inputFuelCons.pack(side=tk.LEFT, padx=(0, 8))

                inputfuelconsvalue = ctk.CTkEntry(fuelConsWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="L/Lap")
                inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=(5, 5))

                DTWrap = tk.Frame(dataWrap, bg=background)
                DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputDriveTime = ctk.CTkLabel(DTWrap, text="D.T. Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                inputDriveTime.pack(side=tk.LEFT, padx=(42, 22))

                inputdriveTimevalue = ctk.CTkEntry(DTWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 5))

                refuelWrap = tk.Frame(dataWrap, bg=background)
                refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputRefuelTime = ctk.CTkLabel(refuelWrap, text="Refuel Time", text_color=textcolor, fg_color=background, text_font=(fontType, 18))
                inputRefuelTime.pack(side=tk.LEFT, padx=(27, 56))

                inputRefuelTimeValue = ctk.CTkEntry(refuelWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 5))

                tyreWrap = tk.Frame(dataWrap, bg=background)
                tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=15)

                inputTyreChange = ctk.CTkLabel(tyreWrap, text="Tyre Change \n Time ", text_color=textcolor, fg_color=background, text_font=(fontType, 15))
                inputTyreChange.pack(side=tk.LEFT, padx=(35, 55))

                inputTyreChangeValue = ctk.CTkEntry(tyreWrap, width=75, height=18, text_color=entryTextColor, border_color=entryBorderColor, fg_color=entryFg, placeholder_text_color=placeholderColor, placeholder_text="Seconds")
                inputTyreChangeValue.pack(padx=(0, 5), side=tk.LEFT)

                dataSubmit = ctk.CTkButton(inputWindow, text="Submit", hover_color=hoverColor, fg_color=buttonColor, text_color=textcolor, height=61, width=108, text_font=(fontType, 15), corner_radius=buttonRadius, command=datainiwrite)
                dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

                inputWindow.mainloop()
            carfilename = curentpath + car+".ini"
            
            editpresetcarwindow.destroy()
            
            editPresetTrackWindow = tk.Toplevel(sprintWindow)
            editPresetTrackWindow['bg']=background
            editPresetTrackWindow.title("SSG+")
            editPresetTrackWindow.geometry("+400+200")

            trackEditLabel = ctk.CTkLabel(editPresetTrackWindow, text="Select which track \n you want to edit", text_font=(fontType, 18), text_color=textcolor, fg_color=background)
            trackEditLabel.pack(side=tk.TOP, pady=(20, 0))

            trackWrap = ctk.CTkFrame(editPresetTrackWindow, fg_color=background, border_color=accent, border_width=borderWidth)
            trackWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)
            
            carConfig = configparser.ConfigParser()
            carConfig.read(curentpath+car+".ini")
            trackList = carConfig.sections()

            for y in trackList: 
                trackButtonName=y
                trackEditSelect = ctk.CTkButton(trackWrap, width=57, height=34, text_font=(fontType, 13), text=trackButtonName, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, corner_radius=buttonRadius, command=lambda y=y :presetInputWindow(y))
                trackEditSelect.pack(side=tk.TOP, pady=10, padx=20)

        editpresetcarwindow = tk.Toplevel(sprintWindow) 
        editpresetcarwindow['bg']=background
        editpresetcarwindow.title("SSG+ Edit preset")
        editpresetcarwindow.geometry("+400+200")
        
        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()

        carEditLabel = ctk.CTkLabel(editpresetcarwindow, text="Select which preset \nyou want to edit", text_font=(fontType, 18), fg_color=background, text_color=textcolor)
        carEditLabel.pack(side=tk.TOP, pady=(20, 0))

        carWrap = ctk.CTkFrame(editpresetcarwindow, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
        carWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)
        
        for x in carList: 
            carbuttonname=x
            carselect = ctk.CTkButton(carWrap, width=57, height=34, text=carbuttonname, text_font=(fontType, 13), fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, corner_radius=buttonRadius, command=lambda x=x :editpresettrack(x))
            carselect.pack(side=tk.TOP, pady=10, padx=20)

    #PRESET BUTTONS

    newpreset = ctk.CTkButton(presets, width=30, height=45, text="New Preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13),command=createnewpreset)
    newpreset.pack(side=tk.LEFT, padx=5, expand=True, pady=25)

    carselectbut = ctk.CTkButton(presets, width=30, height=45, text="Select preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13), command=carSelectwind)
    carselectbut.pack(side=tk.LEFT, pady=25, padx=5, expand=True)

    editpresetbut = ctk.CTkButton(presets, width=30, height=45, text="Edit Preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13), command=editpresetcar)
    editpresetbut.pack(side=tk.LEFT, padx=5, expand=True, pady=25)


    #CALCULATE STRATEGY
    def submitSprint():
        
        #car info
        fueltank = float(fueltankvalue.get())
        fuelcons = float(fuelconsvalue.get())
        wear = float(wearValue.get())

        #race info
        racelengthlaps = int(racelenghtLapsValue.get())
        laptime = float(lapMinValue.get())*60+float(lapSecondsValue.get())
        
        #pit info

        dttime = float(driveTimeValue.get())
        tyrechangetime = float(tyreChangeValue.get())


        #Stint calculations
        fuelneed=racelengthlaps*fuelcons 
        
        sprintText = ""
        ratio = 1 / wear
        fastesttime = 200000000
        fasteststrat = 0

        for pitcount in range(7):
            racetime = laptime*racelengthlaps+wear*racelengthlaps*wear*(racelengthlaps+1)*ratio*0.5/(pitcount+1)+(dttime+tyrechangetime)*pitcount
            racetime = int(racetime)
            conversion=datetime.timedelta(seconds=racetime)
            sprintText+=str(pitcount)+" stop - "+str(conversion) + "\n"
            if racetime<fastesttime :
                fastesttime = racetime
                fasteststrat = pitcount

        outputWindow = tk.Toplevel(sprintWindow)
        outputWindow.title("SSG+ Sprint Output")
        outputWindow['bg'] = background

        sprintOutput = ctk.CTkLabel(outputWindow, text="Sprint Strategy", fg_color=background, text_color=textcolor, text_font=(fontType, 20))
        sprintOutput.pack(expand=True, pady=(20, 0))

        outputWrap = ctk.CTkFrame(outputWindow, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
        outputWrap.pack(expand=True, pady=20, padx=40)

        outputText = tk.Label(outputWrap, text=sprintText, bg=background, fg="#cccccc")
        outputText.config(font=(fontType, 15))
        outputText.pack(padx=10, pady=10)

        conversion=datetime.timedelta(seconds=fastesttime)
        sprintFastestText = "Fastest strategy is - > "+str(fasteststrat)+ " stopper = "+str(conversion) +"\n" +"Fuel needed = " + str(fuelneed)
        fastestStrategy = tk.Label(outputWrap, text=sprintFastestText, bg=background, fg="#cccccc")
        fastestStrategy.config(font=(fontType, 18))
        fastestStrategy.pack(pady=(0, 10), padx=10)

        closeOutput = ctk.CTkButton(outputWindow, text="Close Window", width=100, height=40, fg_color=buttonColor, text_color=textcolor, hover_color="red", command=outputWindow.destroy)
        closeOutput.pack(expand=True, pady=(0, 15))

        outputWindow.mainloop()



    #OTHER BUTTONS

    submitData = ctk.CTkButton(bprWrap, text="Calculate \n Strategy", text_font=(fontType, 14), width=160,height=59, fg_color=buttonColor, text_color=textcolor, hover_color="#547a1f", corner_radius=buttonRadius, command=submitSprint)
    submitData.pack(side=tk.TOP, expand=True, pady=5)

    exitButton = ctk.CTkButton(bprWrap, text="Exit", text_font=(fontType, 14), width=160, height=59, fg_color=buttonColor, text_color=textcolor, hover_color="red", corner_radius=buttonRadius, command=sprintWindow.destroy)
    exitButton.pack(expand=True, side=tk.TOP, pady=(5, 15))