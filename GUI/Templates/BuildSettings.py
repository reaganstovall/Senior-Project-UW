#!/usr/bin/python
#Template file for Automation Station

__template__ = "BuildSettings"
__author__ = "Reagan Stovall"
__copyright__ = "Copyright 2017, Open Source"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Reagan Stovall"
__email__ = "john1988@uw.edu"
__status__ = "Development"
__description__ = "This is a sample Template to measure the temperature and turn on a fan if over a value"


TempOffset = (0,0)
LightOffset = (0,0)
HumidityOffset = (0,0)
MoistureOffset = (0,0)



PAP = [0, 0, 0, 0, 0, 0, 0, 0]
PAT = [0, 0, 0, 0, 0, 0, 0, 0]
PAV = [0, 0, 0, 0, 0, 0, 0, 0]
PAN = ["","","","","","","",""]
PAR = [0, 0, 0, 0, 0, 0, 0, 0]
PAO = [0, 0, 0, 0, 0, 0, 0, 0]
PDP = [0, 0, 0, 0, 0, 0, 0, 0]
PDN = ["","","","","","","",""]

SAP = [0, 0, 0, 0, 0, 0, 0, 0]
SAT = [0, 0, 0, 0, 0, 0, 0, 0]
SAV = [0, 0, 0, 0, 0, 0, 0, 0]
SAN = ["","","","","","","",""]
SAR = [0, 0, 0, 0, 0, 0, 0, 0]
SDP = [0, 0, 0, 0, 0, 0, 0, 0]
SDN = ["","","","","","","",""]

PMP = [0, 0, 0, 0, 0, 0, 0, 0]
PMT = [0, 0, 0, 0, 0, 0, 0, 0]
PMS = [0, 0, 0, 0, 0, 0, 0, 0]
PMN = ["","","","","","","",""]
SMP = [0, 0, 0, 0, 0, 0, 0, 0]
SMT = [0, 0, 0, 0, 0, 0, 0, 0]
SMS = [0, 0, 0, 0, 0, 0, 0, 0]
SMN = ["","","","","","","",""]

PR12P = [0, 0, 0, 0, 0, 0, 0, 0]
PR12N = ["","","","","","","",""]

PRACP = [0, 0, 0, 0, 0, 0, 0, 0]
PRACN = ["","","","","","","",""]

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
#3. Action:     (0: Unused, 1: Regular forward, 2:Bi-directional forward, 3: Bi- Reverse, 4:Relay On, 5:Relay Off
#4. operator:   (0: Unused, 1: Greater than, 2: LesserThan, 3: Closed, 4: Open))
#5. Comparator: (0: no comparator, 1: digital low, 2: digital high, anything else:int)
#6. SensorID:   (a1,a2) where (a1:(0:Unused, 1:PAP, 2:PDP, 3:SAP, 4:SDP), a2:(port)) 
#7. Duration:   (0) Duration that HW perfoms action  
FNC_List = []


#Function Name
FNC_Names = []



