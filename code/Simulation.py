from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Air import Air
from code.Log import Log

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Simulation:
    def __init__(self):
        Log.addLine("create Simulation")
        self._Air = Air()
        self._Arena = Arena()

        """ <<<   Here should be the "MAIN FOR" Of the project   >>> """

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
                            if(Point.exists(i2,j2)):
                                X[i2][j2] = -1000

                elif (self._Arena._mat_zone[i][j] == 2):
                    X[i][j] = 1000
                elif (self._Arena._mat_zone[i][j] == 1):
                    X[i][j] = 500
                elif (self._Arena._mat_zone[i][j] == 0):
                    X[i][j] = 0

        fig, ax = plt.subplots()
        ax.imshow(X, cmap='RdGy', interpolation='nearest')
        plt.show()


