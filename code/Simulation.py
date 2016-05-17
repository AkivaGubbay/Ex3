from code.Global_Parameters import *
from code.Robot import Robot
from code.Zone import Zone
from code.Message import Message

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Simulation:
    def __init__(self, Mylog):
        Mylog.addLine("create Simulation")
        self.Messages = []
        self.Robots = []
        self.Mylog = Mylog

        # Creates a new robot 'that can move' to variable "Robots"
        for s in range(0, int(ROBOTS_MOVE())):
            self.Robots.append(Robot(s))
            Mylog.addLine("create new Robot- " + self.Robots[s].toString())

        # Creates a new robot 'that can't move' to variable "Robots"
        for s in range(int(ROBOTS_MOVE()), int(ROBOTS_MOVE())+int(ROBOTS_NOT_MOVE())):
            self.Robots.append(Robot(s))
            self.Robots[s].CanMove = False
            Mylog.addLine("create new Robot- " + self.Robots[s].toString())

        # Creates Zone:
        self.Zone = Zone(Mylog, self.Robots)

        """ <<<   Here should be the "MAIN FOR" Of the project   >>> """

    # Enter a new Message to X variable "Messages"
    def transmit_Message(self, MyMessage):
        NewMessage = Message(MyMessage.Id_Sender, MyMessage.Message)
        NewMessage.Id_message = len(self.Messages)

        self.Messages.append(NewMessage)
        return NewMessage

    # Reenter a Message to X variable "Messages"
    def transmit_Message_again(self, MyMessage):
        NewMessage = self.transmit_Message(MyMessage)

        NewMessage.Version = MyMessage.Version+1
        return NewMessage

    # Do self.Messages[i].Life--
    # deletes the message when Life==0 equal to zero
    def Deleting_old_messages(self):
        MySize = len(self.Messages)
        i=0
        mone=0
        while(i<MySize):
            self.Messages[i].Life = self.Messages[i].Life - 1
            if (self.Messages[i].Life == 0):
                self.Messages.remove(self.Messages[i])
                MySize = MySize - 1
                mone=mone+1
            else:
                i = i + 1

        self.Mylog.addLine("\"Deleting_old_messages\" function Delete "+str(mone)+" Posts")

    def toString_Messages(self):
        MyStr="toString_Messages [size="+str(len(self.Messages))+"]:"
        for i in range(len(self.Messages)):
            MyStr+="\n"+self.Messages[i].toString()
        return MyStr


    def gui(self):
        X = []
        for i in range(int(ARENA_X())):
            line = int(ARENA_Y())*[0]
            for j in range(int(ARENA_Y())):
                if(self.Zone.Robot_By_XY[i][j]!=-1):
                    line[j] = -1000
                elif (self.Zone.Type_by_XY[i][j] == 2):
                    line[j] = 1000
                elif (self.Zone.Type_by_XY[i][j] == 1):
                    line[j] = 500
                elif (self.Zone.Type_by_XY[i][j] == 0):
                    line[j] = 0
                    """if (i > 0 & i<ARENA_Y()-1 & j> 0 & j<ARENA_Y()-1):
                        if((self.Zone.Robot_By_XY[i][j-1]!=-1)|(self.Zone.Robot_By_XY[i][j+1]!=-1)|(self.Zone.Robot_By_XY[i-1][j]!=-1)|(self.Zone.Robot_By_XY[i+1][j]!=-1)):
                            line[j] = -1000
                        elif ((self.Zone.Robot_By_XY[i-1][j - 1] != -1) | (self.Zone.Robot_By_XY[i+1][j + 1] != -1) | (
                            self.Zone.Robot_By_XY[i - 1][j+1] != -1) | (self.Zone.Robot_By_XY[i + 1][j-1] != -1)):
                            line[j] = -1000"""

            X.append(line)
        fig, ax = plt.subplots()
        ax.imshow(X, cmap='RdGy', interpolation='nearest')
        plt.show()
