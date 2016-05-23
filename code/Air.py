from code.Global_Parameters import *
from code.Robot import Robot
from code.Arena import Arena
from code.Message import Message
from code.Point import Point
from code.Log import Log

class Air:
    static_mat_zone = -1
    _self = -1
    def __init__(self):
        self._messages = []
        self.mone = 0
        _self = self

    def sendMessage(self, _mat_zone, message, robot):
        message._real_location = robot._real_location
        Point.fillMatDistance(_mat_zone,message._mat_distance, message._real_location)
        self.Id_message = self.mone*1000 +robot._id
        self.mone = self.mone+1

    def getMessage(robot):
        for i in range(0, len(Air._self._messages)):
            if(Air._self._messages[i]._mat_distance[robot._real_location._x][robot._real_location._y] <=50):
                return Air._self._messages[i]


    """ # Enter a new Message to X variable "Messages"
   def transmit_Message(self, MyMessage):
       NewMessage = Message(MyMessage.Id_Sender, MyMessage.Message)
       NewMessage.Id_message = len(self._messages)
       self._messages.append(NewMessage)
       return NewMessage

   # Reenter a Message to X variable "Messages"
   def transmit_Message_again(self, MyMessage):
       NewMessage = self.transmit_Message(MyMessage)

       NewMessage.Version = MyMessage.Version+1
       return NewMessage

   # Do self.Messages[i].Life--
   # deletes the message when Life==0 equal to zero
   def Deleting_old_messages(self):
       MySize = len(self._messages)
       i=0
       mone=0
       while(i<MySize):
           self._messages[i].Life = self._messages[i].Life - 1
           if (self._messages[i].Life == 0):
               self._messages.remove(self._messages[i])
               MySize = MySize - 1
               mone=mone+1
           else:
               i = i + 1

       Log.addLine("\"Deleting_old_messages\" function Delete "+str(mone)+" Posts")

   def toString_Messages(self):
       MyStr="toString_Messages [size="+str(len(self._messages))+"]:"
       for i in range(len(self._messages)):
           MyStr+="\n"+self._messages[i].toString()
       return MyStr"""