from code.Point import *
from code.Message import *
#from code.Air import *
from code.Global_Parameters import *
from random import randint
#Life is good!
class Robot:
    static_arena = -1
    static_air = -1

    def __init__(self, id):
        self._id = id
        self._can_move = True
        self._battery_status = BATTARY_CAPACITY()
        self._private_location = Point(0,0)
        self._estimated_location = Point(ARENA_X()/2,ARENA_Y()/2)
        self._estimated_location._deviation = ARENA_X()+ARENA_Y()
        self._real_location = Point(0,0) #later put real location.
        self._message_log = []          #All received messages
        self._private_location_log = [Point(0,0)] #Holds all the robots movements as list of points
        self._neighbors_loc = []*(ROBOTS_MOVE()+ROBOTS_NOT_MOVE())      #Can save all his neighbors location
        self._time = -1                 #Robots always knows the time.
        self._currently_sending = NO_MSG()
        self._currently_get_message = NO_MSG()
        self._action_time = INFINITY()    #When to do my next action(next sending).
        self._current_zone = -1

    def doAction(self):
        if self._action_time != INFINITY():
            if self._action_time == self._time:
                self.forwardMessage()
                return
        else: # Robot has no action. He will now get a random one:
            print("Robot " + str(self._id) + ": No Action Taken.")
            x = randint(1, 3)
            if x == 1: #send new Message.
                print("Robot " + str(self._id) + ": sending new Message")
                self.sendNewMessage()
            elif x == 2: #Move randomly.
                direction = self.getRandomDirection()
                self.move(direction)
                print("Robot " + str(self._id) + ": Moving randomly.")
            elif x == 3:  # get message.
                self.getMessage()
                print("Robot " + str(self._id) + ": Receiving Messages.")



    #Robot asks 'Arena' in witch directions can he move.
    def getEnv(self):
        return Robot.static_arena.getEnv(self._id)


    # Robot moves in given 'direction',
    # updates his 'private_location', 'private_location_log',
    # and calls 'Arena' to update 'real location'.
    def move(self,direction):
        x = self._private_location._x
        y = self._private_location._y
        if direction == UP() : y += -1
        elif direction == LEFT() : x += -1
        elif direction == DOWN() : y += 1
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

    #Creats a new message and sends it if possible:
    def sendNewMessage(self):
        #Want to sent my zone:
        self._estimated_location._zone = self._current_zone # send the true color of zone

        # creating new message:
        msg = Message(self._id,self.creatMessageId(),self._time,self._estimated_location)
        self._currently_sending = msg
        self._action_time = self.msgRandomWaitTime()

        # checking with 'Air' that robot can send now:
        if self._time < self._action_time or Robot.static_air.canSend(self) == False:
            # robot must send another time:

            #Case: 'action time' is now but 'Air' wont let robot send:
            if self._time == self._action_time: self._action_time += 1

            return

        else: #Sending now!
            self._message_log.append(msg._id_message)
            Robot.static_air.sendMessage(msg, self)
            self._action_time = INFINITY()
            self._currently_sending = NO_MSG()




    def forwardMessage(self):
        self._currently_sending._sender_history.append(self._id)  # Adds the robots id to message's 'sender_history'.
        was_sent = Robot.static_air.sendMessage(self._currently_sending, self)
        if was_sent == False:
            self._action_time += 1
            print("Robot " + str(self._id) + ": Is Waiting..")
            return
        else:
            print("Robot " + str(self._id) + "sent message  " + str(self._currently_sending._id_message))
            self._action_time = INFINITY()
            self._currently_sending = NO_MSG()
            return



    def getMessage(self):
        msg = Robot.static_air.getMessage(self)
        if(msg == NO_MSG()):
            return
        else:
            if msg._version >= MAX_NUM_OF_VERSIONS(): return
            msg._version+= 1

            #Updating 'neighbors_loc' with info from recieved message:(location of the last message sender)
            point1 = Point(msg._sender_estimated_location._x, msg._sender_estimated_location._y)
            point1._deviation = Point.signalToDistance(msg._snn)
            point1._zone = msg._sender_estimated_location._zone
            self._neighbors_loc[msg._sender_history[len(msg._sender_history)-1]] =point1

            # Updating 'estimated_location' with info from recieved message:
            self._estimated_location._x -=self._private_location._x
            self._estimated_location._y -= self._private_location._y
            new_point = Point(msg._sender_estimated_location._x, msg._sender_estimated_location._y)
            new_point._deviation = Point.signalToDistance(msg._snn)
            self._estimated_location.joint(new_point)
            self._estimated_location._x += self._private_location._x
            self._estimated_location._y += self._private_location._y

            self._currently_get_message = msg
            self._action_time = self.msgRandomWaitTime()
            self._message_log.append(msg._id_message)


    def creatMessageId(self):
        return self._id + len(self._message_log)

    def msgRandomWaitTime(self):
        return self._time + randint(0,MSG_WAIT_TIME())

    def toString(self):
        return "id:"+str(self._id)+" , battery status:"+str(self._battery_status)+" , message log:"+str(self._message_log)+" ,_estimated_location:"+str(self._estimated_location.toString())+" ,can move:"+str(self._can_move)


