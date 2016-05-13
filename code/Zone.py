from code.Global_Parameters import *
from code.Robot import Robot
from random import randint
from code.log import log

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa



#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
#white = 0    gray = 1     black = 2
class Zone:
    def __init__(self, Mylog):
        self.Robot_By_XY = []   #id of robots on matrix
        self.Type_by_XY = []    #Areas in Zone
        self.Mylog = Mylog

        #Building Zone:
        for i in range(AREANA_X()):
            self.Robot_By_XY.append(AREANA_Y()*[-1])
            self.Type_by_XY.append(AREANA_Y() * [0])

        # Mark gray areas
        Gray_area_point = GRAY_AREA()
        for b in range(len(Gray_area_point)):
            Mylog.addLine("create gray area point between: "+str(Gray_area_point[b]))
            for i in range(Gray_area_point[b][0], Gray_area_point[b][2]+1):
                for j in range(Gray_area_point[b][1], Gray_area_point[b][3]+1):
                    self.Type_by_XY[i][j] = 1


        # Mark black areas
        black_area_point = BLACK_AREA()
        for b in range(len(black_area_point)):
            Mylog.addLine("create black area point between: " + str(black_area_point[b]))
            for i in range(black_area_point[b][0], black_area_point[b][2]+1):
                for j in range(black_area_point[b][1], black_area_point[b][3]+1):
                    self.Type_by_XY[i][j] = 2

        self.Robots = []
        for s in range(0, Robots_move()):
            x = randint(1, AREANA_X()-2)
            y = randint(1, AREANA_Y()-2)

            while(self.Robot_By_XY[x][y]!=-1 | self.Type_by_XY[x][y] == 2):
                x = randint(1, AREANA_X() - 2)
                y = randint(1, AREANA_Y() - 2)
                print("swap XY")

            self.Robots.append(Robot(s))
            self.Robot_By_XY[x][y] = self.Robots[s].id
            Mylog.addLine(
                "create new Robot- " + self.Robots[s].toString() + " in [" + str(x) + "," + str(y) + "]")

        for s in range(0, Robots_not_move()):
            x = randint(1, AREANA_X() - 2)
            y = randint(1, AREANA_X() - 2)

            while (self.Robot_By_XY[x][y] == - 1 | self.Type_by_XY[x][y] == 2):
                x = randint(1, AREANA_X() - 2)
                y = randint(1, AREANA_X() - 2)
                print("swap XY")

            self.Robots.append(Robot(s+Robots_move()))
            self.Robots[s + Robots_move()].CanMove = False
            self.Robot_By_XY[x][y] = self.Robots[s+Robots_move()].id
            Mylog.addLine("create new Robot- " + self.Robots[s+Robots_move()].toString()+" in ["+str(x)+","+str(y)+"]")


    def PrintRobot_By_XY(self):
        print("PrintRobot_By_XY:")
        for i in range(0, len(self.Robot_By_XY)):
            for j in range(0, len(self.Robot_By_XY[i])):
                id =self.Robot_By_XY[i][j]
                if(id !=-1):
                    print("["+str(i)+","+str(j)+"]= Robot_"+str(id)+": canMove-"+ str(self.Robots[id].CanMove))



    def PrintType_by_XY(self):
        print("PrintType_by_XY:")
        for i in range(len(self.Type_by_XY)):
            for j in range(len(self.Type_by_XY[i])):
                if(self.Type_by_XY[i][j] !=0):
                    print("["+str(i)+","+str(j)+"]="+str(self.Type_by_XY[i][j]))
