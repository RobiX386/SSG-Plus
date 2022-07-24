import configparser
import os
from select import select
import tkinter as tk
# from tkcalendar import Calendar

curentpath = os.getcwd() + "\presets"+"\\"

background="#222629"
foreground="#474b4f"
accent="#86c232"
textcolor="#cccccc"
buttonColor="#171a1c"

config= configparser.ConfigParser()
config.read("events.ini")

window = tk.Tk()
window['bg']="#666666"
window.title("SSG+")
window.geometry("500x400+500+200")


labelEventName = tk.Label(window, text=config.get('NAME','name'), fg="White", bg=background)
labelEventName.pack(side=tk.TOP, pady=(20, 0))


def funcDriver():
    def closeFunction():
        try:
            config.add_section('DRIVERS')
            config.set("DRIVERS",entryDriverName.get(),str(entryDriverLaptime.get()))
            with open('events.ini', 'w') as configfile:
                config.write(configfile)
            windowAddDriver.destroy()
        except:
            config.set("DRIVERS",entryDriverName.get(),str(entryDriverLaptime.get()))
            with open('events.ini', 'w') as configfile:
                config.write(configfile)
            windowAddDriver.destroy()

    windowAddDriver = tk.Tk()
    windowAddDriver['bg']="#666666"
    windowAddDriver.title("SSG+")
    windowAddDriver.geometry("300x200+500+200")

    entryDriverName = tk.Entry(windowAddDriver)
    entryDriverName.pack()

    entryDriverLaptime = tk.Entry(windowAddDriver)
    entryDriverLaptime.pack()

    butWriteData = tk.Button(windowAddDriver,text="Add Data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=closeFunction)
    butWriteData.pack()

def funcRaceData():
    def funcImportCarData():
        def funcImportTrackData(car):
            def funcWriteData(track):

                editPresetTrackWindow.destroy()

                dataread = configparser.ConfigParser()
                dataread.read(carfilename)

                try:
                    config.add_section('RACEDATA')
                    config.set('RACEDATA','fueltank',dataread.get(track,'fueltank'))
                    config.set('RACEDATA','fuelcons',dataread.get(track,'fuelcons'))
                    config.set('RACEDATA','dttime',dataread.get(track,'dttime'))
                    config.set('RACEDATA','refueltime',dataread.get(track,'refueltime'))
                except:
                    config.set('RACEDATA','fueltank',dataread.get(track,'fueltank'))
                    config.set('RACEDATA','fuelcons',dataread.get(track,'fuelcons'))
                    config.set('RACEDATA','dttime',dataread.get(track,'dttime'))
                    config.set('RACEDATA','refueltime',dataread.get(track,'refueltime'))

                with open("events.ini","w") as file_object:
                    config.write(file_object)

            carfilename = curentpath+car+".ini"
            
            windowImportCarData.destroy()
            
            editPresetTrackWindow = tk.Tk()
            editPresetTrackWindow['bg']=background
            editPresetTrackWindow.title("SSG+")
            editPresetTrackWindow.geometry("+400+200")
            
            trackfile = curentpath + car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackEditLabel = tk.Label(editPresetTrackWindow, text="Select which track \n you want to edit", fg="White", bg=background)
            trackEditLabel.pack(side=tk.TOP, pady=(20, 0))

            trackWrap = tk.Frame(editPresetTrackWindow, bg=background, highlightbackground=accent, highlightthickness=1)
            trackWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

            for y in trackList: 
                trackButtonName=y
                trackEditSelect = tk.Button(trackWrap, text=trackButtonName, bg=foreground, fg=textcolor, activebackground=accent, activeforeground="white", command=lambda y=y :funcWriteData(y))
                trackEditSelect.pack(side=tk.TOP, pady=10, padx=20)

        windowAddData.destroy()

        windowImportCarData = tk.Tk()
        windowImportCarData['bg']="#666666"
        windowImportCarData.title("SSG+")
        windowImportCarData.geometry("300x200+500+200") 
        readcars = open("CARS.txt", "r")
        carList = readcars.readline() 
        carList = carList.split()
        for x in carList: 
            carbuttonname=x
            carselect = tk.Button(windowImportCarData, text=carbuttonname, bg=foreground, fg=textcolor, activebackground=accent, activeforeground="white", command=lambda x=x :funcImportTrackData(x))
            carselect.pack(side=tk.TOP, pady=10, padx=20)



    windowAddData = tk.Tk()
    windowAddData['bg']="#666666"
    windowAddData.title("SSG+")
    windowAddData.geometry("600x400+500+200")

    inputTitle = tk.Label(windowAddData, text="Input your preset's data", bg=background, fg="white")
    inputTitle.pack(side=tk.TOP, pady=30)

    dataWrap = tk.Frame(windowAddData, highlightbackground=accent, highlightthickness=1, bg=background)
    dataWrap.pack(expand=True, padx=25, pady=(0, 25))

    fuelTankWrap = tk.Frame(dataWrap, bg=background)
    fuelTankWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

    inputFuelTank = tk.Label(fuelTankWrap, text="Fuel Tank Size", fg="white", bg=background)
    inputFuelTank.pack(side = tk.LEFT, padx=(20, 30))

    inputfueltankvalue = tk.Entry(fuelTankWrap, width=12, bg="white")
    inputfueltankvalue.pack(side=tk.LEFT, padx=(0, 5))

    liters = tk.Label(fuelTankWrap, text="Liters", bg=background, fg="white")
    liters.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))

    fuelConsWrap = tk.Frame(dataWrap, bg=background)
    fuelConsWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

    inputFuelCons = tk.Label(fuelConsWrap, text="Fuel Consumption", fg="white", bg=background)
    inputFuelCons.pack(side=tk.LEFT, padx=(0, 10))

    inputfuelconsvalue = tk.Entry(fuelConsWrap, width=12, bg="white")
    inputfuelconsvalue.pack(side=tk.LEFT, pady=0, padx=(5, 5))

    lperlap = tk.Label(fuelConsWrap, text="L/Lap", fg="white", bg=background)
    lperlap.pack(side=tk.LEFT, fill=tk.Y)

    DTWrap = tk.Frame(dataWrap, bg=background)
    DTWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

    inputDriveTime = tk.Label(DTWrap, text="D.T. Time", bg=background, fg="white")
    inputDriveTime.pack(side=tk.LEFT, padx=(42, 27))

    inputdriveTimevalue = tk.Entry(DTWrap, width=12)
    inputdriveTimevalue.pack(side=tk.LEFT, padx=(26, 5))

    seconds = tk.Label(DTWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    refuelWrap = tk.Frame(dataWrap, bg=background)
    refuelWrap.pack(side=tk.TOP, expand=True, pady=10, padx=15)

    inputRefuelTime = tk.Label(refuelWrap, bg=background, fg="white", text="Refuel Time")
    inputRefuelTime.pack(side=tk.LEFT, padx=(27, 44))

    inputRefuelTimeValue = tk.Entry(refuelWrap, width=12)
    inputRefuelTimeValue.pack(side=tk.LEFT, padx=(0, 5))

    seconds = tk.Label(refuelWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    tyreWrap = tk.Frame(dataWrap, bg=background)
    tyreWrap.pack(side=tk.TOP, expand=True, pady=5, padx=15)

    inputTyreChange = tk.Label(tyreWrap, text="Tyre Change \n Time ",  bg=background, fg="white", height=2)
    inputTyreChange.pack(side=tk.LEFT, padx=(35, 45))

    inputTyreChangeValue = tk.Entry(tyreWrap, width=12, fg="black")
    inputTyreChangeValue.pack(padx=(0, 5), side=tk.LEFT)

    seconds = tk.Label(tyreWrap, text="sec", bg=background, fg="white")
    seconds.pack(fill=tk.Y, side=tk.LEFT)

    def dataIniWrite():
        try:
            config.add_section('RACEDATA')
            config.set('RACEDATA','fueltank',inputfueltankvalue.get())
            config.set('RACEDATA','fuelcons',inputfuelconsvalue.get())
            config.set('RACEDATA','dttime',inputdriveTimevalue.get())
            config.set('RACEDATA','refueltime',inputRefuelTimeValue.get())
            config.set('RACEDATA','tyrechangetime',inputTyreChangeValue.get())

        except:
            config.set('RACEDATA','fueltank',inputfueltankvalue.get())
            config.set('RACEDATA','fuelcons',inputfuelconsvalue.get())
            config.set('RACEDATA','dttime',inputdriveTimevalue.get())
            config.set('RACEDATA','refueltime',inputRefuelTimeValue.get())
            config.set('RACEDATA','tyrechangetime',inputTyreChangeValue.get())
        
        with open("events.ini","w") as file_object:
            config.write(file_object)

        windowAddData.destroy()

    dataSubmit = tk.Button(windowAddData, text="Submit", activebackground=accent, activeforeground="white", background=foreground, fg=textcolor, height=2, width=10, bd=1, command=dataIniWrite)
    dataSubmit.pack(side=tk.BOTTOM, expand=True, pady=(0, 20))

    butImportData = tk.Button(windowAddData,text="Import Data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcImportCarData)
    butImportData.pack()

def funcChangeName():
    def funcWriteName():
        try:
            config.add_section('NAME')
            config.set('NAME','name',entryEventName.get())
        except:
            config.set('NAME','name',entryEventName.get())

        with open("events.ini","w") as file_object:
            config.write(file_object)
        
        windowChangeName.destroy()

    windowChangeName = tk.Tk()
    windowChangeName['bg']="#666666"
    windowChangeName.geometry("500x400+500+200")

    entryEventName = tk.Entry(windowChangeName)
    entryEventName.pack()

    butWriteData = tk.Button(windowChangeName,text="Add Data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcWriteName)
    butWriteData.pack()

def funcRaceInfo():
    def funcWriteInfo():
        try:
            config.add_section('EVENTINFO')
            config.set('EVENTINFO','date',entryEventdate.get())
            config.set('EVENTINFO','driver',valueinside.get())
        except:
            config.set('EVENTINFO','date',entryEventdate.get())
            config.set('EVENTINFO','driver',valueinside.get())

        with open("events.ini","w") as file_object:
            config.write(file_object)
        
        windowRaceInfo.destroy()

    windowRaceInfo = tk.Tk()
    windowRaceInfo.geometry("500x400+500+200")

    entryEventdate = tk.Entry(windowRaceInfo)
    entryEventdate.pack()

    cal = Calendar(windowRaceInfo,selectmode='day')
    cal.pack()

    def cale():
        print(cal.get_date())

    butcal = tk.Button(windowRaceInfo,text="show Data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=cale)
    butcal.pack()


    driverlist = config.options('DRIVERS')
    
    valueinside = tk.StringVar(windowRaceInfo)
    valueinside.set("Select a driver")

    optionStartDriver = tk.OptionMenu(windowRaceInfo,valueinside,*driverlist)
    optionStartDriver.pack()

    butWriteData = tk.Button(windowRaceInfo,text="Change Data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcWriteInfo)
    butWriteData.pack()

butAddDriver = tk.Button(window,text="add driver",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcDriver)
butAddDriver.pack()

butAddData = tk.Button(window,text="add data",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcRaceData)
butAddData.pack()

butChangeName = tk.Button(window,text="Change name",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcChangeName)
butChangeName.pack()

butChangeName = tk.Button(window,text="Change event info",height=2, width=15, bg=buttonColor, fg=textcolor, activebackground=accent, bd=1,command=funcRaceInfo)
butChangeName.pack()


window.mainloop()