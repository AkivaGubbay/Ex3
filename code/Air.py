from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Log import Log
import math

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
            if (bool(ACTIVE_MATDISTANCE())):
                Point.fillMatDistance(Air.static_mat_zone,message._mat_distance, message._real_location)

            #Air._self.Id_message = Air._self.mone*1000 +robot._id
            #Air._self.mone = Air._self.mone+1
            Air._messages.append(message)

        return canSend

    @staticmethod
    def getMessage(robot):
        sum_range = 0
        flag = False
        if(len(Air._messages) ==0 ): return NO_MSG()
        nearest_messagesa = Air._messages[0]
        robot_loc = robot._real_location
        r=0
        for i in range(0, len(Air._messages)):
            r =0
            if (bool(ACTIVE_MATDISTANCE())):
                r = Air._messages[i]._mat_distance[robot_loc._x][robot_loc._y]
            else:
                r = Point.airDistancePoints(robot_loc, Air._messages[i]._real_location)
            if(r == INFINITY() or r<=0): continue
            if(r <=MIN_MSG_RANGE()):
                Air._messages[i]._snn = (MAX_MSG_RANGE()-r)*(MAX_MSG_RANGE()-r)
                return Air._messages[i] ##################################put distance to msg
            elif(r >=MAX_MSG_RANGE()):
                continue
            else:
                if(Air._messages[i]._sender_estimated_location._deviation<100):
                    Air._messages[i]._snn = (MAX_MSG_RANGE() - r) * (MAX_MSG_RANGE() - r)
                    return Air._messages[i]  ##################################put distance to msg

                sum_range = sum_range + r
                nearest_mess_loc = nearest_messagesa._real_location
                messa_i = Air._messages[i]._real_location
                if(flag == False):
                    flag = True
                    nearest_messagesa = Air._messages[i]
                    nearest_messagesa._snn = (MAX_MSG_RANGE() - r) * (MAX_MSG_RANGE() - r)
                    return nearest_messagesa
                elif(Point.distance(Air.static_mat_zone, robot_loc,nearest_mess_loc) > Point.distance(Air.static_mat_zone, robot_loc,messa_i)):
                    nearest_messagesa = Air._messages[i]
                    nearest_messagesa._snn = (MAX_MSG_RANGE() - r) * (MAX_MSG_RANGE() - r)
        if(flag): return NO_MSG()
        if(sum_range==0): return NO_MSG()
        if(r==0 or sum_range>= MAX_MSG_RANGE()):
            return NO_MSG()
        else:
            nearest_messagesa._snn = nearest_messagesa._snn - sum_range
            #print("\n%%%\nnearest_messagesa._snn:: " + str(nearest_messagesa._snn))
            #print("sum_range:: " + str(sum_range))
            #print("_snn:: " + str(nearest_messagesa._snn))
            ##################################put distance to msg
            return nearest_messagesa

    @staticmethod
    def canSend(robot):
        sum_range = 0
        robot_loc = Robot(robot)._real_location
        for i in range(0, len(Air._messages)):
            r = 0
            if (bool(ACTIVE_MATDISTANCE())):
                r = Air._messages[i]._mat_distance[robot_loc._x][robot_loc._y]
            else:
                r = Point.airDistancePoints(robot_loc, Air._messages[i]._real_location)

            if (r < MAX_MSG_RANGE()):
                sum_range = sum_range + r
        if (sum_range < math.sqrt(MAX_MSG_RANGE())):
            return True
        else:
            return False