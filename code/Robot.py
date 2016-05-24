from code.Point import *
from code.Message import *
#from code.Air import *
from code.Global_Parameters import *
from random import randint
#chnage is good.
class Robot:
    static_arena = -1
    static_air = -1

    def __init__(self, id):
        self._id = id
        self._can_move = True
        self._battery_status = BATTARY_CAPACITY()
        self._private_location = Point(0,0)
        self._real_location = Point(0,0) #later put real location.
        self._message_log = []          #All received messages
        self._private_location_log = [Point(0,0)] #Holds all the robots movements as list of points
        self._neighbors_color = []      #Can save all his neighbors colors
        self._neighbors_list = []
        self._time = -1                 #Robots always knows the time.
        self._currently_sending = NO_MSG()
        self._currently_get_message = NO_MSG()
        self._action_time = INFINITY()    #When to do my next action(next sending).
        self._current_zone = -1
        self._distance_from = [-1]*(ROBOTS_MOVE()+ROBOTS_NOT_MOVE())#I want to fill the whole list with -1 but i dont knot how many neighbors..

    def doAction(self):
        if self._action_time != INFINITY():
            if self._action_time == self._time:
                val = Robot.static_air.sendMessage(self._currently_sending,self)
                if val == False:
                    self._action_time+= 1
                    print("Robot " + str(self._id) + ": Is Waiting..")
                    return
                else:
                    print("Robot " + str(self._id) + "sent message  " + self._currently_sending._id_message)
                    self._action_time = INFINITY()
                    self._currently_sending = NO_MSG()
                    return
        print("Robot " + str(self._id) + ": No Action Taken.")
        x = randint(1, 3)
        if x == 1: #send new Message.
            print("Robot " + str(self._id) + ": sending new Message")
            self.sendNewMessage()
        if x == 2: #Move randomly.
            direction = self.getRandomDirection()
            self.move(direction)
            print("Robot " + str(self._id) + ": Moving randomly.")
        #if x == 3:  # Move randomly.



    #Robot asks 'Arena' in witch directions can he move.
    def getEnv(self):
        return Robot.static_arena.getEnv(self._id)


    # Robot moves in given 'direction',
    # updates his 'private_location', 'private_location_log',
    # and calls 'Arena' to update 'real location'.
    def move(self,direction):
        x = self._private_location._x
        y = self._private_location._y
        if direction == UP() : y += 1
        elif direction == LEFT() : x += -1
        elif direction == DOWN() : y += -1
        elif direction == RIGHT() : x += 1
        #Update _private_location:d
        self._private_location = Point(x,y)
        #Add to robots new _private_location to log:
        self._private_location_log.append(self._private_location)
        #Update real location:
        Robot.static_arena.moveRobot(self._id,direction)


    #Generates and returns random direction.
    #Before return it check that its a legal move.
    def getRandomDirection(self):
        env = self.getEnv()
        direction = randint(WHITE(), BLACK()) #white,black,gray
        count = 0 #Case: Robot cant move in any direction.
        while(env[direction] == False or count == 11):
            dir = randint(WHITE(), BLACK())
            count+= 1
        if count == 11:
            print("Cant move in any direction..")
        else: return direction


    def sendNewMessage(self):
        msg = Message(self._id,self.creatMessageId(),self._time)
        self._currently_sending = msg
        if self._action_time != INFINITY():
            self._action_time = self.newMsgRandomWaitTime()
        if self._time < self._action_time or Robot.static_air.canSend(self) == False : return
        self._action_time = INFINITY()
        self._message_log.append(msg._id_message)
        Robot.static_air.sendMessage(msg, self)


    def creatMessageId(self):
        return self._id + len(self._message_log)

    def newMsgRandomWaitTime(self):
        return self._time + randint(0,NEW_MSG_WAIT_TIME())

    def toString(self):
        return "id:"+str(self._id)+" , battery status:"+str(self._battery_status)+" , message log:"+str(self._message_log)+" ,neighbors list:"+str(self._neighbors_list)+" ,can move:"+str(self._can_move)


