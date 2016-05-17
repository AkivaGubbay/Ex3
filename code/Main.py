from tkinter import Radiobutton

from code.Point import Point
from code.Arena import Arena
from code.Robot import Robot
from code.Log import Log
from code.Simulation import Simulation
from code.Message import Message
from code.Global_Parameters import *
readParameters()
Mylog = Log()



#test Simulation:
s = Simulation()
s.showGUI()

Message("222",11)
Message("222",5)
Message("222",1)












Mylog.close()

