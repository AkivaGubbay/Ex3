from code.Point import Point
from code.Global_Parameters import *

class Message:
    def __init__(self,Id_Sender,Message):
        self.Id_Sender = Id_Sender
        self.Id_message = -1  # transmit_Message function (on Simulation) updates that value
        self.Version = 0
        self.Message = Message
        self._real_location = Point(0,0)
        self._mat_distance = []
        for i in range(int(float(ARENA_X()))):
            self._mat_distance.append(int(ARENA_Y()) * [INFINITY()])

    def toString(self):
        return "Id_Sender:" + str(self.Id_Sender) +",Id_message:" + str(self.Id_message)+",Version:" + str(self.Version)+",Message:" + str(self.Message)+ ",Life:"+str(self.Life)


