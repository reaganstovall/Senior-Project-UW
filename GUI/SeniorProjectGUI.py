
from tkinter import * 
import tkinter as tk
import math
import os
from tkinter import ttk
from Templates import Template0, BuildSettings
from Templates import Template1
from Templates import Template2
from Templates import TurnOn
import RunProgram


#from matplotlib import *
#import matplotlib
#matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure

# from msilib.schema import RadioButton
from tkinter.ttk import Style
from functools import partial
from distutils.fancy_getopt import wrap_text

gridWidth = 8
gridHeight = 1
titleWidth = 30
titleHeight = 8
small_font = ("Verdana", 5)
mid_font = ("Verdana", 11)
large_font = ("Verdana", 20)
title_font = ("Verdana", 40)

#Personal Info
userName = ""
email = ""
projName = ""
Template = Template1

SensorDropOn = False
MotorDropOn = False
RelayDropOn = False
cancel = False


BG = "#404347"
FG = "white"
BG_S = "#2F4F4F"
BG_R = "#313238"
FG_R = "white"
FG_S = "#e0d045"

class ControlBox(tk.Tk):
    # kwargs is key word arguments 
    def __init__(self, *args, **kwargs):
        # what we want to initialize
        tk.Tk.__init__(self, *args, **kwargs)
        
        # tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "ControlBox")
        
        # container
        
        container = tk.Frame(self)
        container.config(bg=BG)
        container.pack(side="top", fill="both", expand=True)
        Style().configure("TFrame", background=BG)
        self.after(1,lambda: startScreen(self))
        
        # self.bind("<Button-1>", self.turnPage())
        def startScreen(self):
            startTop = tk.Toplevel()
            startTop.overrideredirect(0)
            startTop.geometry("%dx%d+0+0" % (w, h))
            startTop.focus_set()  # <-- move focus to this widget
            startTop.bind("<Escape>", lambda e: e.widget.quit())
            startTop.config(bg=BG)
            startTop.label = tk.Label(startTop, text="Automation Station", font=title_font, bg=BG, fg=FG)
            startTop.label.config(width=titleWidth, height=titleHeight)
            startTop.label.pack()
        
            self.after(1000,lambda: softStart(self,startTop))
        
        def softStart(self,top):
            openingOptions(self)
            top.destroy()
            
        def getUserName(self):
            top = tk.Toplevel()
            top.overrideredirect(0)
            top.geometry("%dx%d+0+0" % (w, h))
            top.focus_set()  # <-- move focus to this widget
            top.bind("<Escape>", lambda e: e.widget.quit())
            top.config(bg=BG)
            
            emailLabel = tk.Label(top, text="User Name",
                                font=large_font, bg=BG, fg=FG) 
            emailLabel.pack(pady=20)   
            e = Entry(top, font=large_font, justify=CENTER, width=gridWidth * 2)     
            e.pack(pady=20)
            
            submit = tk.Button(top, bd=0, text="Submit", font=large_font, bg=BG_R,
                    fg=FG, command=lambda: handleNewProgram(top, e.get()))
            submit.pack(pady=5)
           
        def openingOptions(self):
            openingTop = tk.Toplevel()
            openingTop.overrideredirect(0)
            openingTop.geometry("%dx%d+0+0" % (w, h))
            openingTop.focus_set()  # <-- move focus to this widget
            openingTop.bind("<Escape>", lambda e: e.widget.quit())
            openingTop.config(bg=BG)
            
            Title = tk.Label(openingTop, text="Home",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20)  
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            
            New = tk.Button(openingTop,bd=0,text="New Program", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2, command=lambda: handleNewProgram(self,openingTop))
            New.pack(pady=5)
            
            Old = tk.Button(openingTop,bd=0,text="Old Program", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2, command=lambda: handleOldProgram(self,openingTop))
            Old.pack(pady=5)
            
            Template = tk.Button(openingTop,bd=0,text="Template", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2, command=lambda: handleTemplate(self,openingTop))
            Template.pack(pady=5)
        
        def displayTemplates(self):
            displayTop = tk.Toplevel()
            displayTop.overrideredirect(0)
            displayTop.geometry("%dx%d+0+0" % (w, h))
            displayTop.focus_set()  # <-- move focus to this widget
            displayTop.bind("<Escape>", lambda e: e.widget.quit())
            displayTop.config(bg=BG)
            
            Title = tk.Label(displayTop, text="Templates",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20)  
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            i = 0
            for f in os.listdir('./Templates'):
                if "init" not in f:
                    if "pycache" not in f:
                        f = f.replace(".py","")
                        print(f)
                        New = tk.Button(displayTop,bd=0,text=f,font=large_font,bg=BG_R,width=gridWidth*2,
                                fg=FG, command=lambda i=i: handleTemplateSelection(self,displayTop,i))
                        New.pack(pady=5)
                        i+=1
        
        def buildOptions(self):
            buildTop = tk.Toplevel()
            buildTop.overrideredirect(0)
            buildTop.geometry("%dx%d+0+0" % (w, h))
            buildTop.focus_set()  # <-- move focus to this widget
            buildTop.bind("<Escape>", lambda e: e.widget.quit())
            buildTop.config(bg=BG)
            
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            
            Home = tk.Button(buildTop,bd=0,text="Home", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth,command=lambda: intermediateFunction(self,buildTop))
            Home.pack(pady=5, padx=5, side=LEFT,expand=True)

            Help = tk.Button(buildTop,bd=0,text="Help", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth,command=lambda: helpBuild(self,buildTop))
            Help.pack(pady=5, padx=5, side=LEFT,expand=True)

            Run = tk.Button(buildTop,bd=0,text="Run", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth,command=lambda: buildRun(self,buildTop))
            Run.pack(pady=5, padx=5, side=RIGHT,expand=True)

            Title = tk.Label(buildTop, text=projName,
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20,side=TOP,expand=True)  

            Sensors = tk.Button(buildTop,bd=0,text="Sensors",font=large_font,bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: intermediateSensor(self,buildTop))
            Sensors.pack(pady=5,side=TOP,expand=True)
            
            Motors = tk.Button(buildTop,bd=0,text="Motors", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2, command=lambda: intermediateMotor(self,buildTop))
            Motors.pack(pady=5,side=TOP,expand=True)
            
            Relays = tk.Button(buildTop,bd=0,text="Relays", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: intermediateRelay(self,buildTop))
            Relays.pack(pady=5,side=TOP,expand=True)

            Functions = tk.Button(buildTop,bd=0,text="Functions", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: intermediateFunction(self,buildTop))
            Functions.pack(pady=5,side=TOP,expand=True)
        
        def handleCancel(self,buildRun):
            print("handleCancel")
        
        def buildTemplate(self):
            
            BuildSettings.__template__ = Template.__template__
            BuildSettings.__author__ = Template.__author__
            BuildSettings.__copyright__ = Template.__copyright__
            BuildSettings.__license__ = Template.__license__
            BuildSettings.__version__ = Template.__version__
            BuildSettings.__maintainer__ = Template.__maintainer__
            BuildSettings.__email__ = Template.__email__
            BuildSettings.__status__ = Template.__status__
            BuildSettings.__description__ = Template.__description__
            
            BuildSettings.TempOffset = Template.TempOffset
            BuildSettings.LightOffset = Template.LightOffset
            BuildSettings.HumidityOffset = Template.HumidityOffset
            BuildSettings.MoistureOffset = Template.MoistureOffset
            
            
            BuildSettings.PAP = Template.PAP
            BuildSettings.PAT = Template.PAT
            BuildSettings.PAV = Template.PAV
            BuildSettings.PAN = Template.PAN
            BuildSettings.PAR = Template.PAR
            BuildSettings.PAO = Template.PAO
            BuildSettings.PDP = Template.PDP
            BuildSettings.PDN = Template.PDN
            
            BuildSettings.SAP = Template.SAP
            BuildSettings.SAT = Template.SAT
            BuildSettings.SAV = Template.SAV
            BuildSettings.SAN = Template.SAN
            BuildSettings.SAR = Template.SAR
            BuildSettings.SDP = Template.SDP
            BuildSettings.SDN = Template.SDN
             
            BuildSettings.PMP = Template.PMP
            BuildSettings.PMT = Template.PMT
            BuildSettings.PMS = Template.PMS
            BuildSettings.PMN = Template.PMN
            
            BuildSettings.SMP = Template.SMP
            BuildSettings.SMT = Template.SMT
            BuildSettings.SMS = Template.SMS
            BuildSettings.SMN  = Template.SMN
            
            BuildSettings.PR12P = Template.PR12P
            BuildSettings.PR12N = Template.PR12N
            
            BuildSettings.PRACP = Template.PRACP
            BuildSettings.PRACN = Template.PRACN
            
            BuildSettings.SR12P  = Template.SR12P
            BuildSettings.SR12N  = Template.SR12N
            
            BuildSettings.SRACP = Template.SRACP
            BuildSettings.SRACN = Template.SRACN
            
            BuildSettings.FNC_List = Template.FNC_List
            BuildSettings.FNC_Names = Template.FNC_Names
        
            
        def buildRun(self,top):
            print("buildRun")
            global cancel
            top.destroy()  
            buildTemplate(self)
            buildRun = tk.Toplevel()
            buildRun.overrideredirect(0)
            buildRun.geometry("%dx%d+0+0" % (w, h))
            buildRun.focus_set()  # <-- move focus to this widget
            buildRun.bind("<Escape>", lambda e: e.widget.quit())
            buildRun.config(bg=BG)
            
            Title = tk.Label(buildRun, text=projName,
                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20,side=TOP,expand=True)
            
            #updateSensors(self,buildRun)
            
            buildRun.Cancel = tk.Button(buildRun,bd=0,text="Functions", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: handleCancel(self, buildRun))
            buildRun.Cancel.pack(pady=5,side=TOP,expand=True)
            
            
            RunProgram.sensorRead()
            #buildRun.Sensor[][] = tk.Button(buildRun,bd=0,text="Sensor", font=large_font, bg=BG_R,
            #        fg=FG,width=gridWidth)
            #
            #for i in range(8):
            #    for j in range(2):
            #    buildRun.Sensor = tk.Button(buildRun,bd=0,text="Functions", font=large_font, bg=BG_R,
            #        fg=FG,width=gridWidth*2,command=lambda: handleCancel(self, buildRun))
            #    buildRun.Sensor.pack(pady=5,side=TOP,expand=True)
            
        def updateSensors():
            print("hello")
            #while(cancel is False):
                #RunProgram.sensorInitialization()
                #RunProgram.sensorRead()
                #updateSensors()
                
            
            
            
        def intermediateSensor(self,buildTop):
            buildTop.destroy()
            pickSensors(self)
        
        def intermediateRelay(self,buildTop):
            buildTop.destroy()
            pickRelays(self)
                
        def intermediateMotor(self,buildTop):
            buildTop.destroy()
            pickMotors(self)
            
        def intermediateFunction(self,buildTop):
            buildTop.destroy()
            pickFunctions(self)
            
        def intermediateFunctionDelete(self,buildTop,port):
            del Template.FNC_List[port]
            del Template.FNC_Names[port]
            buildTop.destroy()
            pickFunctions(self)
                
        def pickSensors(self):
            print("pickSensors")
            sensorPickTop = tk.Toplevel()
            sensorPickTop.overrideredirect(0)
            sensorPickTop.geometry("%dx%d+0+0" % (w, h))
            sensorPickTop.focus_set()  # <-- move focus to this widget
            sensorPickTop.bind("<Escape>", lambda e: e.widget.quit())
            sensorPickTop.config(bg=BG)
            
            Title = tk.Label(sensorPickTop, text="Sensors",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20)  
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            
            PrimaryAnalog = tk.Button(sensorPickTop,bd=0,text="Primary Analog", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: showSensors(self,sensorPickTop,0))
            PrimaryAnalog.pack(pady=5)
            
            PrimaryDigital = tk.Button(sensorPickTop,bd=0,text="Primary Digital", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: showSensors(self,sensorPickTop,1))
            PrimaryDigital.pack(pady=5)
            
            if SensorDropOn is True:
                
                SecondaryAnalog = tk.Button(sensorPickTop,bd=0,text="Secondary Analog", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: showSensors(self,sensorPickTop,2))
                SecondaryAnalog.pack(pady=5)
    
                SecondaryDigital = tk.Button(sensorPickTop,bd=0,text="Secondary Digital", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: showSensors(self,sensorPickTop,3))
                SecondaryDigital.pack(pady=5)
        
        def pickMotors(self):
            print("pickMotors")
            motorPickTop = tk.Toplevel()
            motorPickTop.overrideredirect(0)
            motorPickTop.geometry("%dx%d+0+0" % (w, h))
            motorPickTop.focus_set()  # <-- move focus to this widget
            motorPickTop.bind("<Escape>", lambda e: e.widget.quit())
            motorPickTop.config(bg=BG)
            
            motorPickTop.Title = tk.Label(motorPickTop, text="Motors",
                                font=large_font, bg=BG, fg=FG) 
            motorPickTop.Title.pack(pady=20)  
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            if MotorDropOn is True:
                
                motorPickTop.Primary = tk.Button(motorPickTop,bd=0,text="Primary Motors", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: showMotors(self,motorPickTop,0))
                motorPickTop.Primary.pack(pady=5)
                
                motorPickTop.Secondary = tk.Button(motorPickTop,bd=0,text="Primary Secondary", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: showMotors(self,motorPickTop,1))
                motorPickTop.Secondary.pack(pady=5)
            else:showMotors(self,motorPickTop,0)
                
        def pickRelays(self):
            print("pickRelays")
            relayPickTop = tk.Toplevel()
            relayPickTop.overrideredirect(0)
            relayPickTop.geometry("%dx%d+0+0" % (w, h))
            relayPickTop.focus_set()  # <-- move focus to this widget
            relayPickTop.bind("<Escape>", lambda e: e.widget.quit())
            relayPickTop.config(bg=BG)
            
            Title = tk.Label(relayPickTop, text="Relays",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=20)  
             
            #e = Entry(openingTop, font=large_font, justify=CENTER, width=gridWidth*2)     
            #e.pack(pady=20)
            
            
            Primary12 = tk.Button(relayPickTop,bd=0,text="Primary 12v", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2, command=lambda: showRelays(self,relayPickTop,0))
            Primary12.pack(pady=5)
            
            PrimaryAC = tk.Button(relayPickTop,bd=0,text="Primary AC", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2, command=lambda: showRelays(self,relayPickTop,1))
            PrimaryAC.pack(pady=5)
            
            if RelayDropOn is True:
            
                Secondary12 = tk.Button(relayPickTop,bd=0,text="Secondary 12v", font=large_font, bg=BG_R,
                        fg=FG,width=gridWidth*2, command=lambda: showRelays(self,relayPickTop,2))
                Secondary12.pack(pady=5)
    
                SecondaryAC = tk.Button(relayPickTop,bd=0,text="Secondary AC", font=large_font, bg=BG_R,
                        fg=FG,width=gridWidth*2, command=lambda: showRelays(self,relayPickTop,3))
                SecondaryAC.pack(pady=5)
        
        def pickFunctions(self):
            print("PickFunctions")
            funcPickTop = tk.Toplevel()
            funcPickTop.overrideredirect(0)
            funcPickTop.geometry("%dx%d+0+0" % (w, h))
            funcPickTop.focus_set()  # <-- move focus to this widget
            funcPickTop.bind("<Escape>", lambda e: e.widget.quit())
            funcPickTop.config(bg=BG)
            
            Title = tk.Label(funcPickTop, text="Functions",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=10,side=TOP)  
            
            New = tk.Button(funcPickTop,bd=0,text="NewFunction", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: buildNewFunction(self,funcPickTop))
            New.pack(pady=5,side=BOTTOM)
            
            back = tk.Button(funcPickTop,bd=0,text="Back", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: tempBuildOptions(self,funcPickTop))
            back.pack(pady=5,side=BOTTOM)
            
            for i in range(len(Template.FNC_List)):
                print(i)
                if len(Template.FNC_List) < 5:
                    funcBtn = tk.Button(funcPickTop,bd=0,text=Template.FNC_Names[i], font=large_font, bg=BG_R,
                        fg=FG, command=lambda i=i: reviewFunc(self,funcPickTop,i))
                    funcBtn.pack(pady=1,padx=1,side=LEFT,expand=True)
                else:
                    funcBtn = tk.Button(funcPickTop,bd=0,text=("F",[i]), font=large_font, bg=BG_R,
                        fg=FG, command=lambda i=i: reviewFunc(self,funcPickTop,i))
                    funcBtn.pack(pady=1,padx=1,side=LEFT,expand=True)
                
        def buildNewFunction(self, top):
            print("buildNewFunction")
            print(len(Template.FNC_List))
            currStart = 0
            currEnd = 0
            currHW = (0,0)
            currDir = 0
            currOper = 0
            currComp = 0
            currSensor = (0,0)
            currDuration = 0
            
            currTuple = (currStart, currEnd, currHW, currDir, currOper, currComp,
                         currSensor, currDuration)
            Template.FNC_List.append(currTuple)
            print(Template.FNC_List)
            print(len(Template.FNC_List))
            getNewFuncName(self, (len(Template.FNC_List) - 1))
            top.destroy()
            
        def getNewFuncName(self, port):
            newNameTop = tk.Toplevel()
            newNameTop.overrideredirect(0)
            newNameTop.geometry("%dx%d+0+0" % (w, h))
            newNameTop.focus_set()  # <-- move focus to this widget
            newNameTop.bind("<Escape>", lambda e: e.widget.quit())
            newNameTop.config(bg=BG)
            
            nameLabel = tk.Label(newNameTop, text="Function Name",
                                font=large_font, bg=BG, fg=FG) 
            nameLabel.pack(pady=20)   
            e=Entry(newNameTop, font=large_font,justify=CENTER,width=gridWidth*2)     
            e.pack(pady=20)
            
            submit = tk.Button(newNameTop,bd=0,text="Done",font=large_font,bg=BG_R,
                fg=FG,command=lambda: handleNewFuncName(self,newNameTop,e.get(),port))
            submit.pack(pady=5)
        
        def handleNewFuncName(self,newNameTop,name,port): 
            Template.FNC_Names.append(name)
            reviewFunc(self, newNameTop, port)  
        
        def reviewFuncTime(self,top,port):
            print("timing")
            top.destroy()
            funcTop = tk.Toplevel()
            funcTop.overrideredirect(0)
            funcTop.geometry("%dx%d+0+0" % (w, h))
            funcTop.focus_set()  # <-- move focus to this widget
            funcTop.bind("<Escape>", lambda e: e.widget.quit())
            funcTop.config(bg=BG)
            
            Title = tk.Label(funcTop, text="Timing",
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=10,side=TOP)  
            
            startSTime = Template.FNC_List[port][0]#time in seconds
            startHTime = math.floor(startSTime/3600)
            startMTime = math.floor((startSTime - (startHTime*3600))/60)
            startSTime = startSTime%60
            
            endSTime = Template.FNC_List[port][1]#time in seconds
            endHTime = math.floor(endSTime/3600)
            endMTime = math.floor((endSTime - (endHTime*3600))/60)
            endSTime = endSTime%60
            
            startlable = tk.Label(funcTop, text="Start Time",
                                font=mid_font, bg=BG, fg=FG) 
            startlable.pack(side=TOP) 
            
            StartTime = tk.Button(funcTop,bd=0,text=("S:",startSTime,"M:",startMTime,"H:",startHTime), font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*3,command=lambda: handleFuncStart(self,funcTop,port))
            StartTime.pack(pady=5,side=TOP)

            endlable = tk.Label(funcTop, text="End Time",
                                font=mid_font, bg=BG, fg=FG) 
            endlable.pack(side=TOP) 
            
            EndTime = tk.Button(funcTop,bd=0,text=("S:",endSTime,"M:",endMTime,"H:",endHTime), font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*3,command=lambda: handleFuncEnd(self,funcTop,port))
            EndTime.pack(pady=5,side=TOP)
            
            back = tk.Button(funcTop,bd=0,text="Back", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,funcTop,port))
            back.pack(pady=5,side=BOTTOM)
        
        def handleFuncStart(self,topfunc,port):
            print("start")
            topfunc.destroy()
            starttop = tk.Toplevel()
            starttop.overrideredirect(0)
            starttop.geometry("%dx%d+0+0" % (w, h))
            starttop.focus_set()  # <-- move focus to this widget
            starttop.bind("<Escape>", lambda e: e.widget.quit())
            starttop.config(bg=BG)
            
            
            startSTime = Template.FNC_List[port][0]#time in seconds
            startHTime = math.floor(startSTime/3600)
            startMTime = math.floor((startSTime - (startHTime*3600))/60)
            startSTime = startSTime%60
            
            starttop.s = Scale(starttop,label="Seconds",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            starttop.s.pack(pady=3,padx=3)
            starttop.s.set(startSTime)
            
            starttop.m = Scale(starttop,label="Minutes",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            starttop.m.pack(pady=3,padx=3)
            starttop.m.set(startMTime)
#sdfsd            
            starttop.h = Scale(starttop,label="Hours",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=48)     
            starttop.h.pack(pady=3,padx=3)
            starttop.h.set(startHTime)

            starttop.helpBtn = tk.Button(starttop,text="Help",font=large_font,width=gridWidth,
                    command=lambda: helpStartTime(self,starttop))
            starttop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth*2, bd=0)
            starttop.helpBtn.pack(side=LEFT,pady=5)

            starttop.fromChoiceBtn = tk.Button(starttop, bd=0, text="Set Time", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: checkTime(starttop,starttop.s.get(),starttop.m.get(),starttop.h.get()))
            starttop.fromChoiceBtn.pack(side=RIGHT,pady=5)
            
            def checkTime(starttop,s,m,h):
                startTime = int(s+(m*60)+(h*3600))
                if Template.FNC_List[port][1] is 0 or Template.FNC_List[port][1] > startTime:
                    handleFuncStartSelect(self,starttop,starttop.s.get(),starttop.m.get(),starttop.h.get(),port)
                
        def handleFuncEnd(self,topfunc,port):
            print("end")
            topfunc.destroy()
            endtop = tk.Toplevel()
            endtop.overrideredirect(0)
            endtop.geometry("%dx%d+0+0" % (w, h))
            endtop.focus_set()  # <-- move focus to this widget
            endtop.bind("<Escape>", lambda e: e.widget.quit())
            endtop.config(bg=BG)
            
            endSTime = Template.FNC_List[port][1]#time in seconds
            endHTime = math.floor(endSTime/3600)
            endMTime = math.floor((endSTime - (endHTime*3600))/60)
            endSTime = endSTime%60
            
            endtop.s = Scale(endtop,label="Seconds",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            endtop.s.pack(pady=3,padx=3)
            endtop.s.set(endSTime)
            
            endtop.m = Scale(endtop,label="Minutes",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            endtop.m.pack(pady=3,padx=3)
            endtop.m.set(endMTime)
            
            endtop.h = Scale(endtop,label="Hours",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=48)     
            endtop.h.pack(pady=3,padx=3)
            endtop.h.set(endHTime)

            endtop.helpBtn = tk.Button(endtop,text="Help",font=large_font,width=gridWidth,
                    command=lambda: helpEndTime(self,endtop))
            endtop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth*2, bd=0)
            endtop.helpBtn.pack(side=LEFT,pady=5)

            endtop.fromChoiceBtn = tk.Button(endtop, bd=0, text="Set Time", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: handleFuncEndSelect(self,endtop,endtop.s.get(),endtop.m.get(),endtop.h.get(),port))
            endtop.fromChoiceBtn.pack(side=RIGHT,pady=5)
            
        def handleFuncStartSelect(self,top,s,m,h,port):
            startTime = int(s+(m*60)+(h*3600))
            currTuple = (startTime, Template.FNC_List[port][1],Template.FNC_List[port][2],
                         Template.FNC_List[port][3],Template.FNC_List[port][4],
                         Template.FNC_List[port][5],Template.FNC_List[port][6],
                         Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            reviewFuncTime(self,top,port)
        
        def handleFuncEndSelect(self,top,s,m,h,port):
            endTime = int(s+(m*60)+(h*3600))
            currTuple = (Template.FNC_List[port][0],endTime,Template.FNC_List[port][2],
                         Template.FNC_List[port][3],Template.FNC_List[port][4],
                         Template.FNC_List[port][5],Template.FNC_List[port][6],
                         Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            reviewFuncTime(self,top,port)
         
        def helpStartTime(self,topfunc):
            print("helpStartTime")
            helptop = tk.Toplevel()
            helptop.overrideredirect(0)
            helptop.geometry("%dx%d+0+0" % (w, h))
            helptop.focus_set()  # <-- move focus to this widget
            helptop.bind("<Escape>", lambda e: e.widget.quit())
            helptop.config(bg=BG) 
            helptop.helpLable = tk.Label(helptop, 
                text="The Start Time is when this function is active. This value" +
                " is set from the start of the program. If left at 0, the function" +
                " will be active from the start."
                
                ,wraplength= 400,font=large_font, bg=BG, fg=FG) 
            helptop.helpLable.pack(padx=20)
            
            helptop.closeBtn = tk.Button(helptop, bd=0, text="Close", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: helptop.destroy())
            helptop.closeBtn.pack(side=BOTTOM,pady=5) 
        
        def helpEndTime(self,topfunc):
            print("helpEndTime")
            helptop = tk.Toplevel()
            helptop.overrideredirect(0)
            helptop.geometry("%dx%d+0+0" % (w, h))
            helptop.focus_set()  # <-- move focus to this widget
            helptop.bind("<Escape>", lambda e: e.widget.quit())
            helptop.config(bg=BG) 
            helptop.helpLable = tk.Label(helptop, 
                text="The End Time is when this function ends. This value is set" +
                " from the start of the program. If left at 0, the function will" +
                " continue from the Start Time till the end of the program."
                
                ,wraplength= 400,font=large_font, bg=BG, fg=FG) 
            helptop.helpLable.pack(padx=20)
            
            helptop.closeBtn = tk.Button(helptop, bd=0, text="Close", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: helptop.destroy())
            helptop.closeBtn.pack(side=BOTTOM,pady=5) 
        
        def helpFunc(self,topfunc):
            print("helpFunc")
            helptop = tk.Toplevel()
            helptop.overrideredirect(0)
            helptop.geometry("%dx%d+0+0" % (w, h))
            helptop.focus_set()  # <-- move focus to this widget
            helptop.bind("<Escape>", lambda e: e.widget.quit())
            helptop.config(bg=BG) 
            helptop.helpLable = tk.Label(helptop, 
                text="A function is what we call blob of logic that's decided by you."
                
                ,wraplength= 400,font=large_font, bg=BG, fg=FG) 
            helptop.helpLable.pack(padx=20)
            
            helptop.closeBtn = tk.Button(helptop, bd=0, text="Close", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: helptop.destroy())
            helptop.closeBtn.pack(side=BOTTOM,pady=5)
        
        def helpBuild(self,topfunc):
            print("helpDuration")
            helptop = tk.Toplevel()
            helptop.overrideredirect(0)
            helptop.geometry("%dx%d+0+0" % (w, h))
            helptop.focus_set()  # <-- move focus to this widget
            helptop.bind("<Escape>", lambda e: e.widget.quit())
            helptop.config(bg=BG) 
            helptop.helpLable = tk.Label(helptop, 
                text="This is where you set up your sensors and hardware."
                
                ,wraplength= 400,font=large_font, bg=BG, fg=FG) 
            helptop.helpLable.pack(padx=20)
            
            helptop.closeBtn = tk.Button(helptop, bd=0, text="Close", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: helptop.destroy())
            helptop.closeBtn.pack(side=BOTTOM,pady=5) 
         
            
        def helpDuration(self,topfunc):
            print("helpDuration")
            helptop = tk.Toplevel()
            helptop.overrideredirect(0)
            helptop.geometry("%dx%d+0+0" % (w, h))
            helptop.focus_set()  # <-- move focus to this widget
            helptop.bind("<Escape>", lambda e: e.widget.quit())
            helptop.config(bg=BG) 
            helptop.helpLable = tk.Label(helptop, 
                text="The Duration is how long you want the action to be performed" + 
                 " by the hardware. Example: Turn on Relay for 2 minutes(Duration)" +
                 " when sensor is greater than 300."
                
                ,wraplength= 400,font=large_font, bg=BG, fg=FG) 
            helptop.helpLable.pack(padx=20)
            
            helptop.closeBtn = tk.Button(helptop, bd=0, text="Close", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: helptop.destroy())
            helptop.closeBtn.pack(side=BOTTOM,pady=5)
            
           
        def handleFuncSensors(self,senseTop,j,i,port):
            print(j,i,port)
            currSensor = ((j+1),i)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         currSensor,Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncSensor(self,senseTop,port)
            
        def handleFuncSensorSwitch(self,senseTop,port):
            currSensor = (0,0)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         currSensor,Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            senseTop.destroy()
            reviewFuncSensor(self,senseTop,port)
            
        def reviewFuncSensor(self,top,port):
            print("reviewFuncSensor")
            top.destroy()
            senseTop = tk.Toplevel()
            senseTop.overrideredirect(0)
            senseTop.geometry("%dx%d+0+0" % (w, h))
            senseTop.focus_set()  # <-- move focus to this widget
            senseTop.bind("<Escape>", lambda e: e.widget.quit())
            senseTop.config(bg=BG)
            
            senseTop.Title = tk.Label(senseTop, text="Sensors",
                                font=large_font, bg=BG, fg=FG) 
            senseTop.Title.pack(pady=10,side=TOP)
            
            senseTop.back = tk.Button(senseTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,senseTop,port))
            senseTop.back.pack(pady=5,side=BOTTOM,expand=True)
            
            voltage = 0
            type_ = 0
            bias_ = 0
            SensorDropOn = True
            # if there isn't a sensor selected already:
            print(Template.FNC_List[port][6])
            sensorCount = 0
            if (Template.FNC_List[port][6][0] is 0):
                senseTop.sensor = [[0 for i in range(8)] for j in range(4)]
                for i in range(8):
                    for j in range(4):
                        senseTop.sensor[j][i] = tk.Button(senseTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                            fg=FG, command=lambda i=i, j=j: handleFuncSensors(self,senseTop,j,i,port))
                for k in range(8):
                    if Template.PAP[k] is 1:
                        if SensorDropOn is True: senseTop.sensor[0][k].configure(text=("PA",[k]))
                        else:senseTop.sensor[0][k].configure(text=Template.PAN[k])
                        senseTop.sensor[0][k].pack(side = LEFT, expand = True)
                    if Template.PDP[k] is 1:
                        if SensorDropOn is True: senseTop.sensor[1][k].configure(text=("PD",[k]))
                        else:senseTop.sensor[1][k].configure(text=Template.PDN[k])
                        senseTop.sensor[1][k].pack(side = LEFT, expand = True)
                    if SensorDropOn is True:    
                        if Template.SAP[k] is 1: 
                            senseTop.sensor[2][k].configure(text=("SA",[k]))
                            senseTop.sensor[2][k].pack(side = LEFT, expand = True)
                        if Template.SDP[k] is 1:
                            senseTop.sensor[3][k].configure(text=("SD",[k]))
                            senseTop.sensor[3][k].pack(side = LEFT, expand = True)
                sensorCount += 1   
                
            #there is a sensor for this function        
            else:
                if Template.FNC_List[port][6][0] is 1: #Analog
                    name = Template.PAN[Template.FNC_List[port][6][1]]
                    type_= Template.PAT[port]
                    voltage = Template.PAV[port]
                    bias_ = Template.PAR[port]
                elif Template.FNC_List[port][6][0] is 2: #Digital
                    name = Template.PDN[Template.FNC_List[port][6][1]]
                    type_= 0
                elif Template.FNC_List[port][6][0] is 3: #Analog
                    name = Template.SAN[Template.FNC_List[port][6][1]]
                    type_= Template.SAT[port]
                    voltage = Template.SAV[port]
                    bias_ = Template.PAR[port]
                elif Template.FNC_List[port][6][0] is 4: #Digital
                    name = Template.SDN[Template.FNC_List[port][6][1]]
                    type_= 0
           
                if voltage is 3: voltage = 3.3
                if type_ is 0: _type_ = "Switch"
                if type_ is 1: _type_ = "Temperature" 
                if type_ is 2: _type_ = "Moisture"
                if type_ is 3: _type_ = "Humidity"
                if type_ is 4: _type_ = "Light"
                if type_ is 5: _type_ = "pH"
                if type_ is 6: _type_ = "Other"
                
                if bias_ is 0: _bias_ = "100K pulldown"
                if bias_ is 1: _bias_ = "51k pulldown"
                if bias_ is 2: _bias_ = "10k pulldown"
                if bias_ is 3: _bias_ = "5.1k pulldown"
                if bias_ is 4: _bias_ = "1k pulldown"
                if bias_ is 5: _bias_ = "510 pulldown"
                if bias_ is 6: _bias_ = "100 pulldown"
                if bias_ is 7: _bias_ = "none"
                if bias_ is 8: _bias_ = "100k 5v pullup"
                if bias_ is 9: _bias_ = "51k 5v pullup"
                if bias_ is 10: _bias_ = "5.1k 5v pullup"
                if bias_ is 11: _bias_ = "1M pulldown"
                if bias_ is 12: _bias_ = "510k pulldown"
                if bias_ is 13: _bias_ = "100k 3.3v pullup"
                if bias_ is 14: _bias_ = "51k 3.3v pullup"
                if bias_ is 15: _bias_ = "5.1k 3.3v pullup"
                
                
                senseTop.Name = tk.Label(senseTop, text=("Name:",name),
                                font=large_font, bg=BG, fg=FG) 
                senseTop.Name.pack(pady=10,side=TOP)
                
                senseTop.Type = tk.Label(senseTop, text=("Type:",_type_),
                                    font=large_font, bg=BG, fg=FG) 
                senseTop.Type.pack(pady=10,side=TOP)
                
                if((Template.FNC_List[port][6][0] is 1) or (Template.FNC_List[port][6][0] is 3)): #Analog 
                    
                    senseTop.voltage = tk.Label(senseTop, text=("Voltage:",voltage),
                                    font=large_font, bg=BG, fg=FG) 
                    senseTop.voltage.pack(pady=10,side=TOP) 
                    
                    senseTop.Bias = tk.Label(senseTop, text=("Bias:",_bias_),
                                    font=large_font, bg=BG, fg=FG) 
                    senseTop.Bias.pack(pady=10,side=TOP) 
                    
                senseTop.switchBtn = tk.Button(senseTop,bd=0,text="Switch Sensor", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: handleFuncSensorSwitch(self,senseTop,port))
                senseTop.switchBtn.pack(pady=5,side=BOTTOM,expand=True)
        
        def reviewFuncRelay(self,top,port):
            print("reviewFuncRelay")
            top.destroy()
            relayFuncTop = tk.Toplevel()
            relayFuncTop.overrideredirect(0)
            relayFuncTop.geometry("%dx%d+0+0" % (w, h))
            relayFuncTop.focus_set()  # <-- move focus to this widget
            relayFuncTop.bind("<Escape>", lambda e: e.widget.quit())
            relayFuncTop.config(bg=BG)
            
            #if it was a motor and now you're selecting relay 
            hadwareID = Template.FNC_List[port][2][0]
            if((hadwareID is 1) or (hadwareID is 2)):
                currAction = 0
                currOperator = 0
                currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],currAction,currOperator,
                         Template.FNC_List[port][5],Template.FNC_List[port][6],Template.FNC_List[port][7])
                Template.FNC_List[port] = currTuple
            
            
            relayFuncTop.Title = tk.Label(relayFuncTop, text="Relays",
                                font=large_font, bg=BG, fg=FG) 
            relayFuncTop.Title.pack(pady=10,side=TOP)
            
            relayFuncTop.back = tk.Button(relayFuncTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,relayFuncTop,port))
            relayFuncTop.back.pack(pady=5,side=BOTTOM,expand=True)
            
            _type_ = ""
            _port_ = ""
            name = ""
            # if there isn't a sensor selected already:
            print(Template.FNC_List[port][2])
            if (Template.FNC_List[port][2][0] is 0): #hardware is not selected
                relayFuncTop.relay = [[0 for i in range(4)] for j in range(4)]
                for i in range(4):
                    for j in range(4):
                        relayFuncTop.relay[j][i] = tk.Button(relayFuncTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                            fg=FG, width = gridWidth, command=lambda i=i, j=j: handleFuncRelays(self,relayFuncTop,j,i,port))
                for k in range(4):
                    if Template.PR12P[k] is 1:
                        if RelayDropOn is True: relayFuncTop.relay[0][k].configure(text=("12v",[k+1]))
                        else:relayFuncTop.relay[0][k].configure(text=Template.PR12N[k])
                        relayFuncTop.relay[0][k].pack(side = LEFT, expand = True)
                    if Template.PRACP[k] is 1:
                        if RelayDropOn is True: relayFuncTop.relay[1][k].configure(text=("AC",[k+5]))
                        else:relayFuncTop.relay[1][k].configure(text=Template.PRACN[k])
                        relayFuncTop.relay[1][k].pack(side = LEFT, expand = True)
                    if RelayDropOn is True:    
                        if Template.SR12P[k] is 1: 
                            relayFuncTop.relay[2][k].configure(text=("12v",[k+1]))
                            relayFuncTop.relay[2][k].pack(side = LEFT, expand = True)
                        if Template.SRACP[k] is 1:
                            relayFuncTop.relay[3][k].configure(text=("AC",[k+5]))
                            relayFuncTop.relay[3][k].pack(side = LEFT, expand = True)
            #there is a sensor for this function        
            else:
                if Template.FNC_List[port][2][0] is 3:#PRACP 
                    name = Template.PR12N[Template.FNC_List[port][2][1]]
                    _type_= "12v"
                    _port_= ("Relay",[Template.FNC_List[port][2][1]+1])
                elif Template.FNC_List[port][2][0] is 4: #PRACP
                    name = Template.PRACN[Template.FNC_List[port][2][1]]
                    _type_= "AC"
                    _port_= ("Relay",[Template.FNC_List[port][2][1]+5])
                elif Template.FNC_List[port][2][0] is 5: #SR12P
                    name = Template.SR12N[Template.FNC_List[port][2][1]]
                    _type_= "12v"
                    _port_= ("SecondaryRelay",[Template.FNC_List[port][2][1]+1])
                elif Template.FNC_List[port][2][0] is 6: #SRACP
                    name = Template.SRACN[Template.FNC_List[port][2][1]]
                    _type_= "AC"
                    _port_= ("SecondaryRelay",[Template.FNC_List[port][2][1]+5])
                
                relayFuncTop.Name = tk.Label(relayFuncTop, text=("Name:",name),
                                font=large_font, bg=BG, fg=FG) 
                relayFuncTop.Name.pack(pady=10,side=TOP)
                
                relayFuncTop.Type = tk.Label(relayFuncTop, text=("Type:",_type_),
                                    font=large_font, bg=BG, fg=FG) 
                relayFuncTop.Type.pack(pady=10,side=TOP)
                
                relayFuncTop.Port = tk.Label(relayFuncTop, text=("Port:",_port_),
                                    font=large_font, bg=BG, fg=FG) 
                relayFuncTop.Port.pack(pady=10,side=TOP)
                
                relayFuncTop.switchBtn = tk.Button(relayFuncTop,bd=0,text="Switch Relay", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: handleFuncRelaySwitch(self,relayFuncTop,port))
                relayFuncTop.switchBtn.pack(pady=5,side=BOTTOM,expand=True)
        
        def handleFuncRelaySwitch(self,relayTop,port):
            currRelay = (0,0)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         currRelay,Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncRelay(self,relayTop,port)
        
        def handleFuncRelays(self,relayTop,j,i,port):
            print(j,i,port)
            currRelay = ((j+3),i)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         currRelay,Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncRelay(self,relayTop,port)
        
        def reviewFuncMotor(self,top,port):
            print("reviewFuncMotor")
            top.destroy()
            motorFuncTop = tk.Toplevel()
            motorFuncTop.overrideredirect(0)
            motorFuncTop.geometry("%dx%d+0+0" % (w, h))
            motorFuncTop.focus_set()  # <-- move focus to this widget
            motorFuncTop.bind("<Escape>", lambda e: e.widget.quit())
            motorFuncTop.config(bg=BG)
            
            #if it was a relay and now you're selecting motor 
            hadwareID = Template.FNC_List[port][2][0]
            if((hadwareID is 3) or (hadwareID is 4) or (hadwareID is 5) or (hadwareID is 6)):
                currAction = 0
                currOperator = 0
                currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],currAction,currOperator,
                         Template.FNC_List[port][5],Template.FNC_List[port][6],Template.FNC_List[port][7])
                Template.FNC_List[port] = currTuple
            
            motorFuncTop.Title = tk.Label(motorFuncTop, text="Motor",
                                font=large_font, bg=BG, fg=FG) 
            motorFuncTop.Title.pack(pady=10,side=TOP)
            
            motorFuncTop.back = tk.Button(motorFuncTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,motorFuncTop,port))
            motorFuncTop.back.pack(pady=5,side=BOTTOM,expand=True)
            
            type_ = 0
            _type_ = ""
            _port_ = ""
            name = ""
            # if there isn't a sensor selected already:
            print(Template.FNC_List[port][2])
            if (Template.FNC_List[port][2][0] is 0): #hardware is not selected
                motorFuncTop.motor = [[0 for i in range(4)] for j in range(2)]
                for i in range(4):
                    for j in range(2):
                        motorFuncTop.motor[j][i] = tk.Button(motorFuncTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                            fg=FG, width = gridWidth, command=lambda i=i, j=j: handleFuncMotors(self,motorFuncTop,j,i,port))
                for k in range(4):
                    if Template.PMP[k] is 1:
                        if((Template.PMT[k] is 1) or (Template.PMT[k] is 2)):
                            if MotorDropOn is True: motorFuncTop.motor[0][k].configure(text=("M",[k+1]))
                            else:motorFuncTop.motor[0][k].configure(text=Template.PMN[k])
                            motorFuncTop.motor[0][k].pack(side = LEFT, expand = True)
                    if MotorDropOn is True:    
                        if((Template.SMT[k] is 1) or (Template.SMT[k] is 2)):
                            motorFuncTop.motor[1][k].configure(text=Template.SMN[k])
                            motorFuncTop.motor[1][k].pack(side = LEFT, expand = True)
            #there is a sensor for this function        
            else:
                if Template.FNC_List[port][2][0] is 1:#PMP 
                    name = Template.PMN[Template.FNC_List[port][2][1]]
                    type_= Template.PMT[Template.FNC_List[port][2][1]]
                    _port_= ("Motor",[Template.FNC_List[port][2][1]+1])
                elif Template.FNC_List[port][2][0] is 2: #SMP
                    name = Template.SMN[Template.FNC_List[port][2][1]]
                    type_= Template.PMT[Template.FNC_List[port][2][1]]
                    _port_= ("SecondaryMotor",[Template.FNC_List[port][2][1]+1])
                
                
                if type_ is 1: _type_ = "Single Direction"
                if type_ is 2: _type_ = "Bi Directional"
                
                motorFuncTop.Name = tk.Label(motorFuncTop, text=("Name:",name),
                                font=large_font, bg=BG, fg=FG) 
                motorFuncTop.Name.pack(pady=10,side=TOP)
                
                motorFuncTop.Type = tk.Label(motorFuncTop, text=("Type:",_type_),
                                    font=large_font, bg=BG, fg=FG) 
                motorFuncTop.Type.pack(pady=10,side=TOP)
                
                motorFuncTop.Port = tk.Label(motorFuncTop, text=("Port:",_port_),
                                    font=large_font, bg=BG, fg=FG) 
                motorFuncTop.Port.pack(pady=10,side=TOP)
                
                motorFuncTop.switchBtn = tk.Button(motorFuncTop,bd=0,text="Switch Motors", font=large_font, bg=BG_R,
                        fg=FG, width=gridWidth*2,command=lambda: handleFuncMotorSwitch(self,motorFuncTop,port))
                motorFuncTop.switchBtn.pack(pady=5,side=BOTTOM,expand=True)
        
        def handleFuncMotorSwitch(self,motorTop,port):
            currMotor = (0,0)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         currMotor,Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncMotor(self,motorTop,port)
        
        def handleFuncMotors(self,motorTop,j,i,port):
            print(j,i,port)
            currMotor = ((j+1),i)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         currMotor,Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncMotor(self,motorTop,port)
         
        def handleFuncCompValue(self, top, port):
            print("handleFuncCompValue")
            top.destroy()
            funcCompTop = tk.Toplevel()
            funcCompTop.overrideredirect(0)
            funcCompTop.geometry("%dx%d+0+0" % (w, h))
            funcCompTop.focus_set()  # <-- move focus to this widget
            funcCompTop.bind("<Escape>", lambda e: e.widget.quit())
            funcCompTop.config(bg=BG)
            
            funcCompTop.helpBtn = tk.Button(funcCompTop,text="Help",font=mid_font,width=gridWidth)
            funcCompTop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth, bd=0)
            funcCompTop.helpBtn.pack(pady=10)

            funcCompTop.s = Scale(funcCompTop,label="Sensor Value",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*10,to=300)     
            funcCompTop.s.pack(padx=10)
            funcCompTop.s.set(Template.FNC_List[port][5])
            
            funcCompTop.selectBtn = tk.Button(funcCompTop,bd=0,text="Select",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompValueSelect(self,funcCompTop,funcCompTop.s.get(),port))
            funcCompTop.selectBtn.pack(pady=40,padx=100)
            
        def handleFuncCompValueSelect(self, top, value, port):
            print("handleFuncCompValueSelect")
            currValue = (value)
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],Template.FNC_List[port][3],
                         Template.FNC_List[port][4],currValue,
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncComp(self,top,port)
            
        def handleFuncCompActSelect(self, top, value, port):
            print("handleFuncCompValueSelect")
            if value is 1:
                if(Template.PMT[Template.FNC_List[port][2][1]] is 1):currValue = 1
                elif(Template.PMT[Template.FNC_List[port][2][1]] is 2):currValue = 2
            else: currValue = value
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],currValue,
                         Template.FNC_List[port][4],Template.FNC_List[port][5],
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncComp(self,top,port)
            
        def handleFuncCompAction(self, top, port):           
            print("handleFuncCompValue")
            top.destroy()
            funcActTop = tk.Toplevel()
            funcActTop.overrideredirect(0)
            funcActTop.geometry("%dx%d+0+0" % (w, h))
            funcActTop.focus_set()  # <-- move focus to this widget
            funcActTop.bind("<Escape>", lambda e: e.widget.quit())
            funcActTop.config(bg=BG)
            
            funcActTop.helpBtn = tk.Button(funcActTop,text="Help",font=mid_font,width=gridWidth)
            funcActTop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth, bd=0)
            funcActTop.helpBtn.pack(pady=10)

            funcActTop.TurnOnBtn = tk.Button(funcActTop,bd=0,text="Turn On",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompActSelect(self,funcActTop,4,port))
            
            funcActTop.TurnOFFBtn = tk.Button(funcActTop,bd=0,text="Turn OFF",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompActSelect(self,funcActTop,5,port))
            
            funcActTop.RotateForwardBtn = tk.Button(funcActTop,bd=0,text="Rotate Forward",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompActSelect(self,funcActTop,1,port))
            
            funcActTop.RotateReverseBtn = tk.Button(funcActTop,bd=0,text="Rotate Reverse",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompActSelect(self,funcActTop,3,port))
            
            funcActTop.StopBtn = tk.Button(funcActTop,bd=0,text="Stop",font=large_font,bg=BG_R,width=gridWidth*2,
                    fg=FG,command=lambda: handleFuncCompActSelect(self,funcActTop,0,port))
            
            subPort = Template.FNC_List[port][2][1]
            
            if(Template.FNC_List[port][2][0] is 1):#Primary motor
                print("#Primary motor")
                if(Template.PMT[subPort] is 1):#single Direction 
                    print("#single Direction")
                    funcActTop.RotateForwardBtn.pack(pady=40,padx=100)
                    funcActTop.StopBtn.pack(pady=40,padx=100)
                if(Template.PMT[subPort] is 2):#Bi Direction 
                    funcActTop.RotateForwardBtn.pack(pady=40,padx=100)
                    funcActTop.RotateReverseBtn.pack(pady=40,padx=100)
                    funcActTop.StopBtn.pack(pady=40,padx=100)    
            elif(Template.FNC_List[port][2][0] is 2):  
                if(Template.SMT[subPort] is 1):#single Direction 
                    funcActTop.RotateForwardBtn.pack(pady=40,padx=100)
                    funcActTop.StopBtn.pack(pady=40,padx=100)
                if(Template.SMT[subPort] is 2):#Bi Direction 
                    funcActTop.RotateForwardBtn.pack(pady=40,padx=100)
                    funcActTop.RotateReverseBtn.pack(pady=40,padx=100)
                    funcActTop.StopBtn.pack(pady=40,padx=100)             
            else:#Relays        
                funcActTop.TurnOnBtn.pack(pady=40,padx=100)
                funcActTop.TurnOFFBtn.pack(pady=40,padx=100)
                
        def handleFuncCompOperation(self,compFuncTop,port):
            print("handleFuncCompValue")
            compFuncTop.destroy()
            funcOprTop = tk.Toplevel()
            funcOprTop.overrideredirect(0)
            funcOprTop.geometry("%dx%d+0+0" % (w, h))
            funcOprTop.focus_set()  # <-- move focus to this widget
            funcOprTop.bind("<Escape>", lambda e: e.widget.quit())
            funcOprTop.config(bg=BG)
            
            funcOprTop.helpBtn = tk.Button(funcOprTop,text="Help",font=mid_font,width=gridWidth)
            funcOprTop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth, bd=0)
            funcOprTop.helpBtn.pack(pady=10)

            funcOprTop.GreaterBtn = tk.Button(funcOprTop,bd=0,text="Is Greater Than",font=large_font,bg=BG_R,width=gridWidth*3,
                    fg=FG,command=lambda: handleFuncCompOprSelect(self,funcOprTop,1,port))
            
            funcOprTop.LesserBtn = tk.Button(funcOprTop,bd=0,text="Is Less Than",font=large_font,bg=BG_R,width=gridWidth*3,
                    fg=FG,command=lambda: handleFuncCompOprSelect(self,funcOprTop,2,port))
            
            funcOprTop.PressedBtn = tk.Button(funcOprTop,bd=0,text="When Switch is Pressed",font=large_font,bg=BG_R,width=gridWidth*3,
                    fg=FG,command=lambda: handleFuncCompOprSelect(self,funcOprTop,3,port))
            
            funcOprTop.OpenBtn = tk.Button(funcOprTop,bd=0,text="When Switch is Released",font=large_font,bg=BG_R,width=gridWidth*3,
                    fg=FG,command=lambda: handleFuncCompOprSelect(self,funcOprTop,4,port))
            
            if((Template.FNC_List[port][6][0] is 1) or (Template.FNC_List[port][6][0] is 3)):#Analog
                funcOprTop.GreaterBtn.pack(pady=40,padx=100)
                funcOprTop.LesserBtn.pack(pady=40,padx=100)
            else:#digital
                funcOprTop.PressedBtn.pack(pady=40,padx=100)
                funcOprTop.OpenBtn.pack(pady=40,padx=100)
            
        def handleFuncCompOprSelect(self, top, value, port):
            print("handleFuncCompOprSelect")
            currValue = value
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],Template.FNC_List[port][3],
                         currValue, Template.FNC_List[port][5], 
                         Template.FNC_List[port][6],Template.FNC_List[port][7])
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncComp(self,top,port)    
        
        def handleFuncCompDuration(self,topfunc,port):
            print("handleFuncCompDuration")
            topfunc.destroy()
            durTop = tk.Toplevel()
            durTop.overrideredirect(0)
            durTop.geometry("%dx%d+0+0" % (w, h))
            durTop.focus_set()  # <-- move focus to this widget
            durTop.bind("<Escape>", lambda e: e.widget.quit())
            durTop.config(bg=BG)
            
            endSTime = Template.FNC_List[port][7]#time in seconds
            endHTime = math.floor(endSTime/3600)
            endMTime = math.floor((endSTime - (endHTime*3600))/60)
            endSTime = endSTime%60
            
            durTop.s = Scale(durTop,label="Seconds",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            durTop.s.pack(pady=3,padx=3)
            durTop.s.set(endSTime)
            
            durTop.m = Scale(durTop,label="Minutes",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            durTop.m.pack(pady=3,padx=3)
            durTop.m.set(endMTime)
            
            durTop.h = Scale(durTop,label="Hours",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=48)     
            durTop.h.pack(pady=3,padx=3)
            durTop.h.set(endHTime)

            durTop.helpBtn = tk.Button(durTop,text="Help",font=large_font,width=gridWidth,
                    command=lambda: helpDuration(self,durTop))
            durTop.helpBtn.config(bg=BG_R, fg=FG, width=gridWidth*2, bd=0)
            durTop.helpBtn.pack(side=LEFT,pady=5)

            durTop.fromChoiceBtn = tk.Button(durTop, bd=0, text="Set Time", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: handleFuncCompDurSelect(self,durTop,durTop.s.get(),durTop.m.get(),durTop.h.get(),port))
            durTop.fromChoiceBtn.pack(side=RIGHT,pady=5)
            
        def handleFuncCompDurSelect(self, top, s, m, h, port):
            print("handleFuncCompDurSelect")
            
            currValue = (s + (m * 60) + (h * 3600))
            currTuple = (Template.FNC_List[port][0],Template.FNC_List[port][1],
                         Template.FNC_List[port][2],Template.FNC_List[port][3],
                         Template.FNC_List[port][4],Template.FNC_List[port][5], 
                         Template.FNC_List[port][6],currValue)
            Template.FNC_List[port] = currTuple
            print(Template.FNC_List[port])
            reviewFuncComp(self,top,port)    
            
        def reviewFuncComp(self,top,port):
            print("reviewFuncMotor")
            top.destroy()
            compFuncTop = tk.Toplevel()
            compFuncTop.overrideredirect(0)
            compFuncTop.geometry("%dx%d+0+0" % (w, h))
            compFuncTop.focus_set()  # <-- move focus to this widget
            compFuncTop.bind("<Escape>", lambda e: e.widget.quit())
            compFuncTop.config(bg=BG)
            
            compFuncTop.Title = tk.Label(compFuncTop, text="Comparison",
                                font=large_font, bg=BG, fg=FG) 
            compFuncTop.Title.pack(pady=10,side=TOP)
            
            compFuncTop.back = tk.Button(compFuncTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,compFuncTop,port))
            compFuncTop.back.pack(pady=5,side=BOTTOM,expand=True)
            
            
            
            compFuncTop.actionBtn = tk.Button(compFuncTop,bd=0,text="Set Action", font=large_font,
                    fg=FG, width=gridWidth*2,command=lambda: handleFuncCompAction(self,compFuncTop,port))
            if Template.FNC_List[port][3] is 0: compFuncTop.actionBtn.config(bg=BG_R)
            else: compFuncTop.actionBtn.config(bg=BG_S)
            
            compFuncTop.operatorBtn = tk.Button(compFuncTop,bd=0,text="Set Operator", font=large_font,
                    fg=FG, width=gridWidth*2,command=lambda: handleFuncCompOperation(self,compFuncTop,port))
            if Template.FNC_List[port][4] is 0: compFuncTop.operatorBtn.config(bg=BG_R)
            else: compFuncTop.operatorBtn.config(bg=BG_S)
            
            compFuncTop.compareBtn = tk.Button(compFuncTop,bd=0,text="Set Value", font=large_font, 
                    fg=FG, width=gridWidth*2,command=lambda: handleFuncCompValue(self,compFuncTop,port))
            if Template.FNC_List[port][5] is 0: compFuncTop.compareBtn.config(bg=BG_R)
            else: compFuncTop.compareBtn.config(bg=BG_S)
            
            compFuncTop.durationBtn = tk.Button(compFuncTop,bd=0,text="Set Duration", font=large_font, 
                    fg=FG, width=gridWidth*2,command=lambda: handleFuncCompDuration(self,compFuncTop,port))
            if Template.FNC_List[port][7] is 0: compFuncTop.durationBtn.config(bg=BG_R)
            else: compFuncTop.durationBtn.config(bg=BG_S)
            
           
            stupid = False
            HWStupid = False
            #there is a sensor for this function        
            if (Template.FNC_List[port][2][0] is 0): #sensor is not selected
                stupid = True
                HWStupid = True
                compFuncTop.sensorl = tk.Label(compFuncTop, text="Please Select a Hardware component first",
                    font=large_font, bg=BG, fg=FG) 
                compFuncTop.sensorl.pack(pady=10,side=TOP)
                
                compFuncTop.hw = tk.Button(compFuncTop,bd=0,text="Hardware", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFunc(self,compFuncTop,port))
                compFuncTop.hw.pack(pady=5,side=BOTTOM,expand=True)
            # if there isn't a sensor selected already:
            print(Template.FNC_List[port][6])#Sensor
            if (Template.FNC_List[port][6][0] is 0): #sensor is not selected
                stupid = True
                
                compFuncTop.sensor = tk.Button(compFuncTop,bd=0,text="Set Sensor", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: reviewFuncSensor(self,compFuncTop,port))
                compFuncTop.sensor.pack(pady=5,side=BOTTOM,expand=True)
                
                if HWStupid is False:
                    compFuncTop.actionBtn.pack(pady=5,side=TOP,expand=True)
                
            if(stupid is False):#everything is filled out
                
                if ((Template.FNC_List[port][6][0] is 1) or (Template.FNC_List[port][6][0] is 3)):#Analog
                    compFuncTop.compareBtn.pack(pady=5,side=TOP,expand=True)
                compFuncTop.operatorBtn.pack(pady=5,side=TOP,expand=True)
                compFuncTop.actionBtn.pack(pady=5,side=TOP,expand=True)
                compFuncTop.durationBtn.pack(pady=5,side=TOP,expand=True)
                    
                
                
        def reviewFunc(self, top, port):
            print("reviewFunc")
            top.destroy()
            funcTop = tk.Toplevel()
            funcTop.overrideredirect(0)
            funcTop.geometry("%dx%d+0+0" % (w, h))
            funcTop.focus_set()  # <-- move focus to this widget
            funcTop.bind("<Escape>", lambda e: e.widget.quit())
            funcTop.config(bg=BG)
            
            Title = tk.Label(funcTop, text=Template.FNC_Names[port],
                                font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=10,side=TOP)  
            
            Delete = tk.Button(funcTop,bd=0,text="Delete", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: intermediateFunctionDelete(self,funcTop,port))
            Delete.pack(pady=5,side=BOTTOM,expand=True)
            
            back = tk.Button(funcTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: intermediateFunction(self,funcTop))
            back.pack(pady=5,side=BOTTOM,expand=True)

            helper = tk.Button(funcTop,bd=0,text="Help", font=large_font, bg=BG_R,
                    fg=FG, width=gridWidth*2,command=lambda: helpFunc(self, funcTop))
            helper.pack(pady=5,side=BOTTOM,expand=True)
            
            timing = tk.Button(funcTop,bd=0,text="Timing", font=large_font, fg=FG, 
                    width=gridWidth,command=lambda: reviewFuncTime(self,funcTop,port))
            timing.pack(pady=5,side=LEFT,expand=True)
            
            if(Template.FNC_List[port][0] is 0) or (Template.FNC_List[port][1] is 0):
                timing.config(bg = BG_R)
            else: timing.config(bg = BG_S)
            
            Sensor = tk.Button(funcTop,bd=0,text="Sensor", font=large_font, fg=FG,
                    width=gridWidth,command=lambda: reviewFuncSensor(self,funcTop,port))
            Sensor.pack(pady=5,side=LEFT,expand=True)
            
            if(Template.FNC_List[port][6][0] is 0):
                Sensor.config(bg = BG_R)
            else: Sensor.config(bg = BG_S)

            comparator = tk.Button(funcTop,bd=0,text="Action", font=large_font, fg=FG,
                    width=gridWidth,command=lambda: reviewFuncComp(self,funcTop,port))
            comparator.pack(pady=5,side=LEFT,expand=True)
            
            if(Template.FNC_List[port][3] is 0):
                comparator.config(bg = BG_R)
            else: comparator.config(bg = BG_S)
            
            Relay = tk.Button(funcTop,bd=0,text="Relay", font=large_font, fg=FG, 
                    width=gridWidth,command=lambda: reviewFuncRelay(self,funcTop,port))
            Relay.pack(pady=5,side=LEFT,expand=True)
            
            Motor = tk.Button(funcTop,bd=0,text="Motor", font=large_font, fg=FG, 
                    width=gridWidth,command=lambda: reviewFuncMotor(self,funcTop,port))
            Motor.pack(pady=5,side=LEFT,expand=True)

            if(Template.FNC_List[port][2][0] is 0):
                Relay.config(bg = BG_R)
                Motor.config(bg = BG_R)
            elif(Template.FNC_List[port][2][0] is 1):
                Relay.config(bg = BG_R)
                Motor.config(bg = BG_S)
            elif(Template.FNC_List[port][2][0] is 2):
                Relay.config(bg = BG_R)
                Motor.config(bg = BG_S)
            else:
                Relay.config(bg = BG_S)
                Motor.config(bg = BG_R)
        
        
        #Done---------------------------------------------
        def showSensors(self,top,floor):
            top.destroy()
            sensorTop = tk.Toplevel()
            sensorTop.overrideredirect(0)
            sensorTop.geometry("%dx%d+0+0" % (w, h))
            sensorTop.focus_set()  # <-- move focus to this widget
            sensorTop.bind("<Escape>", lambda e: e.widget.quit())
            sensorTop.config(bg=BG)
            
            Title = tk.Label(sensorTop, font=large_font, bg=BG, fg=FG) 
            Title.pack(pady=5,side=TOP)  
            
            homeBtn = tk.Button(sensorTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2, command=lambda: tempBuildOptions(self,sensorTop))
            homeBtn.pack(pady=5,side=BOTTOM,expand=True)
            
            print(floor)
            for i in range(8):
                sensor = tk.Button(sensorTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                        fg=FG, command=lambda i=i: handleSensors(self,sensorTop,floor,i))
                if floor is 0: 
                    sensor.configure(text=("A",i+1))
                    if Template.PAP[i] is 1:
                        sensor.configure(bg=BG_S)
                        Title.configure(text="Primary Analog")
                elif floor is 1: 
                    sensor.configure(text=("D",i+1))
                    if Template.PDP[i] is 1:
                        sensor.configure(bg=BG_S)
                        Title.configure(text="Primary Digital")
                elif floor is 2: 
                    sensor.configure(text=("A",i+1))
                    if Template.SAP[i] is 1:
                        sensor.configure(bg=BG_S)
                        Title.configure(text="Secondary Analog")
                elif floor is 3: 
                    sensor.configure(text=("D",i+1))
                    if Template.SDP[i] is 1:
                        sensor.configure(bg=BG_S)
                        Title.configure(text="Secondary Digital")
                sensor.pack(pady=5,side=LEFT,expand=True)
        #Done---------------------------------------------
        def showMotors(self,top,floor):
            top.destroy()
            motorTop = tk.Toplevel()
            motorTop.overrideredirect(0)
            motorTop.geometry("%dx%d+0+0" % (w, h))
            motorTop.focus_set()  # <-- move focus to this widget
            motorTop.bind("<Escape>", lambda e: e.widget.quit())
            motorTop.config(bg=BG)
            
            motorTop.Title = tk.Label(motorTop, font=large_font, bg=BG, fg=FG) 
            motorTop.Title.pack(pady=5,side=TOP)  
                        
            motorTop.backBtn = tk.Button(motorTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2,command=lambda: tempBuildOptions(self,motorTop))
            motorTop.backBtn.pack(pady=5,side=BOTTOM,expand=True)
            
            print(floor)
            for i in range(4):
                motorTop.motor = tk.Button(motorTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                        fg=FG,width=gridWidth, command=lambda i=i: handleMotorsSelect(self,motorTop,floor,i))
                if floor is 0: 
                    motorTop.motor.configure(text=("M",i+1))
                    if Template.PMP[i] is 1:
                        motorTop.motor.configure(bg=BG_S)
                        motorTop.Title.configure(text="Primary Motors")
                    
                elif floor is 1: 
                    motorTop.motor.configure(text=("M",i+1))
                    if Template.SMP[i] is 1:
                        motorTop.motor.configure(bg=BG_S)
                        motorTop.Title.configure(text="Secondary Motors")
                
                motorTop.motor.pack(pady=5,side=LEFT,expand=True)
        #Done---------------------------------------------
        def showRelays(self,top,floor):
            top.destroy()
            relayTop = tk.Toplevel()
            relayTop.overrideredirect(0)
            relayTop.geometry("%dx%d+0+0" % (w, h))
            relayTop.focus_set()  # <-- move focus to this widget
            relayTop.bind("<Escape>", lambda e: e.widget.quit())
            relayTop.config(bg=BG)
            
            relayTop.Title = tk.Label(relayTop, font=large_font, bg=BG, fg=FG) 
            relayTop.Title.pack(pady=5,side=TOP)  
                        
            relayTop.backBtn = tk.Button(relayTop,bd=0,text="Done", font=large_font, bg=BG_R,
                    fg=FG,width=gridWidth*2, command=lambda: tempBuildOptions(self,relayTop))
            relayTop.backBtn.pack(pady=5,side=BOTTOM,expand=True)
            
            for i in range(4):
                relayTop.relay = tk.Button(relayTop,bd=0,font=large_font,bg=BG_R,height=gridWidth,
                        fg=FG,width=gridWidth, command=lambda i=i: handleRelaySelect(self,relayTop,floor,i))
                if floor is 0: 
                    relayTop.relay.configure(text=("R",[i+1]))
                    if Template.PR12P[i] is 1:
                        relayTop.relay.configure(bg=BG_S)
                        relayTop.Title.configure(text="12v Relays")
                elif floor is 1: 
                    relayTop.relay.configure(text=("R",[i+5]))
                    if Template.PRACP[i] is 1:
                        relayTop.relay.configure(bg=BG_S)
                        relayTop.Title.configure(text="AC Relays")
                elif floor is 2: 
                    relayTop.relay.configure(text=("R",[i+1]))
                    if Template.SR12P[i] is 1:
                        relayTop.relay.configure(bg=BG_S)
                        relayTop.Title.configure(text="12v Relays")
                elif floor is 3: 
                    relayTop.relay.configure(text=("R",[i+5]))
                    if Template.SRACP[i] is 1:
                        relayTop.relay.configure(bg=BG_S)
                        relayTop.Title.configure(text="AC Relays")
                
                relayTop.relay.pack(pady=5,side=LEFT,expand=True)
        #Done---------------------------------------------
        def tempBuildOptions(self,top):
            top.destroy()
            buildOptions(self)
        #Done---------------------------------------------
        def handleRelaySelect(self,sensorPickTop,floor,port):
            print("handleRelaySelect")
            if floor is 0:#Primary 12v
                if Template.PR12P[port] is 1:#Already selected
                    Template.PR12P[port] = 0
                    Template.PR12N[port] = ""
                    showRelays(self,sensorPickTop,floor)
                else:
                    Template.PR12P[port] = 1
                    getRelayName(self,floor,port)
                    sensorPickTop.destroy()
            if floor is 1:#Primary AC
                if Template.PRACP[port] is 1:#Already selected
                    Template.PRACP[port] = 0
                    Template.PRACN[port] = ""
                    showRelays(self,sensorPickTop,floor)
                else:
                    Template.PRACP[port] = 1
                    getRelayName(self,floor,port)
                    sensorPickTop.destroy()  
            if floor is 2:#Secondary 12v
                if Template.SR12P[port] is 1:#Already selected
                    Template.SR12P[port] = 0
                    Template.SR12N[port] = ""
                    showRelays(self,sensorPickTop,floor)
                else:
                    Template.SR12P[port] = 1
                    getRelayName(self,floor,port)
                    sensorPickTop.destroy()  
            if floor is 3:#Secondary AC
                if Template.SRACP[port] is 1:#Already selected
                    Template.SRACP[port] = 0
                    Template.SRACN[port] = ""
                    showRelays(self,sensorPickTop,floor)
                else:
                    Template.SRACP[port] = 1
                    getRelayName(self,floor,port)
                    sensorPickTop.destroy()          
        #Done---------------------------------------------
        def getRelayName(self,floor,port):
            relayTopName = tk.Toplevel()
            relayTopName.overrideredirect(0)
            relayTopName.geometry("%dx%d+0+0" % (w, h))
            relayTopName.focus_set()  # <-- move focus to this widget
            relayTopName.bind("<Escape>", lambda e: e.widget.quit())
            relayTopName.config(bg=BG)
            
            nameLabel = tk.Label(relayTopName, text="Relay Name",
                                font=large_font, bg=BG, fg=FG) 
            nameLabel.pack(pady=20)   
            e=Entry(relayTopName, font=large_font,justify=CENTER,width=gridWidth*2)     
            e.pack(pady=20)
            
            submit = tk.Button(relayTopName,bd=0,text="Done",font=large_font,bg=BG_R,
                fg=FG,command=lambda: handleRelayName(self,relayTopName,e.get(),floor,port))
            submit.pack(pady=5)
        #Done---------------------------------------------
        def handleRelayName(self,top,name,floor,port):
            if floor is 0: 
                Template.PR12N[port] = name
            if floor is 1: 
                Template.PRACN[port] = name
            if floor is 2: 
                Template.SR12N[port] = name
            if floor is 3: 
                Template.SRACN[port] = name
            showRelays(self,top,floor)
        #Done---------------------------------------------
        def handleMotorsSelect(self,motorTop,floor,port):
            print("floor",floor,Template.PAP[port])
            if floor is 0:#Primary analog
                if Template.PMP[port] is 1:#Already selected
                    if (Template.PMT[port] is 2): #Binary Deselection
                        Template.PMP[port+1] = 0
                        Template.PMT[port+1] = 0
                        Template.PMN[port+1] = ""
                    if (Template.PMT[port] is 3): #Binary Deselection
                        Template.PMP[port-1] = 0
                        Template.PMT[port-1] = 0
                        Template.PMN[port-1] = ""
                    Template.PMP[port] = 0
                    Template.PMN[port] = ""
                        
                    showMotors(self,motorTop,floor)
                else:
                    Template.PMP[port] = 1
                    getMotorName(self,floor,port)
                    motorTop.destroy()
            if floor is 1:#Primary Digital
                if Template.SMP[port] is 1:#Already selected
                    if (Template.SMT[port] is 2): #Binary Deselection
                        Template.SMP[port+1] = 0
                        Template.SMT[port+1] = 0
                        Template.SMN[port+1] = ""
                    if (Template.SMT[port] is 3): #Binary Deselection
                        Template.SMP[port-1] = 0
                        Template.SMT[port-1] = 0
                        Template.SMN[port-1] = ""
                    Template.SMP[port] = 0
                    Template.SMN[port] = ""
                        
                    showMotors(self,motorTop,floor)
                else:
                    Template.SMP[port] = 1
                    getMotorName(self,floor,port)
                    motorTop.destroy()       
        #Done---------------------------------------------
        def getMotorName(self,floor,port):
            topName = tk.Toplevel()
            topName.overrideredirect(0)
            topName.geometry("%dx%d+0+0" % (w, h))
            topName.focus_set()  # <-- move focus to this widget
            topName.bind("<Escape>", lambda e: e.widget.quit())
            topName.config(bg=BG)
            
            nameLabel = tk.Label(topName, text="Motor Name",
                                font=large_font, bg=BG, fg=FG) 
            nameLabel.pack(pady=20)   
            e=Entry(topName, font=large_font,justify=CENTER,width=gridWidth*2)     
            e.pack(pady=20)
            
            submit = tk.Button(topName,bd=0,text="Done",font=large_font,bg=BG_R,
                fg=FG,command=lambda: handleMotorName(self,topName,e.get(),floor,port))
            submit.pack(pady=5)
        
        #Done---------------------------------------------
        def handleMotorName(self,top,name,floor,port):
            if floor is 0: 
                Template.PMN[port] = name
                getMotorType(self,floor,port)
            if floor is 1: 
                Template.SMN[port] = name
                getMotorType(self,floor,port)
            top.destroy()
        
        #Done---------------------------------------------
        def getMotorType(self,floor,port):
            typetop = tk.Toplevel()
            typetop.overrideredirect(0)
            typetop.geometry("%dx%d+0+0" % (w, h))
            typetop.focus_set()  # <-- move focus to this widget
            typetop.bind("<Escape>", lambda e: e.widget.quit())
            typetop.config(bg=BG)
            MODE1 = [("Single Direction",1),("Bi-Direction",2)]
            
            v = tk.IntVar()
            v.set(0) #sets which one to pick, annoying feature that can't be disabled
                    
            label = tk.Label(typetop, text="Type of Motor",
                        font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
            label.pack() 
            if floor is 0:
                if((port is 0) or (port is 2)):
                    if(Template.PMP[port+1] is 0):
                        for text, mode in MODE1: #
                            b = tk.Radiobutton(typetop,text=text,
                                variable=v,value=mode,indicatoron=0,
                                command=lambda: handleMotorType(self,typetop,v.get(),floor,port))
                            b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,
                                height=gridHeight, font=large_font)
                            b.pack(padx=5, pady=5)
                    else:handleMotorType(self,typetop,1,floor,port)
                else:handleMotorType(self,typetop,1,floor,port)
            elif((floor is 1) or (floor is 3)):handleMotorType(self,typetop,1,floor,port)
            elif floor is 2:
                if((port is 0) or (port is 2)):
                    if(Template.SMP[port+1] is 0):
                        for text, mode in MODE1: #
                            b = tk.Radiobutton(typetop,text=text,
                                variable=v,value=mode,indicatoron=0,
                                command=lambda: handleMotorType(self,typetop,v.get(),floor,port))
                            b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,
                                height=gridHeight, font=large_font)
                            b.pack(padx=5, pady=5)
                    else:handleMotorType(self,typetop,1,floor,port)
                else:handleMotorType(self,typetop,1,floor,port)
        #Done---------------------------------------------
        def handleMotorType(self,handletop,motorType,floor,port):
            if floor is 0:
                Template.PMT[port] = motorType
                if(motorType is 2):
                    Template.PMP[port + 1] = 1
                    Template.PMT[port + 1] = 3
            if floor is 1:
                Template.SMT[port] = motorType
                if(motorType is 2):
                    Template.SMP[port + 1] = 1
                    Template.SMT[port + 1] = 3
            showMotors(self,handletop,floor)
                
        #Done---------------------------------------------
        def getSensorType(self,floor,port):
            top = tk.Toplevel()
            top.overrideredirect(0)
            top.geometry("%dx%d+0+0" % (w, h))
            top.focus_set()  # <-- move focus to this widget
            top.bind("<Escape>", lambda e: e.widget.quit())
            top.config(bg=BG)
            MODE1 = [("Temperature",1),("Moisture",2),("Humidity",3),
                     ("Light",4),("pH",5),("Other",6)]
            
            v = tk.IntVar()
            v.set(0) #sets which one to pick, annoying feature that can't be disabled
                    
            label = tk.Label(top, text="Type of Sensor",
                        font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
            label.pack() 
            
            if floor is 0 or 2: #analog
                for text, mode in MODE1: #Analog
                    b = tk.Radiobutton(top,text=text,
                        variable=v,value=mode,indicatoron=0,
                        command=lambda: handleSensorType(self,top,v.get(),floor,port))
                    b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,
                        height=gridHeight, font=large_font)
                    b.pack(padx=5, pady=5)
            else:
                handleSensorType(self,top,0,floor,port)
        #Done---------------------------------------------
        def getSensorName(self,floor,port):
            topName = tk.Toplevel()
            topName.overrideredirect(0)
            topName.geometry("%dx%d+0+0" % (w, h))
            topName.focus_set()  # <-- move focus to this widget
            topName.bind("<Escape>", lambda e: e.widget.quit())
            topName.config(bg=BG)
            
            nameLabel = tk.Label(topName, text="Sensor Name",
                                font=large_font, bg=BG, fg=FG) 
            nameLabel.pack(pady=20)   
            e=Entry(topName, font=large_font,justify=CENTER,width=gridWidth*2)     
            e.pack(pady=20)
            
            submit = tk.Button(topName,bd=0,text="Done",font=large_font,bg=BG_R,
                fg=FG,command=lambda: handleSensorName(self,topName,e.get(),floor,port))
            submit.pack(pady=5)
        #Done---------------------------------------------
        def getSensorVoltage(self,nameTop,floor,port):
            nameTop.destroy()
            top = tk.Toplevel()
            top.overrideredirect(0)
            top.geometry("%dx%d+0+0" % (w, h))
            top.focus_set()  # <-- move focus to this widget
            top.bind("<Escape>", lambda e: e.widget.quit())
            top.title("Voltage")
            top.config(bg=BG)
            MODES=[("3.3v",3),("5v",5)]
            
            v = tk.IntVar()
            v.set(4)
            
            label = tk.Label(top, text="Sensor Voltage",
                        font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
            label.pack()     
            for text, mode in MODES:
                b = tk.Radiobutton(top,text=text,variable=v,value=mode,indicatoron=0,
                        command=lambda:handleSensorVoltage(self,top,v.get(),floor,port))
                b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth,height=gridHeight,font=large_font)
                b.pack(padx=5, pady=5)
                
                
        #def handleSensorOffset(self,top,floor,port):
        #    print("handleOffset") 
        #    value = RunProgram.readSensor(floor,port)
        #    getSensorOffset(self,floor,port,value):
        #   top.destroy()
               
                
        def getSensorOffset(self,floor,port,value):
            print("getSensorOffset")
            topOffset = tk.Toplevel()
            topOffset.overrideredirect(0)
            topOffset.geometry("%dx%d+0+0" % (w, h))
            topOffset.focus_set()  # <-- move focus to this widget
            topOffset.bind("<Escape>", lambda e: e.widget.quit())
            topOffset.config(bg=BG)
            
           
            
            label = tk.Label(topOffset, text="Sensor Offset",
                        font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
            label.pack(side = TOP)     
            
            topOffset.offset = Scale(topOffset,label="Sensor Value",font=mid_font,orient=HORIZONTAL,sliderlength=gridWidth*10,
                    length=gridWidth*100,fg=FG,bg=BG,bd=0,troughcolor=BG_R,
                    highlightthickness=0,width=gridWidth*6,to=60)     
            topOffset.offset.pack(pady=3,padx=3, side = TOP)
            topOffset.offset.set(topOffset)
            
            #submit = tk.Button(topOffset,bd=0,text="Set Offset",font=large_font,bg=BG_R,
            #    fg=FG,command=lambda: handleSensorOffset(self,topOffset,topOffset.offset.get(),floor,port))
            #submit.pack(pady=5)
            
            
        #Done---------------------------------------------
        def getSensorBias(self,floor,port):
           
            topBias = tk.Toplevel()
            topBias.overrideredirect(0)
            topBias.geometry("%dx%d+0+0" % (w, h))
            topBias.focus_set()  # <-- move focus to this widget
            topBias.bind("<Escape>", lambda e: e.widget.quit())
            topBias.title("Number of Pins")
            topBias.config(bg=BG)
            MODES=[("Pull Down",1),("Pull Up 5v",2),("Pull Up 3v",3),("None",7)]
            
            v = tk.IntVar()
            v.set(4)
            
            label = tk.Label(topBias, text="Bias Type",
                        font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
            label.pack()     
            for text, mode in MODES:
                b = tk.Radiobutton(topBias,text=text,variable=v,value=mode,indicatoron=0,
                        command=lambda:getBiasResistor(self,topBias,v.get(),floor,port))
                b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,height=gridHeight,font=large_font)
                b.pack(padx=5, pady=5)
        #Done---------------------------------------------
        def getBiasResistor(self,topBias,bias,floor,port):
            topBias.destroy()
            top = tk.Toplevel()
            top.overrideredirect(0)
            top.geometry("%dx%d+0+0" % (w, h))
            top.focus_set()  # <-- move focus to this widget
            top.bind("<Escape>", lambda e: e.widget.quit())
            top.title("Bias")
            top.config(bg=BG)
            MODE1 = [("100",6),("510",5),("1 k",4),("5.1 k",3),
                     ("10 k",2),("51 k",1),("100 k",0),("510 k",12),
                     ("1 M",11)]
            MODE2 = [("5.1 k",10),("51 k",9),("100 k",8)]
            MODE3 = [("5.1 k",15),("51 k",14),("100 k",13)]
            
            v = tk.IntVar()
            
            if bias is 7: resistorHandle(self,top,bias,floor,port)
                
            elif bias is 1:  
                v.set(10) 
                label = tk.Label(top, text="Pull Down Bias",
                            font=large_font,bg=BG,fg=FG,height=gridHeight) 
                label.pack(side=TOP)  
                for text, mode in MODE1:
                    b = tk.Radiobutton(top,text=text,variable=v,value=mode,indicatoron=0,
                            command=lambda: resistorHandle(self,top,v.get(),floor,port))
                    b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth,height=gridWidth,font=mid_font)
                    b.pack(padx=3, pady=5, side=LEFT, expand=True)
            elif bias is 2:  
                v.set(1)  
                label = tk.Label(top, text="Pull Up 5v Bias",
                            font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
                label.pack()  
                for text, mode in MODE2:
                    b = tk.Radiobutton(top,text=text,variable=v,value=mode,indicatoron=0,
                            command=lambda: resistorHandle(self,top,v.get(),floor,port))
                    b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,height=gridHeight,font=large_font)
                    b.pack(padx=5, pady=5)
            elif bias is 3:
                v.set(1)   
                label = tk.Label(top, text="Pull Up 3v Bias",
                            font=large_font,bg=BG,fg=FG,height=gridHeight*2) 
                label.pack()  
                for text, mode in MODE3:
                    b = tk.Radiobutton(top,text=text,variable=v,value=mode,indicatoron=0,
                        command=lambda: resistorHandle(self,top,v.get(),floor,port))
                    b.config(bg=BG_R,fg=FG,bd=0,width=gridWidth*2,height=gridHeight,font=large_font)
                    b.pack(padx=5, pady=5)
        #Done---------------------------------------------
        def resistorHandle(self,top,resistor,floor,port):
            if floor is 0:
                Template.PAR[port] = resistor
            elif floor is 2:
                Template.SAR[port] = resistor
            showSensors(self,top,floor)    
        #Done---------------------------------------------
        def handleSensors(self,sensorTop,floor,port):
            print("floor",floor,Template.PAP[port])
            if floor is 0:#Primary analog
                if Template.PAP[port] is 1:#Already selected
                    Template.PAP[port] = 0
                    Template.PAT[port] = 0
                    Template.PAV[port] = 0
                    Template.PAN[port] = ""
                    Template.PAR[port] = 0
                    showSensors(self,sensorTop,floor)
                else:
                    Template.PAP[port] = 1
                    getSensorType(self,floor,port)
                    sensorTop.destroy()
            if floor is 1:#Primary Digital
                if Template.PDP[port] is 1:#Already selected
                    Template.PDP[port] = 0
                    Template.PDN[port] = ""
                    showSensors(self,sensorTop,floor)
                else:
                    Template.PDP[port] = 1
                    getSensorName(self,floor,port) 
                    sensorTop.destroy()       
            if floor is 2:#Secondary analog
                if Template.SAP[port] is 1:#Already selected
                    Template.SAP[port] = 0
                    Template.SAT[port] = 0
                    Template.SAV[port] = 0
                    Template.SAN[port] = ""
                    Template.SAR[port] = 0
                    showSensors(self,sensorTop,floor)
                else:
                    Template.SAP[port] = 1
                    getSensorType(self,floor,port)
                    sensorTop.destroy()
            if floor is 3:#Secondary Digital
                if Template.SDP[port] is 1:#Already selected
                    Template.SDP[port] = 0
                    Template.SDN[port] = ""
                    showSensors(self,sensorTop,floor)
                else:
                    Template.SDP[port] = 1
                    getSensorType(self,floor,port)
                    sensorTop.destroy()          
            print("handleSensor")
        #Done---------------------------------------------
        def handleSensorVoltage(self,top,voltage,floor,port):
            if floor is 0:
                Template.PAV[port] = voltage
            elif floor is 2:
                Template.SAV[port] = voltage
            getSensorBias(self,floor,port)
            top.destroy() 
        #Done---------------------------------------------
        def handleSensorName(self,top,name,floor,port):
            if floor is 0: 
                Template.PAN[port] = name
                getSensorVoltage(self, top, floor, port)
            if floor is 1: 
                Template.PDN[port] = name
                showSensors(self,top,floor)
            if floor is 2: 
                Template.SAN[port] = name
                getSensorVoltage(self, top, floor, port)
            if floor is 3: 
                Template.SDN[port] = name
                showSensors(self,top,floor)
        #Done---------------------------------------------
        def handleSensorType(self,top,sensorType,floor,port):
            print("handleSensorType  ",self,top,sensorType,floor,port)
            if floor is 0:
                Template.PAT[port] = sensorType
            if floor is 2:
                Template.SAT[port] = sensorType
            getSensorName(self,floor,port)
            top.destroy()
        #Done---------------------------------------------
        def getProjectName(self):
            top = tk.Toplevel()
            top.overrideredirect(0)
            top.geometry("%dx%d+0+0" % (w, h))
            top.focus_set()  # <-- move focus to this widget
            top.bind("<Escape>", lambda e: e.widget.quit())
            top.config(bg=BG)
            
            emailLabel = tk.Label(top, text="Project Name",
                                font=large_font, bg=BG, fg=FG) 
            emailLabel.pack(pady=20)   
            e = Entry(top, font=large_font, justify=CENTER, width=gridWidth*2)     
            e.pack(pady=20)
            
            submit = tk.Button(top, bd=0, text="Start", font=large_font, bg=BG_R,
                    fg=FG, command=lambda: handleNewProject(self,top,e.get()))
            submit.pack(pady=5)
        #Done---------------------------------------------
        def handleNewProject(self,top,name):
            print("handleNewProject")
            global projName
            projName = name 
            buildOptions(self)
            top.destroy()
        #Done---------------------------------------------
        def handleTemplateSelection(self,top,i):
            global Template
            if i is 0: Template = Template1
            elif i is 1: Template = Template2
            elif i is 2: Template = Template0
            elif i is 3: Template = BuildSettings
            elif i is 4: Template = TurnOn
            
            print(Template)
            getProjectName(self) 
            top.destroy()   
        #Done---------------------------------------------
        
        
        def handleNewProgram(self,openingTop):
            print("handleNew")
            handleTemplateSelection(self,openingTop,1)
            
        def handleOldProgram(self,openingTop):
            print("handleOld")
            
            openingTop.destroy() 
                
        def handleTemplate(self,openingTop):
            print("handleTempalte")
            displayTemplates(self)
            openingTop.destroy()
    
    
app = ControlBox()
w, h =app.winfo_screenwidth(), app.winfo_screenheight()      
app.overrideredirect(0)
app.geometry("%dx%d+0+0" % (w, h))
app.focus_set()  # <-- move focus to this widget
app.bind("<Escape>", lambda e: e.widget.quit())
app.mainloop()
