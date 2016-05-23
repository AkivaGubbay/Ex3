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
        Air.static_mat_zone = self._Arena._mat_zone
        """
        #test:
        self._Air.transmit_Message(Message("abcde", 11))
        self._Air._messages[0]._real_location = self._Arena._Robots[11]._real_location


        test::

        point0 = Point(500,500)

        print("to 500, 500: ")
        print(self._Air._messages[0]._real_location.toString())
        print(self._Arena.distance(self._Air._messages[0], point0))
        print("to 500, 500 end")"""

        """ <<<   Here should be the "MAIN FOR" Of the project   >>> """
        """point1 = Point(100,100)
point1._deviation = 200

point2 = Point(105,105)
point2._deviation = 350

print("distance: "+ str(Point.distance(self._Arena._mat_zone, point1,point2)))
return_Point = Point.getCuttingPoints(self._Arena._mat_zone, point1, point2)
print("cuttingPoints: " + return_Point[0].toString() + return_Point[1].toString())
point2.Joint(self._Arena._mat_zone, point1)
print("Joint: " + point2.toString())"""


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
        plt.show()


