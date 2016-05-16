from tkinter import Radiobutton

from code.Point import Point
from code.Zone import Zone
from code.Robot import Robot
from code.log import log
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
Mylog = log()

#test Simulation:
s = Simulation(Mylog)

Message1 = Message(33,"akiva3")
s.transmit_Message(Message1)
Message2 = Message(65,"zvika222")
s.transmit_Message(Message2)
print(s.toString_Messages())
s.Deleting_old_messages()
Message3 = s.transmit_Message_again(Message2)
print(s.toString_Messages())
s.Deleting_old_messages()
s.Deleting_old_messages()
s.gui()


#Test Zone:
#print('Test Zone:')
#z=Zone(Mylog)
#z.PrintRobot_By_XY()
#z.PrintType_by_XY()

Mylog.close()
print()
print("*******************************************************")
r1 = Robot(860)
m1 = Message(000,"Joey: Hey, how you do'n..")
r1.messages.append(m1)
print("have message? ",r1.haveMessage(m1))
print("have message? ",r1.haveMessage("see the bombers.."))
