
#private veriables:
__black_area = []
__gray_area = []


#Reads a given variable from 'Parameters.txt' file:
def getVar(var):
    f = open("Parameters.txt", "r")
    s = f.readline()
    line_var = s.rsplit(" =", 1)[0]
    while(var != line_var):
        s = f.readline()
        line_var = s.rsplit(" =", 1)[0]
    return  s[len(line_var) + 3:-1]

    f.close()

#Reads the black zone from 'Parameters.txt' file:
def getBlackZone():
    global __black_area
    f = open("Parameters.txt", "r")
    s = f.readline()
    line_var = s.rsplit(" =", 1)[0]
    while ("BLACK_AREA" != line_var):
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
    while ("GRAY_AREA" != line_var):
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
    global __current,__up,__left,__down, __right
    global __instant_sending_chance,__max_num_of_versions,__message_life_time

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
    # current,up,left,down,right:
    __current,__up,__left,__down,__right = int(getVar("CURRENT")),int(getVar("UP")),int(getVar("LEFT")),int(getVar("DOWN")),int(getVar("RIGHT"))
    # instant_sending_chance:
    __instant_sending_chance = float(getVar("INSTANT_SENDING_CHANCE"))
    # max_num_of_versions:
    __max_num_of_versions = int(getVar("MAX_NUM_OF_VERSIONS"))
    # message_life_time:
    __message_life_time = int(getVar("MESSAGE_LIFE_TIME"))



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

def CURRENT():
    return __current

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

def MAX_NUM_OF_VERSIONS():
   return __max_num_of_versions

def MESSAGE_LIFE_TIME():
   return __message_life_time


#Add this to tests..
readParameters()
print("**********************globalParametersTest*****************************************")
print("BATTARY_CAPACITY",BATTARY_CAPACITY())
print("TRANSMISSION_RANGE",TRANSMISSION_RANGE())
print("ROBOTS_NOT_MOVE",ROBOTS_NOT_MOVE())
print("ROBOTS_MOVE",ROBOTS_MOVE())
print("ARENA_X",ARENA_X())
print("ARENA_Y",ARENA_Y())
print("BLACK_AREA",BLACK_AREA())
print("GRAY_AREA",GRAY_AREA())
print("LOG_FILE_DIRECTORY","|"+LOG_FILE_DIRECTORY()+"|")
print("WHITE",WHITE()),print("GRAY",GRAY()),print("BLACK",BLACK())
print("OLDER",OLDER()),print("SAME_AGE",SAME_AGE()),print("YOUNGER",YOUNGER())
print("CURRENT",CURRENT()),print("UP",UP()),print("LEFT",LEFT()),print("DOWN",DOWN()),print("RIGHT",RIGHT())
print("INSTANT_SENDING_CHANCE",INSTANT_SENDING_CHANCE())
print("MAX_NUM_OF_VERSIONS",MAX_NUM_OF_VERSIONS())
print("MESSAGE_LIFE_TIME",MESSAGE_LIFE_TIME())


