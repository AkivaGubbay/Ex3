from code.Point import *
from code.Message import *
#from code.Air import *
from code.Global_Parameters import *
from code.Log import Log
from code.Message import Message
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
        self._neighbors_loc = [INFINITY()]*(ROBOTS_MOVE()+ROBOTS_NOT_MOVE())      #Can save all his neighbors location
        self._time = -1                 #Robots always knows the time.
        self._currently_sending = NO_MSG()
        self._currently_get_message = NO_MSG()
        self._action_time = INFINITY()    #When to do my next action(next sending).
        self._current_zone = -1

    def doAction(self):
        # charge battery:
        if(self._current_zone == WHITE()):
            self._battery_status +=BATTARY_CHARGE_LITHT_SPEED()
            if(self._battery_status >BATTARY_CAPACITY()): self._battery_status = BATTARY_CAPACITY()

        if self._action_time != INFINITY():
            if self._action_time == self._time:
                self.forwardMessage()
            return

        if(self._can_move == False): # for static robot:
            self._battery_status = BATTARY_CAPACITY()
            x = randint(0, 10)

            if(x < ROBOT_STATIC_CHANCE_SEND_MSG()*10): # send new Message.
                self.sendNewMessage()
            else: # get message.
                self.getMessage()
            return


        if(BATTERY_ABOUT_TO_END()*BATTARY_CAPACITY() > self._battery_status): #The battery is about to run out

            if (self._current_zone == WHITE()):
                Log.addLine("Robot " + str(self._id) + " The battery is about to run out (" + str(self._battery_status) + ") ---> The robot should rest")
                return
            Env = self.getEnv()
            for i in range(0,len(self._private_location_log)):
                i1 = len(self._private_location_log) - i-1
                if(self._private_location_log[i1]._zone == WHITE()):
                    direction = self._private_location.which_direction(self._private_location_log[i1])
                    if(direction == INFINITY()): continue
                    if(direction !=INFINITY() and self.try_move_to_constant_direction(direction)== True):
                        Log.addLine("Robot " + str(self._id) + " The battery is about to run out ---> The robot go to light on " + str(direction) + "direction - The robot knows the point")
                        return

            if(self._estimated_location._deviation<BATTARY_CAPACITY()):
                for i in range(0,len(self._neighbors_loc)):
                    if(self._neighbors_loc[i] == INFINITY()): continue
                    if(self._neighbors_loc[i]._deviation >BATTARY_CAPACITY()): continue # Only if the robot can go there
                    if(Point.airDistancePoints(self._estimated_location, self._neighbors_loc[i])>BATTARY_CAPACITY()): continue # Only if the robot can go there
                    if(self._neighbors_loc[i]._zone == WHITE()):
                        direction = self._estimated_location.which_direction(self._neighbors_loc[i])
                        if (direction == INFINITY()): continue
                        if(direction !=INFINITY() and self.try_move_to_constant_direction(direction)== True):
                            Log.addLine("Robot " + str(self._id) + " The battery is about to run out ---> the robot goes towards the robot_" + i + " (to the " + str(direction) + ") is there light!")
                            return


            x = randint(1, int(BATTERY_ABOUT_TO_END() *10))
            if(x!=1):
                Log.addLine("Robot " + str(self._id) + " The battery is about to run out (" + str(self._battery_status) + ") ---> The robot rest")
            else:
                Log.addLine("Robot " + str(self._id) + " The battery is about to run out (" + str(self._battery_status) + ") ---> The robot has decided to continue as usual")

        # Robot has no action. He will now get a random:
        x = randint(1, 3) ############################################ <<<<<------------------------
        if x == 1 and self._battery_status > BATTARY_COST_SEND_MSG():  # send new Message.
            self.sendNewMessage()
            return
        elif x == 2 and self._battery_status > BATTARY_COST_WALK():  # Move randomly.
            direction = self.getRandomDirection()
            self.move(direction)
            #Log.addLine("Robot " + str(self._id) + ": Moving randomly.")
            return
        elif x == 3 and self._battery_status > BATTARY_COST_GET_MSG():  # get message.
            self.getMessage()
            return



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
        else: return #BATTARY_COST_WALK
        self._battery_status -= BATTARY_COST_GET_MSG()
        #Update _private_location:d
        self._private_location = Point(x,y)
        #Add to robots new _private_location to log:
        self._private_location_log.append(self._private_location)
        #Update real location:
        Robot.static_arena.moveRobot(self._id,direction)


    def try_move_to_constant_direction(self,direction):
        x = self._private_location._x
        y = self._private_location._y
        possible_direction = self.getEnv()

        if (possible_direction[direction] == True):
            if direction == UP() : y += -1
            elif direction == LEFT() : x += -1
            elif direction == DOWN() : y += 1
            elif direction == RIGHT() : x += 1
            # Update real location:
            Robot.static_arena.moveRobot(self._id, direction)
        elif (possible_direction[(direction+1)%4] == True):
            if (direction+1)%4 == UP() : y += -1
            elif (direction+1)%4 == LEFT() : x += -1
            elif (direction+1)%4 == DOWN() : y += 1
            elif (direction+1)%4 == RIGHT() : x += 1
            # Update real location:
            Robot.static_arena.moveRobot(self._id, (direction+1)%4)
        elif (possible_direction[(direction-1)%4] == True):
            if (direction-1)%4 == UP() : y += -1
            elif (direction-1)%4 == LEFT() : x += -1
            elif (direction-1)%4 == DOWN() : y += 1
            elif (direction-1)%4 == RIGHT() : x += 1
            # Update real location:
            Robot.static_arena.moveRobot(self._id, (direction-1)%4)
        else: return False
        self._battery_status -= BATTARY_COST_GET_MSG()
        #Update _private_location:d
        self._private_location = Point(x,y)
        #Add to robots new _private_location to log:
        self._private_location_log.append(self._private_location)
        return True


    #Generates and returns random direction.
    #Before return it check that its a legal move.
    def getRandomDirection(self):
        env = self.getEnv()
        direction = randint(WHITE(), BLACK()) #white,black,gray
        count = 0 #Case: Robot cant move in any direction.
        while(env[direction] == False and count < 5):
            direction = randint(WHITE(), BLACK())
            count+= 1
        if count == 11:
            Log.addLine("robot "+str(self._id)+" Cant move in any direction. (surrounded by other robots)")
        else: return direction

    #Creats a new message and sends it if possible:
    def sendNewMessage(self):
        #Want to set my zone:
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
            Log.addLine("Robot " + str(self._id) + " sent a new message: " + str(self._currently_sending.toString()))
            print("Robot " + str(self._id) + " sent a new message: " + str(self._currently_sending.toString()))

            self._battery_status -= BATTARY_COST_SEND_MSG()
            self._message_log.append(msg._id_message)
            Robot.static_air.sendMessage(msg, self)
            self._action_time = INFINITY()
            self._currently_sending = NO_MSG()

    def forwardMessage(self):
        if(self._currently_sending == NO_MSG()): # hould not happen .. Debugger
            self._action_time = INFINITY()
            return

        self._currently_sending._sender_history.append(self._id)  # Adds the robots id to message's 'sender_history'.
        was_sent = Robot.static_air.sendMessage(self._currently_sending, self)

        if was_sent == False:
            self._action_time += 1
            Log.addLine("Robot " + str(self._id) + ": Is Waiting to forward Message")
            return
        else:
            self._battery_status -= BATTARY_COST_SEND_MSG()
            Log.addLine("Robot " + str(self._id) + " sent message  " + str(self._currently_sending.toString()))
            print("Robot " + str(self._id) + " sent message  " + str(self._currently_sending.toString()))
            self._action_time = INFINITY()
            self._currently_sending = NO_MSG()
            return

    def getMessage(self):
        msg = Robot.static_air.getMessage(self)
        self._battery_status -= BATTARY_COST_GET_MSG()
        if(msg == NO_MSG()):
            Log.addLine("Robot " + str(self._id) + ": Receiving Messages.  --->  Not received!")
            return
        else:
            if msg._version >= MAX_NUM_OF_VERSIONS(): return
            msg._version+= 1
            Log.addLine("Robot " + str(self._id) + ": Receiving Messages.  --->  Received a new message! " + msg.toString())
            print("Robot " + str(self._id) + ": Receiving Messages.  --->  Received a new message! " + msg.toString())

            #Updating 'neighbors_loc' with info from recieved message:(location of the last message sender)
            point1 = Point(msg._sender_estimated_location._x, msg._sender_estimated_location._y)
            point1._deviation = Point.signalToDistance(msg._snn)
            point1._zone = msg._sender_estimated_location._zone
            if(len(msg._sender_history)>0): self._neighbors_loc[msg._sender_history[len(msg._sender_history)-1]] =point1
            else: self._neighbors_loc[msg._id_source] = point1

            # Updating 'estimated_location' with info from recieved message:
            #toLog = "Robot " + str(self._id) +": Estimated_location before the message - "+ self._estimated_location.toString()
            #Log.addLine(toLog)

            self._estimated_location._x -=self._private_location._x
            self._estimated_location._y -= self._private_location._y
            new_point = Point(msg._sender_estimated_location._x, msg._sender_estimated_location._y)
            new_point._deviation = Point.signalToDistance(msg._snn)
            self._estimated_location.joint(new_point)
            self._estimated_location._x += self._private_location._x
            self._estimated_location._y += self._private_location._y
            #toLog = "Robot " + str(self._id) +": Estimated_location after the message - "+ self._estimated_location.toString()
            #Log.addLine(toLog)

            self._currently_get_message = msg
            self._action_time = self.msgRandomWaitTime()
            self._message_log.append(msg._id_message)

    def creatMessageId(self):
        return self._id + 1000*(len(self._message_log)+1)

    def msgRandomWaitTime(self):
        return self._time + randint(0,MSG_WAIT_TIME())

    def toString(self):
        return "ROBOT[id:"+str(self._id)+" , battery_status:"+str(self._battery_status)+" ,message_log:"+str(self._message_log)+" ,estimated_location:"+str(self._estimated_location.toString())+" ,can_move:"+str(self._can_move) +"]"


