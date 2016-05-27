#private veriables:
__black_area = []
__gray_area = []


#Reads a given variable from 'Parameters.txt' file:
def getVar(var):
    f = open("Parameters.txt", "r")
    s = f.readline()
    line_var = s.rsplit(" =", 1)[0]
    while(var != line_var.upper() and line_var.lower()):
        s = f.readline()
        line_var = s.rsplit(" =", 1)[0]
    f.close()
    return  s[len(line_var) + 3:-1]



#Reads the black zone from 'Parameters.txt' file:
def getBlackZone():
    global __black_area
    f = open("Parameters.txt", "r")
    s = f.readline()
    line_var = s.rsplit(" =", 1)[0]
    while ("BLACK_AREA" != line_var.upper() and line_var.lower()):
        s = f.readline()
        line_var = s.rsplit(" =", 1)[0]
    s = s[len(line_var) + 3:-1]
    parts = s.split(", ")
    for i in parts:
        point_string = str(i)[1:-1]
        cordi = point_string.split(",")
        x1, y1, x2, y2 = int(cordi[0]), int(cordi[1]), int(cordi[2]), int(cordi[3])
        area = [x1, y1, x2, y2]
        __black_area.append(area)
    f.close()

#Reads gray zone from 'Parameters.txt' file:
def getGrayZone():
    global __gray_area
    f = open("Parameters.txt", "r")
    s = f.readline()
    line_var = s.rsplit(" =", 1)[0]
    while ("GRAY_AREA" != line_var.upper() and line_var.lower()):
        s = f.readline()
        line_var = s.rsplit(" =", 1)[0]
    s = s[len(line_var) + 3:-1]
    parts = s.split(", ")
    for i in parts:
        point_string = str(i)[1:-1]
        cordi = point_string.split(",")
        x1, y1, x2, y2 = int(cordi[0]), int(cordi[1]), int(cordi[2]), int(cordi[3])
        area = [x1, y1, x2, y2]
        __gray_area.append(area)
    f.close()

#Gets all constants from 'Parameters.txt' file:
def readParameters():
    global __battary_capacity, __transmission_range
    global __robots_not_move, __robots_move, __arena_x
    global __arena_y, __log_file_directory
    global __white,__gray,__black
    global __older,__same_age,__younger
    global __up,__left,__down, __right
    global __instant_sending_chance,__max_num_of_versions,__message_life_time, __sending_known_deviation
    global __robot_leanght, __infinity, __min_msg_range, __max_msg_range
    global __no_msg, __msg_life_time, __msg_max_version,__msg_wait_time
    global __battery_about_to_end
    global __Button_number_1, __Button_number_2, __Button_number_3
    global __battery_cost_walk, __battery_cost_send_msg, __battery_cost_get_msg, __battery_charge_light_speed
    global __robot_static_Chance_send_msg, __robot_canmove_Chance_send_msg, __robot_canmove_Chance_get_msg
    global __robot_not_move_color,__robot_move_color
    global __active_matdistance

    # battary_capacity:
    __battary_capacity = int(getVar("BATTARY_CAPACITY"))
    # transmission_range:
    __transmission_range = int(getVar("TRANSMISSION_RANGE"))
    # robots_not_move,robots_move:
    __robots_not_move,__robots_move = int(getVar("ROBOTS_NOT_MOVE")),int(getVar("ROBOTS_MOVE"))
    # arena_x,arena_y:
    __arena_x,__arena_y = int(getVar("ARENA_X")),int(getVar("ARENA_Y"))
    # black_area:
    getBlackZone()
    # gray_area:
    getGrayZone()
    # log_file_directory:
    __log_file_directory = getVar("LOG_FILE_DIRECTORY")
    # white,gray,black:
    __white,__gray,__black = int(getVar("WHITE")),int(getVar("GRAY")),int(getVar("BLACK"))
    # white:
    __older,__same_age,__younger = int(getVar("OLDER")),int(getVar("SAME_AGE")),int(getVar("YOUNGER"))
    # up,left,down,right:
    __up,__left,__down,__right = int(getVar("UP")),int(getVar("LEFT")),int(getVar("DOWN")),int(getVar("RIGHT"))
    # instant_sending_chance:
    __instant_sending_chance = float(getVar("INSTANT_SENDING_CHANCE"))
    # sending_known_deviation:
    __sending_known_deviation = float(getVar("SENDING_KNOWN_DEVIATION"))
    # max_num_of_versions:
    __max_num_of_versions = int(getVar("MAX_NUM_OF_VERSIONS"))
    # message_life_time:
    __message_life_time = int(getVar("MESSAGE_LIFE_TIME"))
    # robot length(for gui):
    __robot_leanght = int(getVar("ROBOT_LEANGHT"))
    # For Distance:
    __infinity = int(getVar("INFINITY"))
    # Accuracy range for ssn of messages:
    __min_msg_range,__max_msg_range = int(getVar("MIN_MSG_RANGE")),int(getVar("MAX_MSG_RANGE"))
    # Msg constants:
    __no_msg, __msg_life_time,__msg_max_version = int(getVar("NO_MSG")),int(getVar("MSG_LIFE_TIME")),int(getVar("MSG_MAX_VERSION"))
    # Range of time a message must wait before being sent:
    __msg_wait_time = int(getVar("MSG_WAIT_TIME"))
    # battery_about_to_end:
    __battery_about_to_end = float(getVar("BATTERY_ABOUT_TO_END"))

    # Several steps by pressing the buttons:
    __Button_number_1 = int(getVar("BUTTON_NUMBER_1"))
    __Button_number_2 = int(getVar("BUTTON_NUMBER_2"))
    __Button_number_3 = int(getVar("BUTTON_NUMBER_3"))

    # The cost of battery operation:
    __battery_cost_walk = float(getVar("BATTARY_COST_WALK"))
    __battery_cost_send_msg = float(getVar("BATTARY_COST_SEND_MSG"))
    __battery_cost_get_msg = float(getVar("BATTARY_COST_GET_MSG"))
    __battery_charge_light_speed = float(getVar("BATTARY_CHARGE_LITHT_SPEED"))

    __robot_static_Chance_send_msg = float(getVar("ROBOT_STATIC_CHANCE_SEND_MSG"))
    __robot_canmove_Chance_send_msg = float(getVar("ROBOT_CANMOVE_CHANCE_SEND_MSG"))
    __robot_canmove_Chance_get_msg = float(getVar("ROBOT_CANMOVE_CHANCE_GET_MSG"))

    __robot_not_move_color = int(getVar("ROBOTS_NOT_MOVE_COLOR"))
    __robot_move_color = int(getVar("ROBOTS_MOVE_COLOR"))

    __active_matdistance = int(getVar("ACTIVE_MATDISTANCE"))

