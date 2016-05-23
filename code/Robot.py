from code.Point import *
from code.Global_Parameters import *
from random import randint
#chnage is good.
class Robot:
    static_arena = -1

    def __init__(self, id):
        self._id = id
        self._can_move = True
        self._battery_status = BATTARY_CAPACITY()
        self._private_location = Point(0,0)
        self._real_location = Point(0,0) #later put real location.
        self._message_log = []          #All received messages
        self._private_location_log = [Point(0,0)] #Holds all the robots movements as list of points
        self._neighbors_color = []      #Can save all his neighbors colors
        self._neighbors_list = []
        self._out_book = []             #Messages waiting to be sent.
        self._time = -1                 #Robots always knows the time.
        self._currently_sending = -1
        self._currently_get_message = -1
        self._current_zone = -1
        self._distance_from = [-1]*(ROBOTS_MOVE()+ROBOTS_NOT_MOVE())#I want to fill the whole list with -1 but i dont knot how many neighbors..


    #Robot asks 'Arena' in witch directions can he move.
    def getEnv(self):
        return Robot.static_arena.getEnv(self._id)


    # Robot moves in given 'direction',
    # updates his 'private_location', 'private_location_log',
    # and calls 'Arena' to update 'real location'.
    def move(self,direction):
        x = self._private_location._x
        y = self._private_location._y
        if direction == UP() : y += 1
        elif direction == LEFT() : x += -1
        elif direction == DOWN() : y += -1
        elif direction == RIGHT() : x += 1
        #Update _private_location:d
        self._private_location = Point(x,y)
        #Add to robots new _private_location to log:
        self._private_location_log.append(self._private_location)
        #Update real location:
        Robot.static_arena.moveRobot(self._id,direction)


    #Generates and returns random direction.
    #Before return it check that its a legal move.
    def getRandomDirection(self):
        env = self.getEnv()
        direction = randint(WHITE(), BLACK()) #white,black,gray
        while(env[direction] == False):
            dir = randint(WHITE(), BLACK())
        return direction


    """
    def haveMessage(self, message): #differant versions..
        return message in self.messages

    def addNeighbor(self,neighbor):
        if(self.hasNeighbor()): return
        self.neighbors_list.append(neighbor)

    def hasNeighbor(self, neighbor):
        return neighbor in self.neighbors_list    """


    def toString(self):
        return "id:"+str(self._id)+" , battery status:"+str(self._battery_status)+" , message log:"+str(self._message_log)+" ,neighbors list:"+str(self._neighbors_list)+" ,can move:"+str(self._can_move)


