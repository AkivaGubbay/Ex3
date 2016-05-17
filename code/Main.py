from tkinter import Radiobutton

from code.Point import Point
from code.Arena import Arena
from code.Robot import Robot
from code.Log import Log
from code.Simulation import Simulation
from code.Message import Message
from code.Global_Parameters import *

readParameters()

"""
#Test Point:
print('Test Point:')
p = Point(4,3)
print(p.toString())

#Test Robot:
print('Test Robot:')
r = Robot(12)
print('initial battery: '+str(r.battery_status))
r.messages.append('Joey: How you doing..')
print(r.messages.pop())
print("tostring: "+ r.toString())
"""


#log
Mylog = Log()

#test Simulation:
s = Simulation()

s.showGUI()
print(s._Arena.getEnv(22))
