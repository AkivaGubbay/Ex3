from code.Global_Parameters import *

# TO-DO:
#Add Field so that robot knows what area he is in(white,black,gray).
class Robot:

    def __init__(self, id):
        self.id = id
        self.battery_status = BATTARY_CAPACITY()
        self.messages = []           #All received messages
        self.isTransmitting = True      #Robot is either transmitting or receiving
        self.neighbors_list = []
        self.CanMove = True

    def haveMessage(self, message): #differant versions..
        return message in self.messages

    def addNeighbor(self,neighbor):
        if(self.hasNeighbor()): return
        self.neighbors_list.append(neighbor)

    def hasNeighbor(self, neighbor):
        return neighbor in self.neighbors_list

    def toString(self):
        return "ID:"+str(self.id)+" ,battery_status:"+str(self.battery_status)+" ,messages:"+str(self.messages)+" ,isTransmitting:"+str(self.isTransmitting)+" ,neighbors_list:"+str(self.neighbors_list)+" ,CanMove:"+str(self.CanMove)