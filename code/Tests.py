from tkinter import Radiobutton

from code.Point import Point
from code.Arena import Arena
from code.Robot import Robot
from code.Log import Log
from code.Simulation import Simulation
from code.Message import Message
from code.Global_Parameters import *
#MUST HAVE:
readParameters()
Mylog = Log()

#Tests parameter class:
def globalParametersTest():
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
    print("UP", UP()), print("LEFT", LEFT()), print("DOWN", DOWN()), print("RIGHT",RIGHT())
    print("INSTANT_SENDING_CHANCE", INSTANT_SENDING_CHANCE())
    print("MAX_NUM_OF_VERSIONS", MAX_NUM_OF_VERSIONS())
    print("MESSAGE_LIFE_TIME", MESSAGE_LIFE_TIME())
    print("ROBOT_LEANGHT", ROBOT_LEANGHT())


#Tests Robot class:
def RobotTest():
    r1 = Robot(0)
    print(r1._id)
    Robot.static_arena = Arena()
    #Env:
    env = r1.getEnv()
    print("getEnv: ",env)
    #move:
    r1.move(UP())
    r1.move(LEFT())
    r1.move(UP())
    r1.move(LEFT())
    for i in r1._private_location_log: print(i.toString()+", ")
    #when checkied this.. add random directions for move



RobotTest()



Mylog.close()