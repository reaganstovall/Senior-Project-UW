#!/usr/bin/python
#Template file for Automation STation
from array import array

__author__ = "Reagan Stovall"
__copyright__ = "Copyright 2017, Open Source"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Reagan Stovall"
__email__ = "john1988@uw.edu"
__status__ = "Development"

##sensorActive = [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
##sensorType = [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
##sensorPin = [3,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0]
sensorVoltage = [5,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0]
##sensorResistor = [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0]

#Primary Analog Port (0 or 1)
PAP = [1, 0, 0, 0, 0, 0, 0, 1]

#Primary Analog Type (0:Temp,1:hydra,2... this is arbitrary to what we want)
PAT = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary Analog Name
PAN = ["","","","","","","",""]
PAV = [3, 0, 0, 0, 0, 0, 0, 5]

#Primary Analog Resistor
#pulldowns(0:cap, 1:100, 2:510, 3:1k, 4:5.1K, 5:10K, 6:51K, 7:100K, 8:510K, 9:1M)
#5v pullup(10:5.1K, 11:51K, 12:100K)
#3V pullup(13:5.1K, 14:51K, 15:100K)
PAR = [7, 0, 0, 0, 0, 0, 0, 3]

#Primary Digital Port (0 or 1)
PDP = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary Digital Name
PDN = ["","","","","","","",""]

#Secondary
SAP = [0, 0, 0, 0, 0, 0, 0, 0]
SAT = [0, 0, 0, 0, 0, 0, 0, 0]
SAN = ["","","","","","","",""]
SAR = [0, 0, 0, 0, 0, 0, 0, 0]
SDP = [0, 0, 0, 0, 0, 0, 0, 0]
SDN = ["","","","","","","",""]

#Primary Motor Port (0 or 1)
PMP = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary Motor Type (0:unused, 1:singleDirection, 2:Bidirectional with the 
#next port as the return, 3:connected with the previous Bidirectional)
PMT = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary Motor Speed (will only use if we set up multi processing)
PMS = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary Motor Name
PMN = ["","","","","","","",""]

#Secondary Motors
SMP = [0, 0, 0, 0, 0, 0, 0, 0]
SMT = [0, 0, 0, 0, 0, 0, 0, 0]
SMS = [0, 0, 0, 0, 0, 0, 0, 0]
SMN = ["","","","","","","",""]

#Primary 12V Relay Ports, only the first 4 used
#the extras in the array are for legacy code that I haven't updated
PR12P = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary 12V Relay Names
PR12N = ["","","","","","","",""]

#Primary AC Relay Ports
PRACP = [0, 0, 0, 0, 0, 0, 0, 0]

#Primary AC Relay Names
PRACN = ["","","","","","","",""]

#SEcondary Relays
SR12P = [0, 0, 0, 0, 0, 0, 0, 0]
SR12N = ["","","","","","","",""]

SRACP = [0, 0, 0, 0, 0, 0, 0, 0]
SRACN = ["","","","","","","",""]

#functionList are sets of tuples of 7 

#1. StartTime,    2. EndTime,   3. HWID,  4. Direction, 5. operator, 6. Comparator, 7. Sensor 
#(((int,int,int), (int,int,int), (int,int),   (int),        (int),         (int),    (int,int)

#0. StartTime:  (0,0,0) start from beginning 
#1. EndTime:    (0,0,0) Till the end of the Program once started
#2. HardwareID: (a1,a2) where (a1:(0:Unused, 1:PMP, 2:SMP, 3:PR12P, 4:PRACP, 5:SR12P, 6:SRACP), a2:(port)) 
#3. Direction:  (0: Unused(Off for regular), 1: Regular direction, 2:Bi-directional forward, 3:Bi-directional reverse, 4:Relay on, 5:Relay off)
#4. operator:   (0: Unused, 1: Greater than, 2: LesserThan)
#5. Comparator: (0: no comparator, 1: digital low, 2: digital high, anything else:int)
#6. SensorID:   (a1,a2) where (a1:(0:Unused, 1:PAP, 2:PDP, 3:SAP, 4:SDP), a2:(port)) 
FNC_List = [(1,10,(4,5),4,1,10,(1,0)),(100,1000,0,0,1,10,(1,7))]
#Function Names
FNC_Names = ["first","second"]

TMM = []
