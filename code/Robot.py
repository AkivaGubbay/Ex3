from code.Point import *
from code.Global_Parameters import *

class Robot:

    def __init__(self, id):
        self._id = id
        self._can_move = True
        self._battery_status = BATTARY_CAPACITY()
        self._private_location = Point(0,0)
        self._real_location = Point(0,0)
        self._message_log = []          #All received messages
        self._private_location_log = [] #Holds all the robots movements as list of points
        self._neighbors_color = []      #Can save all his neighbors colors
        self._neighbors_list = []
        self._out_book = []             #Messages waiting to be sent.
        self._time = -1                 #Robots always knows the time.
        self._currently_sending = -1
        self._currently_get_message = -1
        self._current_zone = -1
        self._distance_from = []#I want to fill the whole list with -1 but i dont knot how many neighbors..

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


