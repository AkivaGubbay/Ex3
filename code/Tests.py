from tkinter import Radiobutton

from code.Point import Point
from code.Arena import Arena
from code.Robot import Robot
from code.Log import Log
from code.Simulation import Simulation
from code.Message import Message
from code.Global_Parameters import *

#Tests parameter class:
def globalParametersTest():
    readParameters()
    print("**********************globalParametersTest*****************************************")
    print("BATTARY_CAPACITY", BATTARY_CAPACITY())
    print("TRANSMISSION_RANGE", TRANSMISSION_RANGE())
    print("ROBOTS_NOT_MOVE", ROBOTS_NOT_MOVE())
    print("ROBOTS_MOVE", ROBOTS_MOVE())
    print("ARENA_X", ARENA_X())
    print("ARENA_Y", ARENA_Y())
    print("BLACK_AREA", BLACK_AREA())
    print("GRAY_AREA", GRAY_AREA())
    print("LOG_FILE_DIRECTORY", "|" + LOG_FILE_DIRECTORY() + "|")
    print("WHITE", WHITE()), print("GRAY", GRAY()), print("BLACK", BLACK())
    print("OLDER", OLDER()), print("SAME_AGE", SAME_AGE()), print("YOUNGER", YOUNGER())
    print("CURRENT", CURRENT()), print("UP", UP()), print("LEFT", LEFT()), print("DOWN", DOWN()), print("RIGHT",RIGHT())
    print("INSTANT_SENDING_CHANCE", INSTANT_SENDING_CHANCE())
    print("MAX_NUM_OF_VERSIONS", MAX_NUM_OF_VERSIONS())
    print("MESSAGE_LIFE_TIME", MESSAGE_LIFE_TIME())




globalParametersTest()
#log
Mylog = Log()
s = Simulation()

Message1 = Message(33,"akiva3")
s._Air.transmit_Message(Message1)
Message2 = Message(65,"zvika222")
s._Air.transmit_Message(Message2)
print(s._Air.toString_Messages())
s._Air.Deleting_old_messages()
Message3 = s._Air.transmit_Message_again(Message2)
print(s._Air.toString_Messages())
s._Air.Deleting_old_messages()
s._Air.Deleting_old_messages()

Mylog.close()