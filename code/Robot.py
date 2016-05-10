# robot_type  -  use inheratence for it
class Robot:

    def __init__(self, id, battery_status,message_history,neighbors_list):
        self.id = id
        self.battery_status = battery_status
        self.message_history = message_history     #All received messages
        self.neighbors_list = neighbors_list


