from fileinput import filename
from pickle import TRUE
import tkinter as tk
import configparser
import datetime
import webbrowser

startWindow = tk.Tk()
startWindow['bg']='#333333'
startWindow.title("SSG08")
startWindow.geometry("500x400")
space= ' '

#V0.9 BETA

def error(errortext):
    errorWindow = tk.Tk() 
    errorWindow.config(bg="#333333")
    errorWindow.geometry("200x200+400+300")
    errorWindow.title("ERROR")
    errorlabel = tk.Label(errorWindow, text = errortext, fg= "white", bg="#333333")
    errorlabel.config(font=(18))
    errorlabel.pack(pady=50)
    def windowdestroy ():
        errorWindow.destroy()
    errorbutton = tk.Button(errorWindow,text="EXIT",command = windowdestroy)
    errorbutton.pack(pady=0)

def enduranceWindow():

    startWindow.destroy()
    endWindow = tk.Tk() 
    endWindow.config(bg="#333333")
    #endWindow.geometry("1172x400")
    endWindow.title("SSG08 Endurance")

    pcrWrap = tk.Frame(endWindow, bg="#333333", width=500, height=300) #presets && car info && race info
    pcrWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=20)

    #PRESET START
    presets = tk.Frame(pcrWrap, bg="#333333", highlightbackground="#424242", highlightthickness=3)
    presets.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0, 30))

    presetsTitle = tk.Label(presets, bg="#333333", text="Presets", fg="white", width=17)
    presetsTitle.config(font=('Helvatical bold',18))
    presetsTitle.pack(pady=(15, 0))


    # tracks = tk.Frame(presets, bg="#333333")
    # tracks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    

    #cars = tk.Frame(presets, bg="#333333")
    #cars.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    


    #CARINFO START

    carinfo = tk.Frame(pcrWrap, bg="#333333", highlightbackground="#424242", highlightthickness=3)
    carinfo.pack(side=tk.BOTTOM, fill=tk.X)

    carinfoLabel = tk.Label(carinfo, bg="#333333", text="#Car Info", fg="white", width=24)
    carinfoLabel.config(font=('Helvatical bold',18))
    carinfoLabel.pack()

    tankWrap = tk.Frame(carinfo, bg="#333333")
    tankWrap.pack(fill=tk.X, side=tk.TOP, padx=20)

    fuelTank = tk.Label(tankWrap, text="Fuel Tank Size", fg="white", bg="#333333")
    fuelTank.config(font=('Helvetical bold', 18))
    fuelTank.pack(side = tk.LEFT, padx=(15, 45))

    fueltankvalue = tk.Entry(tankWrap, width=12, bg="white")
    fueltankvalue.pack(pady=20, side=tk.LEFT)

    liters = tk.Label(tankWrap, text="Liters", bg="#333333", fg="white")
    liters.pack(side=tk.LEFT, fill=tk.Y)

    consWrap = tk.Frame(carinfo, bg="#333333")
    consWrap.pack(fill=tk.X, side=tk.TOP, padx=20)

    fuelCons = tk.Label(consWrap, text="Fuel Consumption", fg="white", bg="#333333", width=16)
    fuelCons.config(font=("Helvetical bold", 18))
    fuelCons.pack(side=tk.LEFT)

    fuelconsvalue = tk.Entry(consWrap, width=12, bg="white")
    fuelconsvalue.pack(side=tk.LEFT, pady=20)

    lperlap = tk.Label(consWrap, text="L/Lap", fg="white", bg="#333333")
    lperlap.pack(side=tk.LEFT, fill=tk.Y)

    #RACE INFO START

    raceinfo = tk.Frame(pcrWrap, bg="#333333", highlightbackground="#424242", highlightthickness=3)
    raceinfo.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))

    raceinfoLabel = tk.Label(raceinfo, text="#Race Info", fg="white", width=24, bg="#333333")
    raceinfoLabel.config(font=("Helvetical bold", 18))
    raceinfoLabel.pack()

    lenghtWrap = tk.Frame(raceinfo, bg="#333333")
    lenghtWrap.pack(fill=tk.X, side=tk.TOP, padx=20)

    racelenght = tk.Label(lenghtWrap, width=10, text="Race Length", bg="#333333", fg="White", height=3)
    racelenght.config(font=("Helvetical bold", 18))
    racelenght.pack(side=tk.LEFT)

    racelenghtHourValue = tk.Entry(lenghtWrap, width=3, fg="black")
    racelenghtHourValue.pack(side=tk.LEFT)

    hours = tk.Label(lenghtWrap, text="h", bg="#333333", fg="white")
    hours.pack(side=tk.LEFT, padx=5)

    racelenghtMinuteValue = tk.Entry(lenghtWrap, width=3, fg="black")
    racelenghtMinuteValue.pack(side=tk.LEFT)

    minutes = tk.Label(lenghtWrap, text="min", bg="#333333", fg="white")
    minutes.pack(side=tk.LEFT, padx=5)
    

    laptimeWrap = tk.Frame(raceinfo, bg="#333333")
    laptimeWrap.pack(side=tk.TOP, fill=tk.X, padx=20)

    laptime = tk.Label(laptimeWrap, text="Lap Time", bg="#333333", fg="white", height=3)
    laptime.config(font=("Helvetical bold", 18))
    laptime.pack(side=tk.LEFT, padx=(4, 32))

    lapMinValue = tk.Entry(laptimeWrap, width=3, fg="black")
    lapMinValue.pack(side=tk.LEFT)

    lapMinutes = tk.Label(laptimeWrap, text="min", bg="#333333", fg="white")
    lapMinutes.pack(side=tk.LEFT, padx=5)

    lapSecondsValue = tk.Entry(laptimeWrap, width=5, fg="black")
    lapSecondsValue.pack(side=tk.LEFT, pady=20)

    seconds = tk.Label(laptimeWrap, text="sec", bg="#333333", fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)


    bpWrap = tk.Frame(endWindow, bg="#333333")#buttons && pit info
    bpWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=20)

    #PIT INFO
    
    pitInfo = tk.Frame(bpWrap, bg="#333333", highlightbackground="#424242", highlightthickness=3)
    pitInfo.pack(fill=tk.X, side=tk.TOP, pady=(10, 0))

    pitInfoLabel = tk.Label(pitInfo, width=24, bg="#333333", text="#Pit Info", fg="white")
    pitInfoLabel.config(font=("Helvetical bold", 18))
    pitInfoLabel.pack()

    driveTimeWrap = tk.Frame(pitInfo, bg="#333333")
    driveTimeWrap.pack(side=tk.TOP, fill=tk.X, padx=20)

    driveTime = tk.Label(driveTimeWrap, text="D.T. Time", bg="#333333", fg="white", height=3)
    driveTime.config(font=("Helvetical bold", 18))
    driveTime.pack(side=tk.LEFT)

    driveTimeValue = tk.Entry(driveTimeWrap, width=8)
    driveTimeValue.pack(side=tk.LEFT, padx=(26, 10))

    seconds = tk.Label(driveTimeWrap, text="sec", bg="#333333", fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    refuelWrap = tk.Frame(pitInfo, bg="#333333")
    refuelWrap.pack(side=tk.TOP, fill=tk.X)

    refuelTime = tk.Label(refuelWrap, bg="#333333", fg="white", text="Refuel Time", height=3)
    refuelTime.config(font=("Helvetical bold", 17))
    refuelTime.pack(side=tk.LEFT, padx=(20, 11))

    refuelTimeValue = tk.Entry(refuelWrap, width=8)
    refuelTimeValue.pack(side=tk.LEFT, padx=(0, 10))

    seconds = tk.Label(refuelWrap, text="sec", bg="#333333", fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    tyreChangeWrap = tk.Frame(pitInfo, bg="#333333")
    tyreChangeWrap.pack(side=tk.TOP, fill=tk.X)

    tyreChange = tk.Label(tyreChangeWrap, text="Tyre Change \n Time ",  bg="#333333", fg="white", height=3)
    tyreChange.config(font=("Helvetical bold", 15))
    tyreChange.pack(side=tk.LEFT, padx=(20, 11))

    tyreChangeValue = tk.Entry(tyreChangeWrap, width=8, fg="black")
    tyreChangeValue.pack(padx=(2, 10), side=tk.LEFT)

    seconds = tk.Label(tyreChangeWrap, text="sec", bg="#333333", fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    stintWrap = tk.Frame(pitInfo, bg="#333333")
    stintWrap.pack(side=tk.TOP, fill=tk.X)

    stintpertyre = tk.Label(stintWrap, text="Stint/Tyre", bg="#333333", fg="white", height=3)
    stintpertyre.config(font=("Helvetical bold", 18))
    stintpertyre.pack(side=tk.LEFT, padx=(20, 27))

    stintValue = tk.Entry(stintWrap, width=8, fg="black")
    stintValue.pack(side=tk.LEFT, padx=(0, 10))

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
            
            trackSelectWindow = tk.Tk()
            trackSelectWindow['bg']='#333333'
            trackSelectWindow.title("SSG08")
            trackSelectWindow.geometry("500x400")
            
            trackfile = car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackSelectLabel = tk.Label(trackSelectWindow, text="Select your track", bg="#333333", fg="white")
            trackSelectLabel.config(font=("Helvetical bold", 18))
            trackSelectLabel.pack(side=tk.TOP, pady=(20, 0))

            trackSelectWrap = tk.Frame(trackSelectWindow, bg="#333333", highlightbackground="#424242", highlightthickness=3)
            trackSelectWrap.pack(side=tk.TOP, pady=(20, 100), padx=100)

            for y in trackList: 
                trackfilename=y
                trackButtonName="Select "+y
                TrackSelect = tk.Button(trackSelectWrap, bg="#d1d1d1", fg="#424242", text=trackButtonName, command= lambda trackfilename=trackfilename : insertdata(trackfilename))
                TrackSelect.pack(side=tk.TOP, pady=10, padx=20)
            
        #CAR SELECT
        
        carSelectWindow = tk.Tk()
        carSelectWindow['bg']='#333333'
        carSelectWindow.title("SSG08")

        carSelectLabel = tk.Label(carSelectWindow, text="Select the car", bg="#333333", fg="white")
        carSelectLabel.config(font=("Helvetical bold", 18))
        carSelectLabel.pack(side=tk.TOP, pady=(20,0))
        
        carSelecWrap = tk.Frame(carSelectWindow, bg="#333333", highlightbackground="#424242", highlightthickness=3)
        carSelecWrap.pack(side=tk.TOP, pady=(20, 100), padx=100)

        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()
        
        for x in carList: 
            carbuttonname="Select "+x
            carfilename=x
            carselect = tk.Button(carSelecWrap, bg="#d1d1d1", fg="#424242", text=carbuttonname,command=lambda carfilename=carfilename :trackSelectwind(carfilename))
            carselect.pack(side=tk.TOP, pady=10, padx=20)

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
                            refuelTimeValue.delete(0,tk.END)   
                            refuelTimeValue.insert(0, inputRefuelTimeValue.get())
                            config.set(trackname, "tyrechangetime", inputTyreChangeValue.get())   
                            tyreChangeValue.delete(0,tk.END)
                            tyreChangeValue.insert(0, inputTyreChangeValue.get())

                            inputWindow.destroy()

                            with open(carfilename, "w") as config_file:
                                config.write(config_file)
                            return 0

                        chooseTrackPresetWindow.destroy()
                        inputWindow = tk.Tk()
                        inputWindow['bg']='#333333'
                        inputWindow.title("Input Window")

                        inputTitle = tk.Label(inputWindow, text="Input your preset's data", bg="#333333", fg="white")
                        inputTitle.config(font=("Helvetical bold", 18))
                        inputTitle.pack(side=tk.TOP, pady=20)

                        dataWrap = tk.Frame(inputWindow, highlightbackground="#424242", highlightthickness=3, bg="#333333")
                        dataWrap.pack(expand=True, padx=25, pady=25)

                        fuelTankWrap = tk.Frame(dataWrap, bg="#333333")
                        fuelTankWrap.pack(side=tk.TOP, fill=tk.X)

                        inputFuelTank = tk.Label(fuelTankWrap, text="Fuel Tank Size", fg="white", bg="#333333")
                        inputFuelTank.config(font=('Helvetical bold', 18))
                        inputFuelTank.pack(side = tk.LEFT, padx=(15, 45))

                        inputfueltankvalue = tk.Entry(fuelTankWrap, width=12, bg="white")
                        inputfueltankvalue.pack(pady=20, side=tk.LEFT)

                        liters = tk.Label(fuelTankWrap, text="Liters", bg="#333333", fg="white")
                        liters.pack(side=tk.LEFT, fill=tk.Y)

                        fuelConsWrap = tk.Frame(dataWrap, bg="#333333")
                        fuelConsWrap.pack(side=tk.TOP, fill=tk.X)

                        inputFuelCons = tk.Label(fuelConsWrap, text="Fuel Consumption", fg="white", bg="#333333", width=16)
                        inputFuelCons.config(font=("Helvetical bold", 18))
                        inputFuelCons.pack(side=tk.LEFT)

                        inputfuelconsvalue = tk.Entry(fuelConsWrap, width=12, bg="white")
                        inputfuelconsvalue.pack(side=tk.LEFT, pady=20)

                        lperlap = tk.Label(fuelConsWrap, text="L/Lap", fg="white", bg="#333333")
                        lperlap.pack(side=tk.LEFT, fill=tk.Y)

                        DTWrap = tk.Frame(dataWrap, bg="#333333")
                        DTWrap.pack(side=tk.TOP, fill=tk.X)

                        inputDriveTime = tk.Label(DTWrap, text="D.T. Time", bg="#333333", fg="white", height=3)
                        inputDriveTime.config(font=("Helvetical bold", 18))
                        inputDriveTime.pack(side=tk.LEFT, padx=(15, 57))

                        inputdriveTimevalue = tk.Entry(DTWrap, width=8)
                        inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 10))

                        seconds = tk.Label(DTWrap, text="sec", bg="#333333", fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        refuelWrap = tk.Frame(dataWrap, bg="#333333")
                        refuelWrap.pack(side=tk.TOP, fill=tk.X)

                        inputRefuelTime = tk.Label(refuelWrap, bg="#333333", fg="white", text="Refuel Time", height=3)
                        inputRefuelTime.config(font=("Helvetical bold", 18))
                        inputRefuelTime.pack(side=tk.LEFT, padx=(18, 63))

                        inputRefuelTimeValue = tk.Entry(refuelWrap, width=8)
                        inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 10))

                        seconds = tk.Label(refuelWrap, text="sec", bg="#333333", fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        tyreWrap = tk.Frame(dataWrap, bg="#333333")
                        tyreWrap.pack(side=tk.TOP, fill=tk.X)

                        inputTyreChange = tk.Label(tyreWrap, text="Tyre Change \n Time ",  bg="#333333", fg="white", height=3)
                        inputTyreChange.config(font=("Helvetical bold", 15))
                        inputTyreChange.pack(side=tk.LEFT, padx=(18, 63))

                        inputTyreChangeValue = tk.Entry(tyreWrap, width=8, fg="black")
                        inputTyreChangeValue.pack(padx=(2, 10), side=tk.LEFT)

                        seconds = tk.Label(tyreWrap, text="sec", bg="#333333", fg="white")
                        seconds.pack(fill=tk.Y, side=tk.LEFT)

                        dataSubmit = tk.Button(inputWindow, text="Submit",command = datainiwrite)
                        dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

                        inputWindow.mainloop()
                    
                    config = configparser.ConfigParser()
                    config.read(carfilename)
                    config.add_section(trackname)
                    
                    with open(carfilename, "w") as config_file:
                        config.write(config_file)
                   
                    cartrackfilename = z + "T.txt"
                    cartrackfile = open (cartrackfilename, "a")
                    cartrackfile.write(trackname+space)
                    cartrackfile.close()
                    presetInputWindow()
                    chooseTrackPresetWindow.destroy()

                
                createCarPreset.destroy()
                
                chooseTrackPresetWindow = tk.Tk()
                chooseTrackPresetWindow['bg']='#333333'
                chooseTrackPresetWindow.title("SSG08 Choose Track")
                chooseTrackPresetWindow.geometry("500x250")
                
                chooseTrackLabel = tk.Label(chooseTrackPresetWindow, text="Choose a track for \nyour preset's track", bg="#333333", fg="white")
                chooseTrackLabel.config(font=("Helvetical bold", 18))
                chooseTrackLabel.pack(side=tk.LEFT, expand=True)

                trackpresetvalue = tk.Entry(chooseTrackPresetWindow, width=20)
                trackpresetvalue.pack(side=tk.LEFT, expand=True)
                
                trackpresetsendbut = tk.Button(chooseTrackPresetWindow, text="Next", height=3, bg="#424242", fg="#d1d1d1", width=10, command=lambda:tracksectioncheck(str(trackpresetvalue.get())))
                trackpresetsendbut.pack(side=tk.BOTTOM, pady=(0,20), padx=(0,20))
            
            carfilename = z+".ini"
            
            try:
                open(carfilename, "x")
                carlistfile = open("CARS.txt", "a")
                carlistfile.write(z+space)
                choosetrackpreset()
            except:
                choosetrackpreset()


        createCarPreset = tk.Tk()
        createCarPreset['bg']='#333333'
        createCarPreset.title("SSG08 Create Preset")
        createCarPreset.geometry("500x250")

        selectCarLabel = tk.Label(createCarPreset, bg="#333333", fg="white", text="Choose a name for \nyour preset's car")
        selectCarLabel.config(font=("Helvetical bold", 18))
        selectCarLabel.pack(side=tk.LEFT, expand=True)
        
        carpresetvalue = tk.Entry(createCarPreset, width=20)
        carpresetvalue.pack(side=tk.LEFT, expand=True)
        
        carpresetsendbut = tk.Button(createCarPreset, text="Next", height=3, width=10, bg="#424242", fg="#d1d1d1", command=lambda:filecheck(str(carpresetvalue.get())))
        carpresetsendbut.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))

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
                    refuelTimeValue.delete(0,tk.END)   
                    refuelTimeValue.insert(0, inputRefuelTimeValue.get())
                    config.set(trackname, "tyrechangetime", inputTyreChangeValue.get())   
                    tyreChangeValue.delete(0,tk.END)
                    tyreChangeValue.insert(0, inputTyreChangeValue.get())

                    inputWindow.destroy()

                    with open(carfilename, "w") as config_file:
                        config.write(config_file)
                    return 0

                editPresetTrackWindow.destroy()
                inputWindow = tk.Tk()
                inputWindow['bg']='#333333'
                inputWindow.title("Input Window")

                inputTitle = tk.Label(inputWindow, text="Input your preset's data", bg="#333333", fg="white")
                inputTitle.config(font=("Helvetical bold", 18))
                inputTitle.pack(side=tk.TOP, pady=20)

                dataWrap = tk.Frame(inputWindow, highlightbackground="#424242", highlightthickness=3, bg="#333333")
                dataWrap.pack(expand=True, padx=25, pady=25)

                fuelTankWrap = tk.Frame(dataWrap, bg="#333333")
                fuelTankWrap.pack(side=tk.TOP, fill=tk.X)

                inputFuelTank = tk.Label(fuelTankWrap, text="Fuel Tank Size", fg="white", bg="#333333")
                inputFuelTank.config(font=('Helvetical bold', 18))
                inputFuelTank.pack(side = tk.LEFT, padx=(15, 45))

                inputfueltankvalue = tk.Entry(fuelTankWrap, width=12, bg="white")
                inputfueltankvalue.pack(pady=20, side=tk.LEFT)

                liters = tk.Label(fuelTankWrap, text="Liters", bg="#333333", fg="white")
                liters.pack(side=tk.LEFT, fill=tk.Y)

                fuelConsWrap = tk.Frame(dataWrap, bg="#333333")
                fuelConsWrap.pack(side=tk.TOP, fill=tk.X)

                inputFuelCons = tk.Label(fuelConsWrap, text="Fuel Consumption", fg="white", bg="#333333", width=16)
                inputFuelCons.config(font=("Helvetical bold", 18))
                inputFuelCons.pack(side=tk.LEFT)

                inputfuelconsvalue = tk.Entry(fuelConsWrap, width=12, bg="white")
                inputfuelconsvalue.pack(side=tk.LEFT, pady=20)

                lperlap = tk.Label(fuelConsWrap, text="L/Lap", fg="white", bg="#333333")
                lperlap.pack(side=tk.LEFT, fill=tk.Y)

                DTWrap = tk.Frame(dataWrap, bg="#333333")
                DTWrap.pack(side=tk.TOP, fill=tk.X)

                inputDriveTime = tk.Label(DTWrap, text="D.T. Time", bg="#333333", fg="white", height=3)
                inputDriveTime.config(font=("Helvetical bold", 18))
                inputDriveTime.pack(side=tk.LEFT, padx=(15, 57))

                inputdriveTimevalue = tk.Entry(DTWrap, width=8)
                inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 10))

                seconds = tk.Label(DTWrap, text="sec", bg="#333333", fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                refuelWrap = tk.Frame(dataWrap, bg="#333333")
                refuelWrap.pack(side=tk.TOP, fill=tk.X)

                inputRefuelTime = tk.Label(refuelWrap, bg="#333333", fg="white", text="Refuel Time", height=3)
                inputRefuelTime.config(font=("Helvetical bold", 18))
                inputRefuelTime.pack(side=tk.LEFT, padx=(18, 63))

                inputRefuelTimeValue = tk.Entry(refuelWrap, width=8)
                inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 10))

                seconds = tk.Label(refuelWrap, text="sec", bg="#333333", fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                tyreWrap = tk.Frame(dataWrap, bg="#333333")
                tyreWrap.pack(side=tk.TOP, fill=tk.X)

                inputTyreChange = tk.Label(tyreWrap, text="Tyre Change \n Time ",  bg="#333333", fg="white", height=3)
                inputTyreChange.config(font=("Helvetical bold", 15))
                inputTyreChange.pack(side=tk.LEFT, padx=(18, 63))

                inputTyreChangeValue = tk.Entry(tyreWrap, width=8, fg="black")
                inputTyreChangeValue.pack(padx=(2, 10), side=tk.LEFT)

                seconds = tk.Label(tyreWrap, text="sec", bg="#333333", fg="white")
                seconds.pack(fill=tk.Y, side=tk.LEFT)

                dataSubmit = tk.Button(inputWindow, text="Submit",command = datainiwrite)
                dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

                inputWindow.mainloop()
            carfilename = car+".ini"
            
            editpresetcarwindow.destroy()
            
            editPresetTrackWindow = tk.Tk()
            editPresetTrackWindow['bg']='#333333'
            editPresetTrackWindow.title("SSG08")
            # editPresetTrackWindow.geometry("500x400")
            
            trackfile = car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackEditLabel = tk.Label(editPresetTrackWindow, text="Select what track you want to edit", fg="White", bg="#333333")
            trackEditLabel.config(font=("Helvetical bold", 18))
            trackEditLabel.pack(side=tk.TOP, pady=(20, 0))

            trackWrap = tk.Frame(editPresetTrackWindow, bg="#333333", highlightbackground="#424242", highlightthickness=3)
            trackWrap.pack(side=tk.TOP, pady=(20, 100), padx=100)

            for y in trackList: 
                trackButtonName="Select " + y
                trackEditSelect = tk.Button(trackWrap, text=trackButtonName, bg="#d1d1d1", fg="#424242", width=15,command=lambda y=y :presetInputWindow(y))
                trackEditSelect.pack(side=tk.TOP, pady=10, padx=20)

        editpresetcarwindow = tk.Tk() 
        editpresetcarwindow['bg']='#333333'
        editpresetcarwindow.title("SSG08 Edit preset")
        # editpresetcarwindow.geometry("500x400")
        
        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()

        carEditLabel = tk.Label(editpresetcarwindow, text="Select which preset \nyou want to edit", bg="#333333", fg="white")
        carEditLabel.config(font=("Helvetical bold", 18))
        carEditLabel.pack(side=tk.TOP, pady=(20, 0))

        carWrap = tk.Frame(editpresetcarwindow, background="#333333", highlightbackground="#424242", highlightthickness=3)
        carWrap.pack(side=tk.TOP, pady=(20, 100), padx=100)
        
        for x in carList: 
            carbuttonname="Select "+x
            carselect = tk.Button(carWrap, text=carbuttonname, bg="#424242", fg="#d1d1d1", width=15,command=lambda x=x :editpresettrack(x))
            carselect.pack(side=tk.TOP, pady=10, padx=20)

    #BUTOANE PRESET 

    newpreset = tk.Button(presets, text="New Preset",command=createnewpreset,fg="#d1d1d1" ,bg="#424242")
    newpreset.pack(side=tk.LEFT, padx=0, pady=15, expand=True)

    carselectbut = tk.Button(presets, text="Select preset",command=carSelectwind,fg="#d1d1d1" ,bg="#424242")
    carselectbut.pack(side=tk.LEFT, pady=15, padx=0, expand=True)

    editpresetbut = tk.Button(presets, text="Edit Preset",command=editpresetcar,fg="#d1d1d1" ,bg="#424242")
    editpresetbut.pack(side=tk.LEFT, padx=0, pady=15, expand=True) 


    #CALCULATE STRATEGY
    def submitEndurance():
        
        foutput = open('output.txt', 'w')
        
        #car info
        try:
            fueltank = float(fueltankvalue.get())
        except:
            error("Fuel Tank variable\nis not correct")
            return 0

        try:
            fuelcons = float(fuelconsvalue.get())
        except:
            error("Fuel consumption value\nis not correct")
            return 0


        #race info
        try:
            racelength_h = int(racelenghtHourValue.get())
        except:
            error("Race length value\nis not correct")
            return 0
        try:
            racelength_m = int(racelenghtMinuteValue.get())
        except:
            error("Race length value\nis not correct")
            return 0
        
        try:
            laptime = float(lapMinValue.get())*60+float(lapSecondsValue.get())
        except:
            error("Laptime value\nis not correct")
            return 0

        #pit info
        try:
            dttime = float(driveTimeValue.get())
        except:
            error("DT time value\nis not correct")
            return 0
        try:
            refueltime = float(refuelTimeValue.get())
        except:
            error("Refuel time value\nis not correct")
            return 0
        try:
            tyrechangetime = float(tyreChangeValue.get())
        except:
            error("Tyre change value\nis not correct")
            return 0
        try:
            stintpertyre = int(stintValue.get())
        except:
            error("Stints/Tyre value\nis not correct")
            return 0

        #Stint calculations
        refuellitertime=refueltime/fueltank
        refuellitertime=int(refuellitertime*100)/100
        fuelleft = fueltank
        tyrestint = stintpertyre
        racelength = racelength_h*3600 + racelength_m*60
        timeleft = racelength   
        stinttime = int(fueltank/fuelcons) * laptime + dttime + refueltime + tyrechangetime
        lapcount = 0
        stintcount = 0



        #Stint info print
        conversion = datetime.timedelta(seconds=stinttime)
        textoutput = "\n- Welcome to Smart Strategy Generator - "
        foutput.write(textoutput)
        textoutput = "\nStint lenght = "+str(conversion)+"\nRefuel rate = "+str(refuellitertime)+"seconds/L \n" 
        foutput.write(textoutput)
        while timeleft>stinttime :
            stintcount += 1
            textoutput="\n\nStint #"+str(stintcount)+"\n"
            foutput.write(textoutput)
            while fuelleft>=fuelcons*2:
                fuelleft -= fuelcons
                timeleft -= laptime 
                lapcount += 1
                conversion = datetime.timedelta(seconds=timeleft)
                textoutput = "Lap : "+str(lapcount)+"| Time left : "+str(conversion)+"| Fuel left : "+str(round(fuelleft, 2))
                foutput.write(textoutput)
                foutput.write("\n")

            fuelleft -= fuelcons
            timeleft -= laptime 
            lapcount += 1


            if tyrestint==1:
                tyrestint = stintpertyre
                timeleft -= tyrechangetime
                
            elif tyrestint>1:
                tyrestint -= 1

                
            timeleft = timeleft-(dttime+refueltime)
            conversion = datetime.timedelta(seconds=timeleft)
            textoutput="PIT THIS LAP | Lap : " +str(lapcount)+" | Time left : "+str(conversion)+" | Fuel wasted : "+str(round(fuelleft, 2))
            foutput.write(textoutput)
            fuelleft = fueltank


        #Last stint calculation
        lapsleft = int(timeleft/laptime) + 1
        fuelleft = fuelcons * lapsleft
        timeleft = timeleft - int(refuellitertime*fuelleft) - dttime

        #Last stint generator
        stintcount += 1
        textoutput="\nStint #"+str(stintcount)+"\n"
        foutput.write(textoutput)
        while timeleft>laptime :
            fuelleft -= fuelcons
            timeleft -= laptime 
            lapcount += 1
            conversion = datetime.timedelta(seconds=timeleft)
            textoutput="Lap : "+str(lapcount)+"| Time left :"+str(conversion)+"| Fuel left : "+str(round(fuelleft, 2))
            foutput.write(textoutput)
            foutput.write("\n")

        #Last lap 
        fuelleft -= fuelcons
        timeleft -= laptime 
        lapcount += 1
        textoutput="Lap : "+str(lapcount)+"| Fuel left : "+str(round(fuelleft, 2))+"| Race Finished!"
        foutput.write(textoutput)
        webbrowser.open("output.txt")


    #OTHER BUTTONS
    submitData = tk.Button(bpWrap, text="Calculate \n Strategy", height=2, command=submitEndurance,bg="#b5b5b5")
    submitData.pack(expand=True, side=tk.LEFT, padx=5)

    documentatie = tk.Button(bpWrap, text="Readme", width=8, height=2, bg="#424242", fg="#d1d1d1", command=lambda:webbrowser.open("README.md"))
    documentatie.pack(expand=True, side=tk.LEFT, padx=5)

    exit = tk.Button(bpWrap, text="Exit", command=endWindow.destroy, width=8, height=2, bg="#424242", fg="#d1d1d1")
    exit.pack(expand=True, side=tk.LEFT, padx=5)


canvas = tk.Canvas(startWindow, width = 300, height = 150, bg="#333333", highlightbackground="#333333")      
canvas.pack(pady=(60,0))      
img = tk.PhotoImage(file="SSG.png")      
canvas.create_image(150,75, image=img)    

endurance = tk.Button(startWindow, text="START", height=2, width=15, bg="#2e2e2e", fg="#b5b5b5", command=enduranceWindow)
endurance.config(font=("Helvetical bold",15))
endurance.pack(expand=True)

startWindow.mainloop()
