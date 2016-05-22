from code.Global_Parameters import *
from code.Robot import Robot
from random import randint
from code.Log import Log
from code.Message import Message

class Air:
    def __init__(self):
        self._messages = []

    def getMessage(self, message):
        #fewferw
        x=444

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