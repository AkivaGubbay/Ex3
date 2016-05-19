from code.Global_Parameters import *

#TODO:
#Add field that says what area this point is in(white,black,gray).

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._zone = INFINITY() #temp
        self._deviation = 0

    """def Joint(self, point1):
        if(self inside in point1): return
        elif(point1 inside self):
            self._x = point1._x
            self._y = point1._y
            self._zone = point1._zone

        elif(There is a space between them cutting):
            # Need to find a cutting point and create a new circle
        """


    def toString(self):
        return '('+str(self._x)+', '+str(self._y)+')'

    def airDistance(self, x2, y2):
        x_dis = self._x - x2
        if(x_dis<0): x_dis = x_dis*-1

        y_dis = self._y - y2
        if (y_dis < 0): y_dis = y_dis * -1

        return x_dis + y_dis

    def exists(self):
        bo1 = self._x>=0
        bo2 = self._x<ARENA_X()
        bo3 = self._y>=0
        bo4 = self._y<ARENA_Y()
        return (bo1 &bo2) & (bo3 & bo4)

    def existsXY(x1,y1):
        return Point(x1,y1).exists()

    def toString(self):
        return "[" + str(self._x)+","+ str(self._y)+"]"




