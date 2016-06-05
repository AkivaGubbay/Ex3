from code.Global_Parameters import *
import math

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._zone = INFINITY() #temp value
        self._deviation = 0

    def joint(self, point1):
        if (point1.exists()==False): return

        if(point1._deviation > TRANSMISSION_RANGE() or point1._deviation == INFINITY()): return

        dis = Point.airDistance(self, point1._x, point1._y)
        if (self._deviation - dis - point1._deviation >= 0):  # point1 in self
            self._x = point1._x
            self._y = point1._y
            self._deviation = point1._deviation
        elif (point1._deviation - dis - self._deviation >= 0):  # self in point1
            return
        elif(dis>point1._deviation + self._deviation):#Error?
            if(point1._deviation < self._deviation):
                self._x = point1._x
                self._y = point1._y
                self._deviation = point1._deviation
        else: ###"Circles touching" - need to do Union:###
            # Calculating a straight line out of the two major circuits:
            # y = m1 * x +d1
            if(self._x-point1._x == 0): return
            m1 = +(0.0 + self._y-point1._y)/(self._x-point1._x)

            d1 = point1._y- m1*point1._x
            points1 = Point.getPoints(m1,d1,self._x, self._y,self._deviation)
            points2 = Point.getPoints(m1, d1, point1._x, point1._y, point1._deviation)

            # We got four points, taking the points most often:
            if(Point.airDistancePoints(points1[0], points2[0]) < Point.airDistancePoints(points1[0], points2[1])):
                points2.pop(1)
            else:
                points2.pop(0)

            if (Point.airDistancePoints(points2[0], points1[0]) < Point.airDistancePoints(points2[0], points1[1])):
                points1.pop(1)
            else:
                points1.pop(0)

            # Center the two points will be the new center:
            self._x = int((points1[0]._x + points2[0]._x)/2.0)
            self._y = int((points1[0]._y + points2[0]._y)/2.0)

            # Calculating the straight line parallel to and from taking the new circle radius:
            if(m1 == 0): return
            array = Point.getPoints(1.0/m1, self._x - self._y*1.0/m1,point1._x, point1._y,point1._deviation)
            self._deviation = int(math.fabs(Point.airDistancePoints(array[0], array[1]))/2.0)

    """Finding the intersection points between the straight line "y = mx + d"
    to the circle "(x-a)^2 + (x-b)^2 = (c)^2" """
    def getPoints(m,d, a,b,c):
        # y = mx + d
        #(x-a)^2 + (x-b)^2 = (c)^2

        xV2 = 1 +m*m
        xV1 = -2*a +2*m*d -2*b*m
        xV0 = a*a +b*b -c*c +d*d -2*b*d

        _sqrt = math.fabs((int(xV1*xV1 -4*xV2*xV0)))
        _sqrt = math.sqrt(_sqrt)
        sol_x_1 = (0.0+-xV1 + _sqrt)/(2*xV2)
        sol_x_2 = (0.0 + -xV1 - _sqrt) / (2 * xV2)

        sol_y_1 = sol_x_1 * m + d
        sol_y_2 = sol_x_2 * m + d

        p1 = Point(sol_x_1, sol_y_1)
        p2 = Point(sol_x_2, sol_y_2)
        return [p1,p2]

    def fillMatDistance(_mat_zone, array, startpoint):
        if (bool(ACTIVE_MATDISTANCE())==False): return
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

    def distance(_mat_zone, point1, point2):
        if (bool(ACTIVE_MATDISTANCE()) == False):
            return  Point.airDistancePoints(point1, point2)

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
        return '['+str(self._x)+', '+str(self._y)+'] dev =' +str(self._deviation)

    def airDistance(self, x2, y2):
        return math.sqrt((self._x - x2) * (self._x - x2) + (self._y - y2) * (self._y - y2))

    def airDistancePoints(p1, p2):
        return math.sqrt((p1._x - p2._x) * (p1._x - p2._x) + (p1._y - p2._y) * (p1._y - p2._y))

    # return Is it logical that a robot will be in this place
    def exists(self):
        bo1 = self._x>=0
        bo2 = self._x<ARENA_X()
        bo3 = self._y>=0
        bo4 = self._y<ARENA_Y()
        return (bo1 &bo2) & (bo3 & bo4)

    # return Is it logical that a robot will be in this place
    def existsXY(x1,y1):
        return Point(x1,y1).exists()

    # converter signal to Distance:
    def signalToDistance(signal):
        dis = (MAX_MSG_RANGE() - math.sqrt(math.fabs(signal)))
        if(dis<50): return int(50*(1+INSTANT_SENDING_CHANCE()))
        return int(math.fabs(dis) * (1+INSTANT_SENDING_CHANCE()))

    # Returns What direction is the point1 relative to self:
    def which_direction(self, point1):

        if(point1._deviation != INFINITY() and point1._deviation !=0):
            dis = Point.airDistance(self, point1._x, point1._y)
            if (self._deviation - dis - point1._deviation >= 0 or point1._deviation - dis - self._deviation >= 0):  # point1 in self or self in point1
                return INFINITY()

        if(self._x > point1._x):
            return LEFT()
        elif (self._x < point1._x):
            return RIGHT()
        elif (self._y < point1._y):
            return DOWN()
        else:
            return UP()



