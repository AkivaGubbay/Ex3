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
        #axprev = plt.axes([0.1, 0.001, 0.1, 0.065])
        axnext = plt.axes([0.71, 0.001, 0.25, 0.065])
        bnext = Button(axnext, 'One step forward')
        bnext.on_clicked(callback.oneAction)
        #bprev = Button(axprev, 'Previous')
        #bprev.on_clicked(callback.oneAction)

        plt.show()


    """def action(self, time):
        size = len (self._Arena._Robots_sort_Random)
        for t in range(0, time):
            self._Arena.sortRandomRobotsArray()
            for i in range(0, size):
                self._Arena._Robots_sort_Random[i].doAction()
        self._Air._messages = []
        plt.show()"""

    def oneAction(self, event):
        size = len (Simulation.__self._Arena._Robots_sort_Random)
        self._time += 1
        for t in range(0, 1):
            Simulation.__self._Arena._Robots_sort_Random[i]._time = self._time
            Simulation.__self._Arena.sortRandomRobotsArray()
            for i in range(0, size):
                Simulation.__self._Arena._Robots_sort_Random[i].doAction()
        self._Air._messages = []




