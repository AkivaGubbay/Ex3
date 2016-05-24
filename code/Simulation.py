from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Air import Air
from code.Log import Log

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button



import matplotlib.cm as cm

class Simulation:
    __self = -1
    def __init__(self):
        Log.addLine("create Simulation")
        self._Air = Air()
        self._Arena = Arena()
        Air.static_mat_zone = self._Arena._mat_zone
        Simulation.__self = self
        self._time = 0
        self.Messages_mone = 0


        Robot.static_arena = self._Arena  # Must give the static_arena a value!!!
        Robot.static_air = self._Air  # Must give the static_air a value!!!

    def showGUI(self):
        X = []
        for i in range(int(ARENA_X())):
            line = int(ARENA_Y())*[-1]
            X.append(line)

        for i in range(int(ARENA_X())):
            for j in range(int(ARENA_Y())):
                if(X[i][j] != -1): continue

                if(self._Arena._mat_robot_id[i][j]!=-1):
                    X[i][j] = -1000
                    for i2 in range(i-ROBOT_LEANGHT(), i+ROBOT_LEANGHT()):
                        for j2 in range(j - ROBOT_LEANGHT(), j + ROBOT_LEANGHT()):
                            if(Point.existsXY(i2,j2)):
                                X[i2][j2] = -1000

                elif (self._Arena._mat_zone[i][j] == 2):
                    X[i][j] = 1000
                elif (self._Arena._mat_zone[i][j] == 1):
                    X[i][j] = 500
                elif (self._Arena._mat_zone[i][j] == 0):
                    X[i][j] = 0

        fig, ax = plt.subplots()
        ax.imshow(X, cmap='RdGy', interpolation='nearest')

        callback = self

        Msg1_loc = plt.axes([0.1, 0.95, 0.85, 0.045])
        Msg1 = Button(Msg1_loc, "Time= "+str(self._time) + ",   Robot moved= "+str(Arena._mone_move) + ",    Messages mone = " + str(self.Messages_mone))

        #button1:
        butt1_loc = plt.axes([0.1, 0.001, 0.25, 0.065])
        butt1 = Button(butt1_loc, str(BUTTON_NUMBER_1())+' step forward')
        butt1.on_clicked(callback.actionButton1)

        # button2:
        butt2_loc = plt.axes([0.4, 0.001, 0.25, 0.065])
        butt2 = Button(butt2_loc, str(BUTTON_NUMBER_2()) +' step forward')
        butt2.on_clicked(callback.actionButton2)

        ##button3:
        butt3_loc = plt.axes([0.7, 0.001, 0.25, 0.065])
        butt3 = Button(butt3_loc, str(BUTTON_NUMBER_3()) +' step forward')
        butt3.on_clicked(callback.actionButton3)

        plt.show()

    def actionButton1(self, event):
        self.action(BUTTON_NUMBER_1())

    def actionButton2(self, event):
        self.action(BUTTON_NUMBER_2())

    def actionButton3(self, event):
        self.action(BUTTON_NUMBER_3())

    def action(self, time):
        size = len (Simulation.__self._Arena._Robots_sort_Random)
        for t in range(0, time):
            self._time += 1
            Log.addLine("\n\n####    Simulation: Time = " + str(self._time) +"   ####")
            print("\n\n####    Simulation: Time = " + str(self._time) +"   ####")
            Simulation.__self._Arena.sortRandomRobotsArray()
            for i in range(0, size):
                robot = self._Arena._Robots_sort_Random[i]
                robot._time = self._time
                robot._current_zone = self._Arena.getEnv(robot._id)

                robot.doAction()
        self.Messages_mone +=len(Air._messages)
        Air._messages = []

        #plt.close()
        self.showGUI()




