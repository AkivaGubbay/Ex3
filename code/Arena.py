from code.Global_Parameters import *
from code.Robot import Robot
from random import randint
from code.Log import Log
from code.Point import Point

import random

class Arena:
    _mone_move =0
    def __init__(self):
        self._mat_robot_id = []
        self._Robots = []
        self._Robots_sort_Random = []
        self._mat_zone = [] #by color (white = 0    gray = 1     black = 2)

        for i in range(int(float(ARENA_X()))):
            self._mat_robot_id.append(int(ARENA_Y())*[-1])
            self._mat_zone.append(int(ARENA_Y())*[WHITE()])

        # Mark gray areas:
        Gray_area_point = GRAY_AREA()
        for b in range(len(Gray_area_point)):
            Log.addLine("create gray area point between: "+str(Gray_area_point[b]))
            for i in range(Gray_area_point[b][0], Gray_area_point[b][2]+1):
                for j in range(Gray_area_point[b][1], Gray_area_point[b][3]+1):
                    self._mat_zone[i][j] = GRAY()


        # Mark black areas:
        black_area_point = BLACK_AREA()
        for b in range(len(black_area_point)):
            Log.addLine("create black area point between: " + str(black_area_point[b]))
            for i in range(black_area_point[b][0], black_area_point[b][2]+1):
                for j in range(black_area_point[b][1], black_area_point[b][3]+1):
                    self._mat_zone[i][j] = BLACK()

        # Creates a new robot 'that can move' to variable "Robots"
        for s in range(0, int(ROBOTS_MOVE())):
            self._Robots.append(Robot(s))
            self._Robots_sort_Random.append(s)
            Log.addLine("create new Robot- " + self._Robots[s].toString())

        # Creates a new robot 'that can't move' to variable "Robots"
        for s in range(int(ROBOTS_MOVE()), int(ROBOTS_MOVE())+int(ROBOTS_NOT_MOVE())):
            self._Robots.append(Robot(s))
            self._Robots_sort_Random.append(s)
            self._Robots[s]._can_move = False

            Log.addLine("create new Robot- " + self._Robots[s].toString())

        #put the robots on Arena:
        for s in range(0, len(self._Robots)):
            x = randint(1, int(ARENA_X()) - 2)
            y = randint(1, int(ARENA_Y()) - 2)
            bool1 = self._mat_robot_id[x][y]!=-1
            bool2 = self._mat_zone[x][y] == BLACK()
            bool3 = self._Robots[s]._can_move == False
            bool4 = self._mat_zone[x][y] != WHITE()
            while((bool1 |bool2 ) | (bool3 & bool4)):
                x = randint(1, ARENA_X() - 2)
                y = randint(1, ARENA_Y() - 2)
                bool1 = self._mat_robot_id[x][y] != -1
                bool2 = self._mat_zone[x][y] == BLACK()
                bool3 = self._Robots[s]._can_move == False
                bool4 = self._mat_zone[x][y] != WHITE()

            self._Robots.append(Robot(s))
            self._mat_robot_id[x][y] = self._Robots[s]._id
            self._Robots[s]._real_location = Point(x, y)
            #self._Robots_sort_Random[s]._real_location = Point(x, y)
            if(bool3): #self._Robots[s]._can_move == False
                self._Robots[s]._estimated_location = Point(x, y)
                self._Robots[s]._estimated_location._deviation = 0
            Log.addLine("put Robot_" + str(self._Robots[s]._id) + self._Robots[s]._real_location.toString())

        self.sortRandomRobotsArray()

    """Returns the robot can he move forward(UP, DOWN, LEFT,RIGHT)
    Assumes that that the location of the robot's true, namely:  x>0, y>o, x<ARENA_X(), y<ARENA_Y()-1"""
    def getEnv(self, id):
        x = self._Robots[id]._real_location._x
        y = self._Robots[id]._real_location._y
        array = [True,True,True,True]

        if (Point.existsXY(x, y-1) == False or y-1 ==0):
            array[UP()] = False
        elif(self._mat_robot_id[x][y-1]!=-1 | self._mat_zone[x][y-1]):
            array[UP()] =False

        if (Point.existsXY(x, y+1) == False or y+1 != ARENA_Y()-1):
            array[DOWN()] = False
        elif(self._mat_robot_id[x][y+1]!=-1 | self._mat_zone[x][y+1]):
            array[DOWN()] =False

        if (Point.existsXY(x - 1, y) == False or x-1 ==0):
            array[LEFT()] = False
        elif(self._mat_robot_id[x-1][y]!=-1 | self._mat_zone[x-1][y]):
            array[LEFT()] =False

        if(Point.existsXY(x+1, y) == False or x+1 != ARENA_X()-1):
            array[RIGHT()] = False
        elif(self._mat_robot_id[x+1][y]!=-1 | self._mat_zone[x+1][y]):
            array[RIGHT()] =False

        return array

    """Returns the point where the robot is currently"""
    def getCurrentZone(self,id):
        x = self._Robots[id]._real_location._x
        y = self._Robots[id]._real_location._y

        return self._mat_zone[x][y]

    def moveRobot(self,id, direction):
        array = self.getEnv(id)
        if(array[direction]==False):
            return False
        else:
            Arena._mone_move +=1
            x = self._Robots[id]._real_location._x
            y = self._Robots[id]._real_location._y
            self._mat_robot_id[x][y]=-1

            tolog = ""
            if(direction == UP()):
                tolog = ("Robot " + str(id) + ": move UP From [" + str(x) + "][" + str(y) + "] to [" + str(x) + "][" + str(y-1) + "]")
                y = y - 1
            elif(direction == DOWN()):
                tolog =("Robot " + str(id) + ": move DOWN From [" + str(x) + "][" + str(y) + "] to [" + str(x) + "][" + str(y+1) + "]")
                y = y + 1
            elif (direction == LEFT()):
                tolog =("Robot " + str(id) + ": move LEFT From [" + str(x) + "][" + str(y) + "] to [" + str(x-1) + "][" + str(y) + "]")
                x = x - 1
            else:
                tolog =("Robot " + str(id) + ": move RIGHT From [" + str(x) + "][" + str(y) + "] to [" + str(x+1) + "][" + str(y) + "]")
                x = x + 1

            Log.addLine(tolog)
            #print(tolog)
            self._mat_robot_id[x][y] = id
            self._Robots[id]._real_location = Point(x,y)

            return True

    def sortRandomRobotsArray(self):
        for i in range(len(self._Robots_sort_Random)):
            sw = random.randint(0,len(self._Robots_sort_Random)-1)
            temp = self._Robots_sort_Random[sw]
            self._Robots_sort_Random[sw] = self._Robots_sort_Random[i]
            self._Robots_sort_Random[i] = temp






