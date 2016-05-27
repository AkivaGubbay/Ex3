from code.Point import Point
from code.Global_Parameters import *

#TODO:
# add senders to 'sender_history'

#good day!
class Message:
    def __init__(self,Id_Sender,Id_Message,Time,sender_estimated_loc):
        self._id_source = Id_Sender    # Upond creation: source = sender.
        self._id_message = Id_Message  # transmit_Message function (on Simulation) updates that value
        self._sender_history = []  # From here you can also find the latest sender.
        self._sender_estimated_location = sender_estimated_loc

        self._create_time = Time   #so that we dont pass 'MSG_LIFE_TIME'.
        self._version = 0    #so that we dont pass 'MAX_VERSION'.
        self._real_location = Point(0,0)
        self._snn = 0
        self._mat_distance = []
        #Iputing '_mat_distance' distances:

        if(bool(ACTIVE_MATDISTANCE())):
            for i in range(int(float(ARENA_Y()))):
                self._mat_distance.append(int(ARENA_X()) * [INFINITY()])

    @staticmethod
    def equals(self, message):
        if(self._id_message != message._id_message): return 0
        elif (self._version > message._version): return 1
        else: return 2


    def __str__(self):
        return "MSG- id_message:" + str(self._id_message)+", id source:" + str(self._id_source) +" ,Version:" + str(self._version) +" ,Snn:" + str(self._snn)

    def toString(self):
        return "MSG[id_message:" + str(self._id_message)+", id source:" + str(self._id_source) +" ,Version:" + str(self._version) +" ,Snn:" + str(self._snn) +"]"




