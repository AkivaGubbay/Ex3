from code.Global_Parameters import *
import math


#TODO:
#Add field that says what area this point is in(white,black,gray).

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._zone = INFINITY() #temp
        self._deviation = 0

    def Joint(self, point1):
        dis = Point.airDistance(self, point1._x, point1._y)
        if(self._deviation - dis - point1._deviation >= 0): #point1 in self
            self._x = point1._x
            self._y = point1._y
            self._deviation = point1._deviation
        elif (point1._deviation - dis - self._deviation >= 0):  # self in point1
            return
        else:  # (There is a space between them cutting):
            bool1 = (self._x- self._deviation<=0) | (self._y- self._deviation<=0)
            bool2 = (point1._x- point1._deviation<=0) | (point1._y- point1._deviation<=0)
            bool3 = (self._x- self._deviation>=ARENA_X()-1) | (self._y- self._deviation>=ARENA_Y()-1)
            bool4 = (point1._x- point1._deviation>=ARENA_X()-1) | (point1._y- point1._deviation>=ARENA_Y()-1)
            if(bool1 | bool2 | bool3 | bool4): # Checks that the Circle does not come out from the field
                if(self._deviation> point1._deviation):
                    self._x = point1._x
                    self._y = point1._y
                    self._deviation = point1._deviation
            else: #A union between two circles



    def fillMatDistance(_mat_zone, array, startpoint):
        QueuePoint = []
        QueuePoint.append(startpoint)
        index = 0
        size = 1
        boo1 = len(QueuePoint) > 0
        boo2 = index < TRANSMISSION_RANGE()
        while (boo1 & boo2):
            if (size == 0):
                index = index + 1
                size = len(QueuePoint) - 1
            x = QueuePoint[0]._x
            y = QueuePoint[0]._y
            boolea1 = array[x][y] == INFINITY()
            boolea2 = QueuePoint[0].exists()
            boolea3 = _mat_zone[x][y] != BLACK()
            if (boolea1 & boolea2 & boolea3):
                array[x][y] = index
                QueuePoint.append(Point(x - 1, y))
                QueuePoint.append(Point(x + 1, y))
                QueuePoint.append(Point(x, y - 1))
                QueuePoint.append(Point(x, y + 1))
            QueuePoint.pop(0)
            boo1 = len(QueuePoint) > 0
            boo2 = index < TRANSMISSION_RANGE()
            size = size - 1

    def getMiddlePoint(_mat_zone, point1, point2):
        array1 = []
        for i in range(int(float(ARENA_Y()))):
            array1.append(int(ARENA_X()) * [INFINITY()])

        QueuePoint = []
        QueuePoint.append(point1)
        QueuePoint.append(point2)
        index = 0
        size = len(QueuePoint)
        boo1 = len(QueuePoint) > 0
        boo2 = index < TRANSMISSION_RANGE()
        while (boo1 & boo2):
            if (size == 0):
                index = index + 1
                size = len(QueuePoint) - 1
            x = QueuePoint[0]._x
            y = QueuePoint[0]._y
            if (array1[x][y] != INFINITY()):
                return QueuePoint[0]

            boolea1 = array1[x][y] == INFINITY()
            boolea2 = QueuePoint[0].exists()
            boolea3 = _mat_zone[x][y] != BLACK()
            if (boolea1 & boolea2 & boolea3):
                array1[x][y] = index
                QueuePoint.append(Point(x - 1, y))
                QueuePoint.append(Point(x, y - 1))
                QueuePoint.append(Point(x + 1, y))
                QueuePoint.append(Point(x, y + 1))
            QueuePoint.pop(0)
            boo1 = len(QueuePoint) > 0
            boo2 = index < TRANSMISSION_RANGE()
            size = size - 1
        return Point(INFINITY(), INFINITY())

    def distance(_mat_zone, point1, point2):
        array = []
        for i in range(int(float(ARENA_Y()))):
            array.append(int(ARENA_X()) * [INFINITY()])

        JOKER = -999
        array[point2._x][point2._y] = JOKER

        QueuePoint = []
        QueuePoint.append(point1)
        index = 0
        size = 1
        boo1 = len(QueuePoint) > 0
        boo2 = index < TRANSMISSION_RANGE()
        while (boo1 & boo2):
            if (size == 0):
                index = index + 1
                size = len(QueuePoint) - 1
            x = QueuePoint[0]._x
            y = QueuePoint[0]._y
            if(array[x][y] == JOKER):
                return index

            boolea1 = array[x][y] == INFINITY()
            boolea2 = QueuePoint[0].exists()
            boolea3 = _mat_zone[x][y] != BLACK()
            if (boolea1 & boolea2 & boolea3):
                array[x][y] = index
                QueuePoint.append(Point(x - 1, y))
                QueuePoint.append(Point(x + 1, y))
                QueuePoint.append(Point(x, y - 1))
                QueuePoint.append(Point(x, y + 1))
            QueuePoint.pop(0)
            boo1 = len(QueuePoint) > 0
            boo2 = index < TRANSMISSION_RANGE()
            size = size - 1

        return INFINITY()

    def getCuttingPoints(_mat_zone, point1, point2):
        return_Point = []
        array1 = []
        for i in range(int(float(ARENA_Y()))):
            array1.append(int(ARENA_X()) * [INFINITY()])

        QueuePoint = []
        QueuePoint.append(point1)
        #QueuePoint.append(point2)
        index = 0
        size = len(QueuePoint)
        boo1 = len(QueuePoint) > 0
        boo2 = index < TRANSMISSION_RANGE()
        while (boo1 & boo2):
            if (size == 0):
                index = index + 1
                size = len(QueuePoint) - 1
                if(len(return_Point)>0):
                    return return_Point
            x = QueuePoint[0]._x
            y = QueuePoint[0]._y
            if(array1[x][y] !=INFINITY()):
                return_Point.append(QueuePoint[0])
                if (len(return_Point) == 3):
                    return_Point.pop(1)
            boolea1 = array1[x][y] == INFINITY()
            boolea2 = QueuePoint[0].exists()
            boolea3 = _mat_zone[x][y] != BLACK()
            if (boolea1 & boolea2 & boolea3):
                array1[x][y] = index
                QueuePoint.append(Point(x - 1, y))
                QueuePoint.append(Point(x, y - 1))
                QueuePoint.append(Point(x + 1, y))
                QueuePoint.append(Point(x, y + 1))
            QueuePoint.pop(0)
            boo1 = len(QueuePoint) > 0
            boo2 = index < TRANSMISSION_RANGE()
            size = size - 1
        print("222222222222222222222222222222")
        return INFINITY()

    def toString(self):
        return '['+str(self._x)+', '+str(self._y)+']:' +str(self._zone)+'-' +str(self._deviation)

    def airDistance(self, x2, y2):
        return math.sqrt((self._x - x2) * (self._x - x2) + (self._y - y2) * (self._y - y2))

    def exists(self):
        bo1 = self._x>=0
        bo2 = self._x<ARENA_X()
        bo3 = self._y>=0
        bo4 = self._y<ARENA_Y()
        return (bo1 &bo2) & (bo3 & bo4)

    def existsXY(x1,y1):
        return Point(x1,y1).exists()




