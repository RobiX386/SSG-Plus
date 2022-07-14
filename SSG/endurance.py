from fileinput import filename
from msilib import text
import tkinter as tk
import configparser
import datetime
from turtle import width
import webbrowser
import os
import customtkinter as ctk
from errorFile import error
import sys


class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()
#Supressing known exceptions
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

space= ' '
curentpath = os.getcwd() + "\presets"+"\\"


def enduranceFunc():
    endWindow = tk.Tk() 
    endWindow.config(bg=background)
    endWindow.title("SSG+ Endurance")
    endWindow.geometry("+300+100")
    endWindow.resizable(False, False)

    pcrWrap = tk.Frame(endWindow, bg=background, width=500, height=300) #presets && car info && race info
    pcrWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(20, 15))

    #PRESET START
    presets = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    presets.pack(pady=(15, 0),side=tk.TOP, fill=tk.BOTH, expand=True)

    presetsTitle = ctk.CTkLabel(pcrWrap, fg_color=background, text="Presets", text_font=(fontType, 18), text_color=mainTextColor, width=40)
    presetsTitle.place(x=170, y=0, anchor=tk.N)

    #CARINFO START

    carinfo = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    carinfo.pack(side=tk.BOTTOM, fill=tk.X)

    carinfoLabel = ctk.CTkLabel(pcrWrap, text_font=(fontType, 18), fg_color=background, text="#Car Info", text_color=mainTextColor, width=40)
    carinfoLabel.place(x=170, y=247, anchor = tk.N)

    tankWrap = tk.Frame(carinfo, bg=background)
    tankWrap.pack(fill=tk.X, side=tk.TOP, padx=20, pady=(20, 0))

    fuelTank = ctk.CTkLabel(tankWrap, text_font=(fontType, 18), text="Fuel Tank Size", text_color=mainTextColor, fg_color=background)
    fuelTank.pack(side = tk.LEFT, padx=(0, 44))

    fueltankvalue = ctk.CTkEntry(tankWrap, width=76, height=20, border_color=entryBorderColor, fg_color=entryFg, text_color=entryTextColor, placeholder_text_color=placeholderColor, placeholder_text="Liters")
    fueltankvalue.pack(pady=20, side=tk.LEFT)

    consWrap = tk.Frame(carinfo, bg=background)
    consWrap.pack(fill=tk.X, side=tk.TOP, padx=(4, 20), pady=(0, 3))

    fuelCons = ctk.CTkLabel(consWrap, text="Fuel Consumption", text_color=mainTextColor, fg_color=background, text_font=(fontType, 18))
    fuelCons.pack(side=tk.LEFT, padx=(0, 23))

    fuelconsvalue = ctk.CTkEntry(consWrap, width=76, height=20, border_color=entryBorderColor, text_color=entryTextColor, placeholder_text="L/Lap", placeholder_text_color=placeholderColor, fg_color=entryFg)
    fuelconsvalue.pack(side=tk.LEFT, pady=20)


    #RACE INFO

    raceinfo = ctk.CTkFrame(pcrWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    raceinfo.pack(side=tk.TOP, fill=tk.X, pady=15)

    raceinfoLabel = ctk.CTkLabel(pcrWrap, text="#Race Info", text_font=(fontType, 18), text_color=mainTextColor, fg_color=background, width=40)
    raceinfoLabel.place(x=170, y=92, anchor=tk.N)

    lenghtWrap = tk.Frame(raceinfo, bg=background)
    lenghtWrap.pack(expand=True, side=tk.TOP, pady=(30, 15))

    racelenght = ctk.CTkLabel(lenghtWrap, text="Race Length", text_font=(fontType, 18), fg_color=background, text_color=mainTextColor)
    racelenght.pack(side=tk.LEFT, padx=0)

    racelenghtHourValue = ctk.CTkEntry(lenghtWrap, width=40, height=19, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="h", placeholder_text_color=placeholderColor)
    racelenghtHourValue.pack(side=tk.LEFT, padx=5)

    racelenghtMinuteValue = ctk.CTkEntry(lenghtWrap, width=40, height=19, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="min", placeholder_text_color=placeholderColor)
    racelenghtMinuteValue.pack(side=tk.LEFT, padx=5)    

    laptimeWrap = tk.Frame(raceinfo, bg=background)
    laptimeWrap.pack(side=tk.TOP, expand=True, pady=(15, 15))

    laptime = ctk.CTkLabel(laptimeWrap, text="Lap Time", fg_color=background, text_color=mainTextColor, text_font=(fontType, 18))
    laptime.pack(side=tk.LEFT, padx=(0, 15), pady=(0, 9))

    lapMinValue = ctk.CTkEntry(laptimeWrap, width=40, height=19, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="min", placeholder_text_color=placeholderColor)
    lapMinValue.pack(side=tk.LEFT, padx=5)

    lapSecondsValue = ctk.CTkEntry(laptimeWrap, width=40, height=19, fg_color=entryFg, border_color=entryBorderColor, placeholder_text="sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    lapSecondsValue.pack(side=tk.LEFT, pady=0, padx=5)

    #buttons && pit info
    bprWrap = tk.Frame(endWindow, bg=background)
    bprWrap.pack(side=tk.LEFT, fill=tk.Y, pady=40, padx=(15, 20))

    #PIT INFO
    
    pitInfo = ctk.CTkFrame(bprWrap, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
    pitInfo.pack(fill=tk.X, side=tk.TOP, pady=(18, 10))

    pitInfoLabel = ctk.CTkLabel(endWindow, fg_color=background, text_font=(fontType, 18), text="#Pit Info", text_color=mainTextColor, width=40)
    pitInfoLabel.place(x=507, y=40, anchor=tk.N)

    driveTimeWrap = tk.Frame(pitInfo, bg=background)
    driveTimeWrap.pack(side=tk.TOP, expand=True, pady=(13, 13))

    driveTime = ctk.CTkLabel(driveTimeWrap, text="D.T. Time", text_font=(fontType, 18), fg_color=background, text_color=mainTextColor)
    driveTime.pack(side=tk.LEFT)

    driveTimeValue = ctk.CTkEntry(driveTimeWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    driveTimeValue.pack(side=tk.LEFT, padx=0)

    refuelWrap = tk.Frame(pitInfo, bg=background)
    refuelWrap.pack(side=tk.TOP, expand=True, pady=12)

    refuelTime = ctk.CTkLabel(refuelWrap, fg_color=background, text_color=mainTextColor, text="Refuel Time", text_font=(fontType, 17))
    refuelTime.pack(side=tk.LEFT, padx=0)

    refuelTimeValue = ctk.CTkEntry(refuelWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    refuelTimeValue.pack(side=tk.LEFT, padx=0)

    tyreChangeWrap = tk.Frame(pitInfo, bg=background)
    tyreChangeWrap.pack(side=tk.TOP, expand=True, pady=12)

    tyreChange = ctk.CTkLabel(tyreChangeWrap, text="Tyre Change \n Time ", text_font=(fontType, 15),  fg_color=background, text_color=mainTextColor)
    tyreChange.pack(side=tk.LEFT, padx=0)

    tyreChangeValue = ctk.CTkEntry(tyreChangeWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, placeholder_text="Sec", placeholder_text_color=placeholderColor, text_color=entryTextColor)
    tyreChangeValue.pack(padx=0, side=tk.LEFT)

    stintWrap = tk.Frame(pitInfo, bg=background)
    stintWrap.pack(side=tk.TOP, expand=True, pady=(13, 10), padx=5)

    stintpertyre = ctk.CTkLabel(stintWrap, text="Stint/Tyre", fg_color=background, text_color=mainTextColor, text_font=(fontType, 18))
    stintpertyre.pack(side=tk.LEFT, padx=0)

    stintValue = ctk.CTkEntry(stintWrap, width=53, height=20, border_color=entryBorderColor, fg_color=entryFg, text_color=entryTextColor)
    stintValue.pack(side=tk.LEFT, padx=0)


    def compareEnduranceScreen():
        def submitEnduranceComp():

            CompareValuesList = submitEndurance()

            timeLeftCompare = CompareValuesList[0]
            lapCountCompare = CompareValuesList[1]

            foutput = open('output.txt', 'w')


            fueltank = float(fueltankvalue.get())
            fuelcons = float(fuelconsComparevalue.get())

            #race info
            racelength_h = int(racelenghtHourValue.get())
            racelength_m = int(racelenghtMinuteValue.get())
            laptime = float(lapCompareMinValue.get())*60+float(lapCompareSecondsValue.get())
            dttime = float(driveTimeValue.get())
            refueltime = float(refuelTimeValue.get())
            tyrechangetime = float(tyreChangeValue.get())
            stintpertyre = int(stintCompareValue.get())

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

            #Output window
            enduranceCompareOutput = tk.Tk()
            enduranceCompareOutput.title("SSG+ Endurance 2nd Output")
            enduranceCompareOutput['bg']=background
            enduranceCompareOutput.geometry("+1200+0")

            enduranceCompareStrategy = tk.Label(enduranceCompareOutput, text="Second Endurance \n Strategy", bg=background, fg="white")
            enduranceCompareStrategy.config(font=("Helvetical bold", 18))
            enduranceCompareStrategy.pack(expand=True, pady=(20, 0))

            outputCompareWrap = tk.Frame(enduranceCompareOutput, bg=background, highlightbackground=accent, highlightthickness=1)
            outputCompareWrap.pack(expand=True, padx=30, pady=20)

            outputCompareScroll = tk.Scrollbar(outputCompareWrap, width=10)
            outputCompareScroll.pack(side=tk.RIGHT, fill=tk.Y)

            outputList = tk.Listbox(outputCompareWrap, yscrollcommand=outputCompareScroll.set, bg=background, fg=textcolor, bd=0,height=25, width=52, highlightbackground=background,selectbackground=buttonColor)

            #Stint info print
            conversion = datetime.timedelta(seconds=stinttime)
            textoutput = "\n- Welcome to Smart Strategy Generator - "
            foutput.write(textoutput)
            outputList.insert(tk.END, textoutput)
            textoutput = "\nStint lenght = "+str(conversion)
            outputList.insert(tk.END, textoutput)
            foutput.write(textoutput)
            textoutput = "\nRefuel rate = "+str(refuellitertime)+"seconds/L \n"
            outputList.insert(tk.END, textoutput)
            foutput.write(textoutput)

            while timeleft>stinttime :
                stintcount += 1
                textoutput="\n\nStint #"+str(stintcount)+"\n"
                foutput.write(textoutput)
                outputList.insert(tk.END, textoutput)
                while fuelleft>=fuelcons*2:
                        fuelleft -= fuelcons
                        timeleft -= laptime 
                        timeleft = int(timeleft * 100) / 100
                        lapcount += 1
                        conversion = str(datetime.timedelta(seconds=timeleft))
                        if len(conversion)>8:
                            conversion = conversion[:-5]
                        textoutput = "Lap : "+str(lapcount)+" | Time left : "+str(conversion)+" | Fuel left : "+str(round(fuelleft, 2))
                        foutput.write(textoutput)
                        outputList.insert(tk.END, textoutput)
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
                conversion = str(datetime.timedelta(seconds=timeleft))
                if len(conversion)>8:
                    conversion = conversion[:-5]
                textoutput="PIT THIS LAP | Lap : " +str(lapcount)+" | Time left : "+str(conversion)+" | Fuel wasted : "+str(round(fuelleft, 2))
                foutput.write(textoutput)
                outputList.insert(tk.END, textoutput)
                outputList.insert(tk.END, " ")
                fuelleft = fueltank


            #Last stint calculation
            lapsleft = int(timeleft/laptime) + 1
            fuelleft = fuelcons * lapsleft
            timeleft = timeleft - int(refuellitertime*fuelleft) - dttime

            #Last stint generator

            stintcount += 1
            textoutput="\nStint #"+str(stintcount)+"\n"
            foutput.write(textoutput)
            outputList.insert(tk.END, textoutput)
            while timeleft>laptime :
                fuelleft -= fuelcons
                timeleft -= laptime 
                lapcount += 1
                conversion = datetime.timedelta(seconds=timeleft)
                textoutput="Lap : "+str(lapcount)+"| Time left :"+str(conversion)+"| Fuel left : "+str(round(fuelleft, 2))
                foutput.write(textoutput)
                foutput.write("\n")
                outputList.insert(tk.END, textoutput)


            #Last lap 
            fuelleft -= fuelcons
            timeleft -= laptime 
            lapcount += 1
            textoutput="Lap : "+str(lapcount)+"| Fuel left : "+str(round(fuelleft, 2))+"| Race Finished!"
            foutput.write(textoutput)
            outputList.insert(tk.END, textoutput)
            print(timeleft)
            # webbrowser.open("output.txt")

            outputList.config(font=("Helvetical bold", 14))
            outputList.pack(padx=10, pady=10, fill=tk.BOTH, side=tk.LEFT)

            outputCompareScroll.config(command=outputList.yview)
            # DE REVENIT
            closeButton = tk.Button(enduranceCompareOutput, text="Close Window", width=15, height=2, bg=buttonColor, fg=textcolor,activebackground="red", activeforeground="white", bd=1,command=enduranceCompareOutput.destroy)
            closeButton.config(font=("Helvetical bold", 13))
            closeButton.pack(pady=(0, 15))
            
            compareWindow.destroy()

            if lapcount == lapCountCompare:
                if(timeleft<timeLeftCompare):
                    error("2nd strategy is faster")
                else:
                    error("1st strategy is faster")
            elif lapcount>lapCountCompare:
                error("2nd strategy is faster")
            else:
                error("1st strategy is better")
            

        
        foutput = open('output.txt', 'w')
        
        #car info
        # try:
        #     fueltank = float(fueltankvalue.get())
        # except:
        #     error("Fuel Tank variable\nis not correct")
        #     return 0

        # try:
        #     fuelcons = float(fuelconsvalue.get())
        # except:
        #     error("Fuel consumption value\nis not correct")
        #     return 0


        # #race info
        # try:
        #     racelength_h = int(racelenghtHourValue.get())
        # except:
        #     error("Race length value\nis not correct")
        #     return 0
        # try:
        #     racelength_m = int(racelenghtMinuteValue.get())
        # except:
        #     error("Race length value\nis not correct")
        #     return 0
        
        # try:
        #     laptime = float(lapMinValue.get())*60+float(lapSecondsValue.get())
        # except:
        #     error("Laptime value\nis not correct")
        #     return 0

        # #pit info
        # try:
        #     dttime = float(driveTimeValue.get())
        # except:
        #     error("DT time value\nis not correct")
        #     return 0
        # try:
        #     refueltime = float(refuelTimeValue.get())
        # except:
        #     error("Refuel time value\nis not correct")
        #     return 0
        # try:
        #     tyrechangetime = float(tyreChangeValue.get())
        # except:
        #     error("Tyre change value\nis not correct")
        #     return 0
        # try:
        #     stintpertyre = int(stintValue.get())
        # except:
        #     error("Stints/Tyre value\nis not correct")
        #     return 0

        compareWindow = tk.Tk()
        compareWindow['bg']=background
        compareWindow.title("SSG+")
        compareWindow.geometry("+500+200")

        compareInputLabel = ctk.CTkLabel(compareWindow, text="Enter Second\nStrategy's Data", text_font=(fontType, 15), text_color=textcolor)
        compareInputLabel.pack(expand=True, pady=10)

        compareInputWrap = ctk.CTkFrame(compareWindow, fg_color=background, border_color=accent, border_width=borderWidth, corner_radius=cornerRadius)
        compareInputWrap.pack(expand=True, padx=40, pady=(10, 25))

        #laptime

        laptimeCompareWrap = tk.Frame(compareInputWrap, bg=background)
        laptimeCompareWrap.pack(side=tk.TOP, expand=True, pady=(1, 0))

        laptimeCompare = tk.Label(laptimeCompareWrap, text="Lap Time", bg=background, fg="white", height=2)
        laptimeCompare.config(font=("Helvetical bold", 18))
        laptimeCompare.pack(side=tk.LEFT, padx=(10, 70), pady=(0, 0))

        entryWrap = tk.Frame(laptimeCompareWrap, bg=background)
        entryWrap.pack(side=tk.LEFT, padx=(0, 0))

        lapCompareMinValue = tk.Entry(entryWrap, width=3, fg="black")
        lapCompareMinValue.pack(side=tk.LEFT)

        lapCompareMinutes = tk.Label(entryWrap, text="min", bg=background, fg="white")
        lapCompareMinutes.pack(side=tk.LEFT, padx=0)

        lapCompareSecondsValue = tk.Entry(entryWrap, width=5, fg="black")
        lapCompareSecondsValue.pack(side=tk.LEFT, padx=(10, 0))

        secondsCompare = tk.Label(entryWrap, text="sec", bg=background, fg="white")
        secondsCompare.pack(fill=tk.Y, side=tk.LEFT, padx=0)

        #Stint info

        stintWrapCompare = tk.Frame(compareInputWrap, bg=background)
        stintWrapCompare.pack(side=tk.TOP, expand=True)

        stintpertyreCompare = tk.Label(stintWrapCompare, text="Stint/Tyre", bg=background, fg="white", height=2)
        stintpertyreCompare.config(font=("Helvetical bold", 18))
        stintpertyreCompare.pack(side=tk.LEFT, padx=(0, 100))

        stintCompareValue = tk.Entry(stintWrapCompare, width=8, fg="black")
        stintCompareValue.pack(side=tk.LEFT, padx=(0, 18))

        #fuel cons

        tankWrapCompare = tk.Frame(compareInputWrap, bg=background)
        tankWrapCompare.pack(fill=tk.X, side=tk.TOP, padx=1, pady=(0, 6))

        fuelConsCompare = tk.Label(tankWrapCompare, text="Fuel Consumption", fg="white", bg=background, width=16, height=2)
        fuelConsCompare.config(font=("Helvetical bold", 18))
        fuelConsCompare.pack(side=tk.LEFT)

        fuelconsComparevalue = tk.Entry(tankWrapCompare, width=12, bg="white")
        fuelconsComparevalue.pack(side=tk.LEFT, pady=0)

        consWrapCompare = tk.Frame(tankWrapCompare, bg=background)
        consWrapCompare.pack(fill=tk.X, side=tk.TOP, padx=0)

        lperlapCompare = tk.Label(tankWrapCompare, text="L/Lap", fg="white", bg=background)
        lperlapCompare.pack(side=tk.LEFT, fill=tk.Y)

        #SUBMIT COMPARE BUTTON
        submitCompareData = ctk.CTkButton(compareWindow, text="Compare \n Strategy", width=108, height=61, fg_color=buttonColor, text_color=textcolor, hover_color="#547a1f", text_font=(fontType, 14), corner_radius=buttonRadius, command=submitEnduranceComp)
        # submitCompareData.config(font=("Helvetical bold", 14))
        submitCompareData.pack(expand=True, padx=0, pady=(0, 20))

        compareWindow.mainloop()

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
            trackSelectWindow['bg']=background
            trackSelectWindow.title("SSG+")
            trackSelectWindow.geometry("+400+200")
            
            trackfile = car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

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
        
        carSelectWindow = tk.Tk()
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
                
                chooseTrackPresetWindow = tk.Tk()
                chooseTrackPresetWindow['bg']=background
                chooseTrackPresetWindow.title("SSG+ Choose Track")
                chooseTrackPresetWindow.geometry("300x300+400+200")
                
                chooseTrackLabel = ctk.CTkLabel(chooseTrackPresetWindow, fg_color=background, text_color=textcolor, text="Choose a track for \nyour preset", text_font=(fontType, 18))
                chooseTrackLabel.pack(side=tk.TOP, expand=True)

                trackpresetvalue = ctk.CTkEntry(chooseTrackPresetWindow, width=171, height=27, text_font=(fontType, 14), placeholder_text="Track's name", placeholder_text_color=placeholderColor, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor)
                trackpresetvalue.pack(side=tk.TOP, expand=True)
                
                trackpresetsendbut = ctk.CTkButton(chooseTrackPresetWindow, text="Next", height=40, width=80, fg_color=foreground, text_color=textcolor, text_font=(fontType, 14), hover_color=hoverColor, corner_radius=buttonRadius, command=lambda:[tracksectioncheck(str(trackpresetvalue.get()).replace(" ", ""))])
                trackpresetsendbut.pack(side=tk.TOP, expand=True)

                chooseTrackPresetWindow.mainloop()            

            if len(str(carpresetvalue.get())) < 2:
                error("Car name is invalid")
                exit()


            carfilename = curentpath+ z +".ini"
            
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

        selectCarLabel = ctk.CTkLabel(createCarPreset, fg_color=background, text_color=textcolor, text="Choose a car for \nyour preset", text_font=(fontType, 18))
        selectCarLabel.pack(side=tk.TOP, expand=True)
        
        carpresetvalue = ctk.CTkEntry(createCarPreset, width=171, height=27, text_font=(fontType, 14), placeholder_text="Car's name", placeholder_text_color=placeholderColor, text_color=entryTextColor, fg_color=entryFg, border_color=entryBorderColor)
        carpresetvalue.pack(side=tk.TOP, expand=True)

        carpresetsendbut = ctk.CTkButton(createCarPreset, text="Next", height=40, width=80, fg_color=foreground, text_color=textcolor, text_font=(fontType, 14), hover_color=hoverColor, corner_radius=buttonRadius, command=lambda:[filecheck(str(carpresetvalue.get()).replace(" ", ""))])
        carpresetsendbut.pack(side=tk.TOP, expand=True)

        createCarPreset.mainloop()

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
            carfilename = curentpath+car+".ini"
            
            editpresetcarwindow.destroy()
            
            editPresetTrackWindow = tk.Tk()
            editPresetTrackWindow['bg']=background
            editPresetTrackWindow.title("SSG+")
            editPresetTrackWindow.geometry("+400+200")
            
            trackfile = curentpath + car + "T.txt"  
            readtracks = open(trackfile, "r")
            trackList = readtracks.readline()
            trackList = trackList.split()

            trackEditLabel = ctk.CTkLabel(editPresetTrackWindow, text="Select which track \n you want to edit", text_font=(fontType, 18), text_color=textcolor, fg_color=background)
            trackEditLabel.pack(side=tk.TOP, pady=(20, 0))

            trackWrap = ctk.CTkFrame(editPresetTrackWindow, fg_color=background, border_color=accent, border_width=borderWidth)
            trackWrap.pack(side=tk.TOP, pady=(20, 60), padx=100)

            for y in trackList: 
                trackButtonName=y
                trackEditSelect = ctk.CTkButton(trackWrap, width=57, height=34, text_font=(fontType, 13), text=trackButtonName, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, corner_radius=buttonRadius, command=lambda y=y :presetInputWindow(y))
                trackEditSelect.pack(side=tk.TOP, pady=10, padx=20)

            editPresetTrackWindow.mainloop()

        editpresetcarwindow = tk.Tk() 
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

        editpresetcarwindow.mainloop()

    #PRESET BUTTONS

    newpreset = ctk.CTkButton(presets, width=60, height=35, text="New Preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13),command=createnewpreset)
    newpreset.pack(side=tk.LEFT, padx=0, pady=20, expand=True)

    carselectbut = ctk.CTkButton(presets, width=60, height=35, text="Select preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13), command=carSelectwind)
    carselectbut.pack(side=tk.LEFT, pady=20, padx=0, expand=True)

    editpresetbut = ctk.CTkButton(presets, width=60, height=35, text="Edit Preset", text_color=textcolor, fg_color=buttonColor, corner_radius=buttonRadius, hover_color=hoverColor, text_font=(fontType, 13), command=editpresetcar)
    editpresetbut.pack(side=tk.LEFT, padx=0, pady=20, expand=True)


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

        #Output window
        enduranceOutput = tk.Tk()
        enduranceOutput.title("SSG+ Endurance Output")
        enduranceOutput['bg']=background
        enduranceOutput.geometry("+400+0")

        enduranceStrategy = tk.Label(enduranceOutput, text="Endurance \n Strategy", bg=background, fg=textcolor)
        enduranceStrategy.config(font=("Helvetical bold", 18))
        enduranceStrategy.pack(expand=True, pady=(20, 0))

        outputWrap = tk.Frame(enduranceOutput, bg=background, highlightbackground=accent, highlightthickness=1)
        outputWrap.pack(expand=True, padx=30, pady=20)

        outputScroll = tk.Scrollbar(outputWrap, width=10)
        outputScroll.pack(side=tk.RIGHT, fill=tk.Y)

        outputList = tk.Listbox(outputWrap, yscrollcommand=outputScroll.set, bg=background, fg=textcolor, bd=0,height=25, width=52, highlightbackground=background,selectbackground=foreground)

        #Stint info print
        conversion = datetime.timedelta(seconds=stinttime)
        textoutput = "\n- Welcome to Smart Strategy Generator - "
        foutput.write(textoutput)
        outputList.insert(tk.END, textoutput)
        textoutput = "\nStint lenght = "+str(conversion)
        outputList.insert(tk.END, textoutput)
        foutput.write(textoutput)
        textoutput = "\nRefuel rate = "+str(refuellitertime)+"seconds/L \n"
        outputList.insert(tk.END, textoutput)
        foutput.write(textoutput)

        while timeleft>stinttime :
            stintcount += 1
            textoutput="\n\nStint #"+str(stintcount)+"\n"
            foutput.write(textoutput)
            outputList.insert(tk.END, textoutput)
            while fuelleft>=fuelcons*2:
                fuelleft -= fuelcons
                timeleft -= laptime 
                timeleft = int(timeleft * 100) / 100
                lapcount += 1
                conversion = str(datetime.timedelta(seconds=timeleft))
                if len(conversion)>8:
                            conversion = conversion[:-5]
      
                textoutput = "Lap : "+str(lapcount)+" | Time left : "+str(conversion)+" | Fuel left : "+str(round(fuelleft, 2))
                foutput.write(textoutput)
                outputList.insert(tk.END, textoutput)
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
            conversion = str(datetime.timedelta(seconds=timeleft))
            if len(conversion)>8:
                            conversion = conversion[:-5]
                
            textoutput="PIT THIS LAP | Lap : " +str(lapcount)+" | Time left : "+str(conversion)+" | Fuel wasted : "+str(round(fuelleft, 2))
            foutput.write(textoutput)
            outputList.insert(tk.END, textoutput)
            outputList.insert(tk.END, " ")
            fuelleft = fueltank


        #Last stint calculation
        lapsleft = int(timeleft/laptime) + 1
        fuelleft = fuelcons * lapsleft
        timeleft = timeleft - int(refuellitertime*fuelleft) - dttime

        #Last stint generator

        stintcount += 1
        textoutput="\nStint #"+str(stintcount)+"\n"
        foutput.write(textoutput)
        outputList.insert(tk.END, textoutput)
        while timeleft>laptime :
            fuelleft -= fuelcons
            timeleft -= laptime 
            lapcount += 1
            conversion = str(datetime.timedelta(seconds=timeleft))
            if len(conversion) > 9:
                conversion=conversion[:-4]
            textoutput="Lap : "+str(lapcount)+"| Time left :"+str(conversion)+"| Fuel left : "+str(round(fuelleft, 2))
            foutput.write(textoutput)
            foutput.write("\n")
            outputList.insert(tk.END, textoutput)
            

        #Last lap 
        fuelleft -= fuelcons
        timeleft -= laptime 
        lapcount += 1
        textoutput="Lap : "+str(lapcount)+"| Fuel left : "+str(round(fuelleft, 2))+"| Race Finished!"
        foutput.write(textoutput)
        outputList.insert(tk.END, textoutput)
        # webbrowser.open("output.txt")

        outputList.config(font=(fontType, 14))
        outputList.pack(padx=10, pady=10, fill=tk.BOTH, side=tk.LEFT)

        outputScroll.config(command=outputList.yview)

        closeButton = tk.Button(enduranceOutput, text="Close Window", width=15, height=2, bg=foreground, fg=textcolor,activebackground="red", activeforeground="white", bd=1,command=enduranceOutput.destroy)
        closeButton.config(font=(fontType, 13))
        closeButton.pack(pady=(0, 15))

        CompareValuesList = [timeleft, lapcount]
        return CompareValuesList


    #OTHER BUTTONS

    deButtonWrap = tk.Frame(bprWrap, bg=background)
    deButtonWrap.pack(expand=True, pady=(0, 20))

    csButtonWrap = tk.Frame(bprWrap, bg=background)
    csButtonWrap.pack(expand=False)


    documentaton = ctk.CTkButton(deButtonWrap, text="Readme", width=108, height=61, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, text_font=("Helvetical bold", 14), corner_radius=buttonRadius, command=lambda:webbrowser.open("README.md"))
    documentaton.pack(expand=True, side=tk.LEFT, padx=(0,7))

    exit = ctk.CTkButton(deButtonWrap, text="Exit", width=108, height=61, fg_color=buttonColor, text_color=textcolor, hover_color="red", text_font=("Helvetical bold", 14), corner_radius=buttonRadius, command=endWindow.destroy,)
    exit.pack(expand=True, side=tk.LEFT, padx=(7, 0))

    compareData = ctk.CTkButton(csButtonWrap, text="Compare \n Strategy", width=108, height=61, fg_color=buttonColor, text_color=textcolor, hover_color=hoverColor, text_font=("Helvetical bold", 14), corner_radius=buttonRadius, command=compareEnduranceScreen)
    compareData.pack(expand=True, side=tk.LEFT, padx=(0,7))

    submitData = ctk.CTkButton(csButtonWrap, text="Calculate \n Strategy", command=submitEndurance, width=108, height=61, fg_color=buttonColor, text_color=textcolor, hover_color="#547a1f", text_font=("Helvetical bold", 14), corner_radius=buttonRadius)
    submitData.pack(expand=True, side=tk.LEFT, padx=(7,0))
