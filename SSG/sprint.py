from fileinput import filename
import tkinter as tk
import configparser
import datetime
import webbrowser
import os
from errorFile import error

#colors&&fonts

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

space= ' '
curentpath = os.getcwd() + "\presets"+"\\"


def sprintFunc():
    sprintWindow = tk.Tk() 
    sprintWindow.config(bg=background)
    sprintWindow.title("SSG+ Sprint")
    sprintWindow.geometry("+350+100")

    pcrWrap = tk.Frame(sprintWindow, bg=background, width=500, height=300) #presets && car info && race info
    pcrWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(20, 15))

    #PRESET START
    presets = tk.Frame(pcrWrap, bg=background, highlightbackground=accent, highlightthickness=1)
    presets.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    presetsTitle = tk.Label(presets, bg=background, text="Presets", fg="white", width=17)
    presetsTitle.config(font=('Helvatical bold',18))
    presetsTitle.pack(pady=(15, 0))

    #CARINFO START

    carinfo = tk.Frame(pcrWrap, bg=background, highlightbackground=accent, highlightthickness=1)
    carinfo.pack(side=tk.BOTTOM, fill=tk.X)

    carinfoLabel = tk.Label(carinfo, bg=background, text="#Car Info", fg="white", width=24)
    carinfoLabel.config(font=('Helvatical bold',18))
    carinfoLabel.pack()

    tankWrap = tk.Frame(carinfo, bg=background)
    tankWrap.pack(fill=tk.X, side=tk.TOP, padx=20)

    fuelTank = tk.Label(tankWrap, text="Fuel Tank Size", fg="white", bg=background)
    fuelTank.config(font=(fontType, 18))
    fuelTank.pack(side = tk.LEFT, padx=(0, 44))

    fueltankvalue = tk.Entry(tankWrap, width=12, bg="white")
    fueltankvalue.pack(pady=20, side=tk.LEFT)

    liters = tk.Label(tankWrap, text="Liters", bg=background, fg="white")
    liters.pack(side=tk.LEFT, fill=tk.Y)

    consWrap = tk.Frame(carinfo, bg=background)
    consWrap.pack(fill=tk.X, side=tk.TOP, padx=(4, 20))

    fuelCons = tk.Label(consWrap, text="Fuel Consumption", fg="white", bg=background, width=16)
    fuelCons.config(font=(fontType, 18))
    fuelCons.pack(side=tk.LEFT)

    fuelconsvalue = tk.Entry(consWrap, width=12, bg="white")
    fuelconsvalue.pack(side=tk.LEFT, pady=20)

    lperlap = tk.Label(consWrap, text="L/Lap", fg="white", bg=background)
    lperlap.pack(side=tk.LEFT, fill=tk.Y)    



    #RACE INFO

    raceinfo = tk.Frame(pcrWrap, bg=background, highlightbackground=accent, highlightthickness=1)
    raceinfo.pack(side=tk.TOP, fill=tk.X, pady=15)

    raceinfoLabel = tk.Label(raceinfo, text="#Race Info", fg="white", width=24, bg=background)
    raceinfoLabel.config(font=(fontType, 18))
    raceinfoLabel.pack()

    lenghtWrap = tk.Frame(raceinfo, bg=background)
    lenghtWrap.pack(expand=True, side=tk.TOP)

    racelenght = tk.Label(lenghtWrap, width=10, text="Race Length", bg=background, fg="White", height=3)
    racelenght.config(font=(fontType, 18))
    racelenght.pack(side=tk.LEFT, padx=(10, 24))

    racelenghtLapsValue = tk.Entry(lenghtWrap, width=5, fg="black")
    racelenghtLapsValue.pack(side=tk.LEFT)

    laps = tk.Label(lenghtWrap, text="Laps", bg=background, fg="white")
    laps.pack(side=tk.LEFT, padx=(5, 22))

    laptimeWrap = tk.Frame(raceinfo, bg=background)
    laptimeWrap.pack(side=tk.TOP, expand=True)

    laptime = tk.Label(laptimeWrap, text="Lap Time", bg=background, fg="white", height=3)
    laptime.config(font=(fontType, 18))
    laptime.pack(side=tk.LEFT, padx=(15, 41), pady=(0, 9))

    lapMinValue = tk.Entry(laptimeWrap, width=3, fg="black")
    lapMinValue.pack(side=tk.LEFT)

    lapMinutes = tk.Label(laptimeWrap, text="min", bg=background, fg="white")
    lapMinutes.pack(side=tk.LEFT, padx=5)

    lapSecondsValue = tk.Entry(laptimeWrap, width=5, fg="black")
    lapSecondsValue.pack(side=tk.LEFT, pady=0)

    seconds = tk.Label(laptimeWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT, padx=(2, 0))


    #buttons && pit info
    bprWrap = tk.Frame(sprintWindow, bg=background)
    bprWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(15, 20))

    #PIT INFO
    
    pitInfo = tk.Frame(bprWrap, bg=background, highlightbackground=accent, highlightthickness=1)
    pitInfo.pack(fill=tk.X, side=tk.TOP)

    pitInfoLabel = tk.Label(pitInfo, width=24, bg=background, text="#Pit Info", fg="white")
    pitInfoLabel.config(font=(fontType, 18))
    pitInfoLabel.pack()

    driveTimeWrap = tk.Frame(pitInfo, bg=background)
    driveTimeWrap.pack(side=tk.TOP, expand=True)

    driveTime = tk.Label(driveTimeWrap, text="D.T. Time", bg=background, fg="white", height=3)
    driveTime.config(font=(fontType, 18))
    driveTime.pack(side=tk.LEFT)

    driveTimeValue = tk.Entry(driveTimeWrap, width=8)
    driveTimeValue.pack(side=tk.LEFT, padx=(26, 5))

    seconds = tk.Label(driveTimeWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    tyreChangeWrap = tk.Frame(pitInfo, bg=background)
    tyreChangeWrap.pack(side=tk.TOP, expand=True)

    tyreChange = tk.Label(tyreChangeWrap, text="Tyre Change \n Time ",  bg=background, fg="white", height=3)
    tyreChange.config(font=(fontType, 15))
    tyreChange.pack(side=tk.LEFT, padx=(3, 7))

    tyreChangeValue = tk.Entry(tyreChangeWrap, width=8, fg="black")
    tyreChangeValue.pack(padx=(2, 5), side=tk.LEFT)

    seconds = tk.Label(tyreChangeWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    wearWrap = tk.Frame(pitInfo, bg=background)
    wearWrap.pack(side=tk.TOP, expand=True)

    tyreWar = tk.Label(wearWrap, text="Tyre Wear", bg=background, fg="white", height=3)
    tyreWar.config(font=(fontType, 18))
    tyreWar.pack(side=tk.LEFT, padx=(3, 15))

    wearValue = tk.Entry(wearWrap, width=8, fg="black")
    wearValue.pack(side=tk.LEFT, padx=(0, 27))

    #SELECT PRESET
    def carSelectwind():
        def trackSelectwind(car):
            def insertdata(track):
                #DATA INPUT
                inifilename=curentpath+car+".ini"
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
                tyreChangeValue.delete(0,tk.END)
                tyreChangeValue.insert(0, data[4])
                trackSelectWindow.destroy()

            #TRACK SELECT
            carSelectWindow.destroy()
            
            trackSelectWindow = tk.Tk()
            trackSelectWindow['bg']=background
            trackSelectWindow.title("SSG+")
            trackSelectWindow.geometry("+400+200")

            trackfile = curentpath + car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackSelectLabel = tk.Label(trackSelectWindow, text="Select your track", bg=background, fg="#cccccc", bd=0, highlightcolor="#00FF00")
            trackSelectLabel.config(font=(fontType, 18))
            trackSelectLabel.pack(side=tk.TOP, pady=(20, 0))

            trackSelectWrap = tk.Frame(trackSelectWindow, bg=background, highlightbackground=accent, highlightthickness=1)
            trackSelectWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

            for y in trackList: 
                trackfilename=y
                trackButtonName=y
                TrackSelect = tk.Button(trackSelectWrap, bg=foreground, fg="#cccccc", activebackground=accent, activeforeground="white", bd=1, text=trackButtonName, command= lambda trackfilename=trackfilename : insertdata(trackfilename))
                TrackSelect.config(font=(fontType, 13))
                TrackSelect.pack(side=tk.TOP, pady=10, padx=20)
            
        #CAR SELECT
        
        carSelectWindow = tk.Tk()
        carSelectWindow['bg']=background
        carSelectWindow.title("SSG+")
        carSelectWindow.geometry("+400+200")

        carSelectLabel = tk.Label(carSelectWindow, text="Select the car", bg=background, fg="white")
        carSelectLabel.config(font=(fontType, 18))
        carSelectLabel.pack(side=tk.TOP, pady=(20,0))
        
        carSelecWrap = tk.Frame(carSelectWindow, bg=background, highlightbackground=accent, highlightthickness=1)
        carSelecWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()
        
        for x in carList: 
            carbuttonname=x
            carfilename=x
            carselect = tk.Button(carSelecWrap, bg=foreground, fg="#cccccc", activebackground=accent, activeforeground="white", bd=1, text=carbuttonname, command=lambda carfilename=carfilename :trackSelectwind(carfilename))
            carselect.config(font=(fontType, 13))
            carselect.pack(side=tk.TOP, pady=10, padx=30)

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
                        inputWindow = tk.Tk()
                        inputWindow['bg']=background
                        inputWindow.title("Input Window")
                        inputWindow.geometry("+400+200")

                        inputTitle = tk.Label(inputWindow, text="Input your preset's data", bg=background, fg="white")
                        inputTitle.config(font=(fontType, 18))
                        inputTitle.pack(side=tk.TOP, pady=30)

                        dataWrap = tk.Frame(inputWindow, highlightbackground=accent, highlightthickness=1, bg=background)
                        dataWrap.pack(expand=True, padx=25, pady=(0, 25))

                        fuelTankWrap = tk.Frame(dataWrap, bg=background)
                        fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputFuelTank = tk.Label(fuelTankWrap, text="Fuel Tank Size", fg="white", bg=background)
                        inputFuelTank.config(font=(fontType, 18))
                        inputFuelTank.pack(side = tk.LEFT, padx=(20, 30))

                        inputfueltankvalue = tk.Entry(fuelTankWrap, width=12, bg="white")
                        inputfueltankvalue.pack(side=tk.LEFT, padx=(0, 5))

                        liters = tk.Label(fuelTankWrap, text="Liters", bg=background, fg="white")
                        liters.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))

                        fuelConsWrap = tk.Frame(dataWrap, bg=background)
                        fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputFuelCons = tk.Label(fuelConsWrap, text="Fuel Consumption", fg="white", bg=background)
                        inputFuelCons.config(font=(fontType, 18))
                        inputFuelCons.pack(side=tk.LEFT, padx=(0, 10))

                        inputfuelconsvalue = tk.Entry(fuelConsWrap, width=12, bg="white")
                        inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=(5, 5))

                        lperlap = tk.Label(fuelConsWrap, text="L/Lap", fg="white", bg=background)
                        lperlap.pack(side=tk.LEFT, fill=tk.Y)

                        DTWrap = tk.Frame(dataWrap, bg=background)
                        DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputDriveTime = tk.Label(DTWrap, text="D.T. Time", bg=background, fg="white")
                        inputDriveTime.config(font=(fontType, 18))
                        inputDriveTime.pack(side=tk.LEFT, padx=(42, 27))

                        inputdriveTimevalue = tk.Entry(DTWrap, width=12)
                        inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 5))

                        seconds = tk.Label(DTWrap, text="sec", bg=background, fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        refuelWrap = tk.Frame(dataWrap, bg=background)
                        refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                        inputRefuelTime = tk.Label(refuelWrap, bg=background, fg="white", text="Refuel Time")
                        inputRefuelTime.config(font=(fontType, 18))
                        inputRefuelTime.pack(side=tk.LEFT, padx=(27, 44))

                        inputRefuelTimeValue = tk.Entry(refuelWrap, width=12)
                        inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 5))

                        seconds = tk.Label(refuelWrap, text="sec", bg=background, fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        tyreWrap = tk.Frame(dataWrap, bg=background)
                        tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=15)

                        inputTyreChange = tk.Label(tyreWrap, text="Tyre Change \n Time ",  bg=background, fg="white", height=2)
                        inputTyreChange.config(font=(fontType, 15))
                        inputTyreChange.pack(side=tk.LEFT, padx=(35, 45))

                        inputTyreChangeValue = tk.Entry(tyreWrap, width=12, fg="black")
                        inputTyreChangeValue.pack(padx=(0, 5), side=tk.LEFT)

                        seconds = tk.Label(tyreWrap, text="sec", bg=background, fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        dataSubmit = tk.Button(inputWindow, text="Submit", activebackground=accent, activeforeground="white", background=foreground, fg="#cccccc", height=2, width=10, bd=1, command=datainiwrite)
                        dataSubmit.config(font=(fontType, 13))
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
                
                chooseTrackPresetWindow = tk.Tk()
                chooseTrackPresetWindow['bg']=background
                chooseTrackPresetWindow.title("SSG+ Choose Track")
                chooseTrackPresetWindow.geometry("300x300+400+200")
                
                chooseTrackLabel = tk.Label(chooseTrackPresetWindow, text="Choose a track for \nyour preset", bg=background, fg="white")
                chooseTrackLabel.config(font=(fontType, 18))
                chooseTrackLabel.pack(side=tk.TOP, expand=True)

                trackpresetvalue = tk.Entry(chooseTrackPresetWindow, width=15)
                trackpresetvalue.config(font=(fontType, 14))
                trackpresetvalue.pack(side=tk.TOP, expand=True)
                
                trackpresetsendbut = tk.Button(chooseTrackPresetWindow, text="Next", height=2, bg=foreground, fg="#cccccc", width=7, activebackground=accent, activeforeground="white", command=lambda:tracksectioncheck(str(trackpresetvalue.get()).replace(" ", "")))
                trackpresetsendbut.config(font=(fontType, 14))
                trackpresetsendbut.pack(side=tk.TOP, expand=True)
            
            if len(str(carpresetvalue.get())) < 2:
                error("Car name is invalid")
                exit()

            carfilename = curentpath + z+".ini"
            
            try:
                open(carfilename, "x")
                carlistfile = open("CARS.txt", "a")
                carlistfile.write(z+space)
                choosetrackpreset()
            except:
                choosetrackpreset()


        createCarPreset = tk.Tk()
        createCarPreset['bg']=background
        createCarPreset.title("SSG+ Create Preset")
        createCarPreset.geometry("300x300+400+200")

        selectCarLabel = tk.Label(createCarPreset, bg=background, fg="white", text="Choose a car for \nyour preset")
        selectCarLabel.config(font=(fontType, 18))
        selectCarLabel.pack(side=tk.TOP, expand=True)
        
        carpresetvalue = tk.Entry(createCarPreset, width=15)
        carpresetvalue.config(font=(fontType, 14))
        carpresetvalue.pack(side=tk.TOP, expand=True)

        carpresetsendbut = tk.Button(createCarPreset, text="Next", height=2, width=7, bg=foreground, fg="#cccccc", activebackground=accent, activeforeground="white", command=lambda:filecheck(str(carpresetvalue.get()).replace(" ", "")))
        carpresetsendbut.config(font=(fontType, 14))
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
                inputWindow = tk.Tk()
                inputWindow['bg']=background
                inputWindow.title("Input Window")
                inputWindow.geometry("+400+200")

                inputTitle = tk.Label(inputWindow, text="Input your preset's data", bg=background, fg="white")
                inputTitle.config(font=(fontType, 18))
                inputTitle.pack(side=tk.TOP, pady=30)

                dataWrap = tk.Frame(inputWindow, highlightbackground=accent, highlightthickness=1, bg=background)
                dataWrap.pack(expand=True, padx=25, pady=(0, 25))

                fuelTankWrap = tk.Frame(dataWrap, bg=background)
                fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputFuelTank = tk.Label(fuelTankWrap, text="Fuel Tank Size", fg="white", bg=background)
                inputFuelTank.config(font=(fontType, 18))
                inputFuelTank.pack(side = tk.LEFT, padx=(20, 30))

                inputfueltankvalue = tk.Entry(fuelTankWrap, width=12, bg="white")
                inputfueltankvalue.pack(side=tk.LEFT, padx=(0, 5))

                liters = tk.Label(fuelTankWrap, text="Liters", bg=background, fg="white")
                liters.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))

                fuelConsWrap = tk.Frame(dataWrap, bg=background)
                fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputFuelCons = tk.Label(fuelConsWrap, text="Fuel Consumption", fg="white", bg=background)
                inputFuelCons.config(font=(fontType, 18))
                inputFuelCons.pack(side=tk.LEFT, padx=(0, 10))

                inputfuelconsvalue = tk.Entry(fuelConsWrap, width=12, bg="white")
                inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=(5, 5))

                lperlap = tk.Label(fuelConsWrap, text="L/Lap", fg="white", bg=background)
                lperlap.pack(side=tk.LEFT, fill=tk.Y)

                DTWrap = tk.Frame(dataWrap, bg=background)
                DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputDriveTime = tk.Label(DTWrap, text="D.T. Time", bg=background, fg="white")
                inputDriveTime.config(font=(fontType, 18))
                inputDriveTime.pack(side=tk.LEFT, padx=(42, 27))

                inputdriveTimevalue = tk.Entry(DTWrap, width=12)
                inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 5))

                seconds = tk.Label(DTWrap, text="sec", bg=background, fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                refuelWrap = tk.Frame(dataWrap, bg=background)
                refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

                inputRefuelTime = tk.Label(refuelWrap, bg=background, fg="white", text="Refuel Time")
                inputRefuelTime.config(font=(fontType, 18))
                inputRefuelTime.pack(side=tk.LEFT, padx=(27, 44))

                inputRefuelTimeValue = tk.Entry(refuelWrap, width=12)
                inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 5))

                seconds = tk.Label(refuelWrap, text="sec", bg=background, fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                tyreWrap = tk.Frame(dataWrap, bg=background)
                tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=15)

                inputTyreChange = tk.Label(tyreWrap, text="Tyre Change \n Time ",  bg=background, fg="white", height=2)
                inputTyreChange.config(font=(fontType, 15))
                inputTyreChange.pack(side=tk.LEFT, padx=(35, 45))

                inputTyreChangeValue = tk.Entry(tyreWrap, width=12, fg="black")
                inputTyreChangeValue.pack(padx=(0, 5), side=tk.LEFT)

                seconds = tk.Label(tyreWrap, text="sec", bg=background, fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                dataSubmit = tk.Button(inputWindow, text="Submit", activebackground=accent, activeforeground="white", background=foreground, fg="#cccccc", height=2, width=10, bd=1, command=datainiwrite)
                dataSubmit.config(font=(fontType, 13))
                dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

                inputWindow.mainloop()
            carfilename = curentpath + car+".ini"
            
            editpresetcarwindow.destroy()
            
            editPresetTrackWindow = tk.Tk()
            editPresetTrackWindow['bg']=background
            editPresetTrackWindow.title("SSG+")
            editPresetTrackWindow.geometry("+400+200")
            
            trackfile = curentpath + car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackEditLabel = tk.Label(editPresetTrackWindow, text="Select what track you want to edit", fg="White", bg=background)
            trackEditLabel.config(font=(fontType, 18))
            trackEditLabel.pack(side=tk.TOP, pady=(20, 0))

            trackWrap = tk.Frame(editPresetTrackWindow, bg=background, highlightbackground=accent, highlightthickness=1)
            trackWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

            for y in trackList: 
                trackButtonName=y
                trackEditSelect = tk.Button(trackWrap, text=trackButtonName, bg=foreground, fg="#cccccc", activebackground=accent, activeforeground="white", command=lambda y=y :presetInputWindow(y))
                trackEditSelect.config(font=(fontType, 13))
                trackEditSelect.pack(side=tk.TOP, pady=10, padx=20)

        editpresetcarwindow = tk.Tk() 
        editpresetcarwindow['bg']=background
        editpresetcarwindow.title("SSG+ Edit preset")
        editpresetcarwindow.geometry("+400+200")
        
        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()

        carEditLabel = tk.Label(editpresetcarwindow, text="Select which preset \nyou want to edit", bg=background, fg="white")
        carEditLabel.config(font=(fontType, 18))
        carEditLabel.pack(side=tk.TOP, pady=(20, 0))

        carWrap = tk.Frame(editpresetcarwindow, background=background, highlightbackground=accent, highlightthickness=1)
        carWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)
        
        for x in carList: 
            carbuttonname=x
            carselect = tk.Button(carWrap, text=carbuttonname, bg=foreground, fg="#cccccc", activebackground=accent, activeforeground="white", command=lambda x=x :editpresettrack(x))
            carselect.config(font=(fontType, 13))
            carselect.pack(side=tk.TOP, pady=10, padx=20)

    #PRESET BUTTONS

    newpreset = tk.Button(presets, text="New Preset",command=createnewpreset,fg="#cccccc" ,bg=foreground, activebackground=accent, activeforeground="white", bd=1)
    newpreset.config(font=(fontType, 12))
    newpreset.pack(side=tk.LEFT, padx=0, pady=27, expand=True)

    carselectbut = tk.Button(presets, text="Select preset",command=carSelectwind,fg="#cccccc" ,bg=foreground, activebackground=accent, activeforeground="white", bd=1)
    carselectbut.config(font=(fontType, 12))
    carselectbut.pack(side=tk.LEFT, pady=27, padx=0, expand=True)

    editpresetbut = tk.Button(presets, text="Edit Preset",command=editpresetcar,fg="#cccccc" ,bg=foreground, activebackground=accent, activeforeground="white", bd=1)
    editpresetbut.config(font=(fontType, 12))
    editpresetbut.pack(side=tk.LEFT, padx=0, pady=27, expand=True) 


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

        outputWindow = tk.Tk()
        outputWindow.title("SSG+ Sprint Output")
        outputWindow['bg'] = background

        sprintOutput = tk.Label(outputWindow, text="Sprint Strategy", bg=background, fg="white")
        sprintOutput.config(font=(fontType, 20))
        sprintOutput.pack(expand=True, pady=(20, 0))

        outputWrap = tk.Frame(outputWindow, bg=background, highlightbackground=accent, highlightthickness=1)
        outputWrap.pack(expand=True, pady=20, padx=40)

        outputText = tk.Label(outputWrap, text=sprintText, bg=background, fg="#cccccc")
        outputText.config(font=(fontType, 15))
        outputText.pack(padx=10, pady=10)

        conversion=datetime.timedelta(seconds=fastesttime)
        sprintFastestText = "Fastest strategy is - > "+str(fasteststrat)+ " stopper = "+str(conversion) +"\n" +"Fuel needed = " + str(fuelneed)
        fastestStrategy = tk.Label(outputWrap, text=sprintFastestText, bg=background, fg="#cccccc")
        fastestStrategy.config(font=(fontType, 18))
        fastestStrategy.pack(pady=(0, 10), padx=10)

        closeOutput = tk.Button(outputWindow, text="Close Window", width=10, height=2, bg=foreground, fg="#cccccc", activebackground="red", activeforeground="white", bd=1, command=outputWindow.destroy)
        closeOutput.pack(expand=True, pady=(0, 15))

        outputWindow.mainloop()



    #OTHER BUTTONS

    documentaton = tk.Button(bprWrap, text="Readme", width=20, height=2, bg=foreground, fg="#cccccc", activebackground=accent,bd=1, command=lambda:webbrowser.open("README.md"))
    documentaton.config(font=(fontType, 14))
    documentaton.pack(expand=True, side=tk.TOP, pady=(10, 0))

    submitData = tk.Button(bprWrap, text="Calculate \n Strategy", height=2, width=20, command=submitSprint,bg="#b5b5b5", bd=1, activebackground=accent, activeforeground="white")
    submitData.config(font=(fontType, 14))
    submitData.pack(side=tk.TOP, expand=True, pady=(0, 0))

    exit = tk.Button(bprWrap, text="Exit", command=sprintWindow.destroy, width=20, height=2, bg=foreground, fg="#cccccc", activeforeground="white", activebackground="red", bd=1)
    exit.config(font=(fontType, 14))
    exit.pack(expand=True, side=tk.TOP, pady=(0, 0))