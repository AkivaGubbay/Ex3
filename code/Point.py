#TODO:
#Add field that says what area this point is in(white,black,gray).

class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y     #self.x = x,  self.y = y.

    def toString(self):
        return '('+str(self.x)+', '+str(self.y)+')'


