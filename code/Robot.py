from code.Global_Parameters import *

#Will add inheritace for differante types of robots.
class Robot:

    def __init__(self, id):
        self.id = id
        self.battery_status = BATTARY_CAPACITY()
        self.messages = []         #All received messages
        self.isTransmitting = True      #Robot is either transmitting or receiving
        self.neighbors_list = []

