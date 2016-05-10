from code.Point import Point

class Robot:

    def __init__(self, id, battery_status,message_history,neighbors_list):
        self.id = id
        self.battery_status = battery_status
        self.message_history = message_history     #All received messages
        self.neighbors_list = neighbors_list


p = Point(4,3)
print(p.toString())
