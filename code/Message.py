from code.Point import Point
from code.Global_Parameters import *

#TODO:
# add senders to 'sender_history'

class Message:
    def __init__(self,Id_Sender,Id_Message,Time):
        self._id_source = Id_Sender    # Upond creation: source = sender.
        self._id_message = Id_Message  # transmit_Message function (on Simulation) updates that value
        self_sender_history = [Id_Sender]  # From here you can also find the latest sender.
        self._create_time = Time   #so that we dont pass 'MSG_LIFE_TIME'.
        self._version = 0    #so that we dont pass 'MAX_VERSION'.
        self._real_location = Point(0,0)
        self._snn = -1
        self._mat_distance = []
        #Iputing '_mat_distance' distances:
        for i in range(int(float(ARENA_Y()))):
            self._mat_distance.append(int(ARENA_X()) * [INFINITY()])


    def __str__(self):
        return ",id_message:" + str(self._id_message)+"id source:" + str(self._id_source) +",Version:" + str(self._version)+ ",Life:"+str(self._lif)




