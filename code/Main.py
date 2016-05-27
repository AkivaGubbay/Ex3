from tkinter import Radiobutton

from code.Point import Point
from code.Arena import Arena
from code.Robot import Robot
from code.Log import Log
from code.Simulation import Simulation
from code.Message import Message
from code.Global_Parameters import *
import webbrowser


#MUST HAVE:
readParameters()
Mylog = Log()



s = Simulation()
s.showGUI()

Mylog.close()

webbrowser.open("LogFile.txt")

