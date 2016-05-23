from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Air import Air
from code.Log import Log
import math
import random

readParameters()
Mylog = Log()

"""p1 = Point(100,100)
p1._deviation = 100
print(p1.toString())

p2 = Point(30,70)
p2._deviation = 40
print(p2.toString())

p1.Joint(p2)
print(p1.toString())"""


print(Point.signalToDistance(450*450))