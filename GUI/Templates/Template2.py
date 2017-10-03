#!/usr/bin/python
#Template file for Automation STation

__template__ = "Template1"
__author__ = "Reagan Stovall"
__copyright__ = "Copyright 2017, Open Source"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Reagan Stovall"
__email__ = "john1988@uw.edu"
__status__ = "Development"
__description__ = "This is a sample Template to measure the temperature and turn on a fan if over a value"


TempOffset = (0,100)
LightOffset = (0,100)
HumidityOffset = (0,100)
MoistureOffset = (0,100)


PAP = [1, 0, 1, 0, 1, 0, 1, 0]
PAT = [1, 0, 1, 0, 1, 0, 2, 0]
PAV = [3, 0, 5, 0, 3, 0, 5, 0]
PAN = ["PTemp1","","PTemp2","","PTemp3","","PTemp4",""]
PAR = [2, 0, 3, 0, 4, 0, 5, 0]
PAO = [23, 0, -12, 0, 23, 0, 18, 0]
PDP = [1, 0, 1, 0, 1, 0, 1, 0]
PDN = ["PSwitch1","","PSwitch3","","PSwitch4","","PSwitch5",""]

SAP = [0, 0, 0, 0, 0, 0, 0, 0]
SAT = [0, 0, 0, 0, 0, 0, 0, 0]
SAV = [0, 0, 0, 0, 0, 0, 0, 0]
SAN = ["","","","","","","",""]
SAR = [0, 0, 0, 0, 0, 0, 0, 0]
SDP = [0, 0, 0, 0, 0, 0, 0, 0]
SDN = ["","","","","","","",""]

PMP = [1, 0, 1, 1, 0, 0, 0, 0]
PMT = [1, 0, 2, 3, 0, 0, 0, 0]
PMS = [1, 0, 2, 0, 0, 0, 0, 0]
PMN = ["PM1","","PM3","","","","",""]

SMP = [0, 0, 0, 0, 0, 0, 0, 0]
SMT = [0, 0, 0, 0, 0, 0, 0, 0]
SMS = [0, 0, 0, 0, 0, 0, 0, 0]
SMN = ["","","","","","","",""]

PR12P = [1, 0, 1, 0, 0, 0, 0, 0]
PR12N = ["","","","","","","",""]

PRACP = [1, 0, 1, 0, 0, 0, 0, 0]
PRACN = ["PRAC_1","","PRAC_3",""]

SR12P = [0, 0, 0, 0, 0, 0, 0, 0]
SR12N = ["","","","","","","",""]

SRACP = [0, 0, 0, 0, 0, 0, 0, 0]
SRACN = ["","","","","","","",""]
#functionList is one large list with tuples of 8 values 
#0. StartTime, 1. EndTime, 2. HWID, 3. Direction, 4. operator, 5. Comparator, 6. Sensor   7. Duration
#(( (Seconds), (Seconds),  (int,int),   (int),        (int),         (int),    (int,int),      (int)), (tuple2), (.ect))

#0. StartTime:  (0) Start from beginning 
#1. EndTime:    (0) Till the end of the Program once started
#2. HardwareID: (a1,a2) where (a1:(0:Unused, 1:PMP, 2:SMP, 3:PR12P, 4:PRACP, 5:SR12P, 6:SRACP), a2:(port)) 
#3. Action:     (0: Unused, 1: Regular direction, 2:Opposite Only for Bi-directional motors)
#4. operator:   (0: Unused, 1: Greater than, 2: LesserThan, 3: Closed, 4: Open))
#5. Comparator: (0: no comparator, 1: digital low, 2: digital high, anything else:int)
#6. SensorID:   (a1,a2) where (a1:(0:Unused, 1:PAP, 2:PDP, 3:SAP, 4:SDP), a2:(port)) 
#7. Duration:   (0) Duration that HW perfoms action  
FNC_List = [(123123,14234234,(0,0),0,0,0,(0,0),0),(123123,14234234,(0,0),0,0,0,(0,0),0),(123123,14234234,(0,0),0,0,0,(0,0),0),(123123,14234234,(0,0),0,0,0,(0,0),0)]

#Function Name
FNC_Names = ["First","Second","Third","Fourth"]

TMM = []



