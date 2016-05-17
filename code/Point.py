from code.Global_Parameters import *

#TODO:
#Add field that says what area this point is in(white,black,gray).

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def toString(self):
        return '('+str(self._x)+', '+str(self._y)+')'

    def airDistance(self, x2, y2):
        x_dis = self._x - x2
        if(x_dis<0): x_dis = x_dis*-1

        y_dis = self._y - y2
        if (y_dis < 0): y_dis = y_dis * -1

        return x_dis + y_dis

    def exists(x1,y1):
        bo1 = x1>=0
        bo2 = x1<ARENA_X()
        bo3 = y1>=0
        bo4 = y1<ARENA_Y()
        return (bo1 &bo2) & (bo3 & bo4)

    def toString(self):
        return "[" + str(self._x)+","+ str(self._y)+"]"




