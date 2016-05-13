from code.Global_Parameters import *
from code.Robot import Robot
from code.Zone import Zone


class Simulation:
    def __init__(self, Mylog):
        Mylog.addLine("create Simulation")

        self.Robots = []
        for s in range(0, Robots_move()):
            self.Robots.append(Robot(s))
            Mylog.addLine("create new Robot- " + self.Robots[s].toString())

        for s in range(Robots_move(), Robots_move()+Robots_not_move()):
            self.Robots.append(Robot(s))
            self.Robots[s].CanMove = False
            Mylog.addLine("create new Robot- " + self.Robots[s].toString())

        self.Zone = Zone(Mylog, self.Robots)
