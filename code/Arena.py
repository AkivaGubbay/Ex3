from code.Global_Parameters import *
from code.Robot import Robot
from random import randint
from code.Log import Log


class Arena:
    def __init__(self, Robots):
        self._mat_robot_id = []
        self._mat_zone = [] #by color (white = 0    gray = 1     black = 2)
        print(ARENA_X())

        for i in range(int(float(ARENA_X()))):
            self._mat_robot_id.append(int(ARENA_Y())*[-1])
            self._mat_zone.append(int(ARENA_Y())*[WHITE()])

        # Mark gray areas:
        Gray_area_point = GRAY_AREA()
        for b in range(len(Gray_area_point)):
            Log.addLine("create gray area point between: "+str(Gray_area_point[b]))
            for i in range(Gray_area_point[b][0], Gray_area_point[b][2]+1):
                for j in range(Gray_area_point[b][1], Gray_area_point[b][3]+1):
                    self._mat_zone[i][j] = GRAY()


        # Mark black areas:
        black_area_point = BLACK_AREA()
        for b in range(len(black_area_point)):
            Log.addLine("create black area point between: " + str(black_area_point[b]))
            for i in range(black_area_point[b][0], black_area_point[b][2]+1):
                for j in range(black_area_point[b][1], black_area_point[b][3]+1):
                    self._mat_zone[i][j] = BLACK()

        #put the robots on Arena:
        for s in range(0, len(Robots)):
            x = randint(1, int(ARENA_X()) - 2)
            y = randint(1, int(ARENA_Y()) - 2)
            bool1 = self._mat_robot_id[x][y]!=-1
            bool2 = self._mat_zone[x][y] == BLACK()
            bool3 = Robots[s].CanMove == False
            bool4 = self._mat_zone[x][y] != WHITE()
            while((bool1 |bool2 ) | (bool3 & bool4)):
                x = randint(1, ARENA_X() - 2)
                y = randint(1, ARENA_Y() - 2)
                print("swap XY")
                bool1 = self._mat_robot_id[x][y] != -1
                bool2 = self._mat_zone[x][y] == BLACK()
                bool3 = Robots[s].CanMove == False
                bool4 = self._mat_zone[x][y] != WHITE()

            Robots.append(Robot(s))
            self._mat_robot_id[x][y] = Robots[s].id
            Log.addLine("put Robot_" + str(Robots[s].id) + " in [" + str(x) + "," + str(y) + "]")



    def Print_mat_robot_id(self):
        print("Print_mat_robot_id:")
        for i in range(0, len(self._mat_robot_id)):
            for j in range(0, len(self._mat_robot_id[i])):
                id =self._mat_robot_id[i][j]
                if(id !=-1):
                    print("["+str(i)+","+str(j)+"]= Robot_"+str(id)+": canMove-"+ str(self.Robots[id].CanMove))

    def PrintType_by_XY(self):
        print("PrintType_by_XY:")
        for i in range(len(self._mat_zone)):
            for j in range(len(self._mat_zone[i])):
                if(self._mat_zone[i][j] !=0):
                    print("["+str(i)+","+str(j)+"]="+str(self._mat_zone[i][j]))