#Project Constants:
def BATTARY_CAPACITY():
    return __battary_capacity

def TRANSMISSION_RANGE():
    return __transmission_range

def ROBOTS_NOT_MOVE():
    return __robots_not_move

def ROBOTS_MOVE():
    return __robots_move

def ARENA_X():
    return __arena_x

def ARENA_Y():
    return __arena_y

def BLACK_AREA():
    return __black_area;

def GRAY_AREA():
   return __gray_area

def LOG_FILE_DIRECTORY():
    return __log_file_directory

def WHITE():
   return __white

def GRAY():
   return __gray

def BLACK():
   return __black

def OLDER():
   return __older

def SAME_AGE():
   return __same_age

def YOUNGER():
   return __younger

def UP():
    return __up

def LEFT():
    return __left

def DOWN():
    return __down

def RIGHT():
    return __right

def INSTANT_SENDING_CHANCE():
   return __instant_sending_chance

def SENDING_KNOWN_DEVIATION():
   return __sending_known_deviation

def MAX_NUM_OF_VERSIONS():
   return __max_num_of_versions

def MESSAGE_LIFE_TIME():
   return __message_life_time

def ROBOT_LEANGHT():
    return __robot_leanght

def INFINITY():
    return __infinity
def MIN_MSG_RANGE():
    return __min_msg_range

def MAX_MSG_RANGE():
    return __max_msg_range

def NO_MSG():
    return __no_msg

def MSG_LIFE_TIME():
    return __msg_life_time

def MSG_MAX_VERSION():
    return __msg_max_version

def MSG_WAIT_TIME():       # Range of time a new message must waut before being sent:
    return __msg_wait_time

def BATTERY_ABOUT_TO_END():
    return __battery_about_to_end

def BUTTON_NUMBER_1():
    return __Button_number_1

def BUTTON_NUMBER_2():
    return __Button_number_2

def BUTTON_NUMBER_3():
    return __Button_number_3

def BATTARY_COST_WALK():
    return __battery_cost_walk

def BATTARY_COST_SEND_MSG():
    return __battery_cost_send_msg

def BATTARY_COST_GET_MSG():
    return __battery_cost_get_msg

def BATTARY_CHARGE_LITHT_SPEED():
    return __battery_charge_light_speed

def ROBOT_STATIC_CHANCE_SEND_MSG():
    return __robot_static_Chance_send_msg

def ROBOT_CANMOVE_CHANCE_SEND_MSG():
    return __robot_canmove_Chance_send_msg

def ROBOT_CANMOVE_CHANCE_GET_MSG():
    return __robot_canmove_Chance_get_msg

def ROBOTS_NOT_MOVE_COLOR():
    return __robot_not_move_color

def ROBOTS_MOVE_COLOR():
    return __robot_move_color

def ACTIVE_MATDISTANCE():
    return __active_matdistance


