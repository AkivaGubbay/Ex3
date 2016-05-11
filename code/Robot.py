from code.Global_Parameters import *

#TODO:
#Add inheritace for differante types of robots.
#Add Field so that robot knows what area he is in(white,black,gray).
class Robot:

    def __init__(self, id):
        self.id = id
        self.battery_status = BATTARY_CAPACITY()
        self.messages = []         #All received messages
        self.isTransmitting = True      #Robot is either transmitting or receiving
        self.neighbors_list = []

    def haveMessage(self, message):
        for i in self.messages:
            if(message is self.messages[i]):   #'is' compares id's of strings
                return True
        return False

    def addNeighbor(self,neighbor):
        if(neighbor in self.neighbors_list): return
        self.neighbors_list.append(neighbor)