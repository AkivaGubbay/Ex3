from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Log import Log

class Air:
    static_mat_zone = -1
    _self = -1
    _messages = []
    def __init__(self):
        _self = self

    @staticmethod
    def sendMessage(message, robot):
        canSend = Air.canSend(robot)
        if(canSend == True):
            message._real_location = robot._real_location
            Point.fillMatDistance(Air.static_mat_zone,message._mat_distance, message._real_location)
            #Air._self.Id_message = Air._self.mone*1000 +robot._id
            #Air._self.mone = Air._self.mone+1
            Air._messages.append(message)

        return canSend

    @staticmethod
    def getMessage(robot):
        sum_range = 0
        flag = False
        nearest_messages = Message(INFINITY(), INFINITY(),INFINITY())
        robot_loc = robot._real_location
        for i in range(0, len(Air._messages)):
            r = Air._messages[i]._mat_distance[robot_loc._x][robot_loc._y]
            if(r <=MIN_MSG_RANGE()):
                Air._messages[i]._snn = (MAX_MSG_RANGE()-r)*(MAX_MSG_RANGE()-r)
                return Air._messages[i] ##################################put distance to msg
            elif(r >=MAX_MSG_RANGE()):
                continue
            else:
                sum_range = sum_range + r
                nearest_mess_loc = nearest_messagesa._real_location
                messa_i = Air._messages[i]._real_location
                if(flag == False):
                    nearest_messagesa = Air._messages[i]
                    flag = True
                elif(Point.distance(Air.static_mat_zone, robot_loc,nearest_mess_loc) > Point.distance(Air.static_mat_zone, robot_loc,messa_i)):
                    nearest_messagesa = Air._messages[i]
        if(sum_range>= MAX_MSG_RANGE()):
            return NO_MSG()
        else:
            nearest_messagesa._snn = (MAX_MSG_RANGE()-r)*(MAX_MSG_RANGE()-r)
            ##################################put distance to msg
            return nearest_messagesa

    @staticmethod
    def canSend(robot):
        sum_range = 0
        robot_loc = Robot(robot)._real_location
        for i in range(0, len(Air._messages)):
            r = Air._messages[i]._mat_distance[robot_loc._x][robot_loc._y]
            if (r < MAX_MSG_RANGE()):
                sum_range = sum_range + r
        if (sum_range < MAX_MSG_RANGE()):
            return True
        else:
            return False