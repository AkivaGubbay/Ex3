
#private veriables:
__battary_capacity =-1
__transmission_range = -1
__robots_not_move = -1
__robots_move = -1
__arena_x = -1
__arena_y = -1
__black_area = []
__gray_area = []
__log_file_directory = "original"


#Reads data from Parameters.txt file:
def readParameters():
    global __battary_capacity,__transmission_range
    global __robots_not_move, __robots_move, __arena_x
    global __arena_y,__black_area, __gray_area, __log_file_directory

    f = open("Parameters.txt","r")

    #battary_capacity:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __battary_capacity = int(s[len(sub)+2:])
    print("battary_capacity: "+str(__battary_capacity))

    #transmission_range:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __transmission_range = int(s[len(sub)+2:])
    print("transmission_range: "+str(__transmission_range))

    #robots_not_move:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __robots_not_move = int(s[len(sub) + 2:])
    print("robots_not_move: "+str(__robots_not_move))

    #robots_move:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __robots_move = int(s[len(sub) + 2:])
    print("robots_move: "+str(__robots_move))

    #arena_x:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __arena_x = int(s[len(sub) + 2:])
    print("arena_x: "+str(__arena_x))

    #arena_y:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __arena_y = int(s[len(sub) + 2:])
    print("arena_y: "+str(__arena_y))

    #black_area:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    s = s[len(sub) + 2:-1]
    parts = s.split(", ")
    for i in parts:
        point_string = str(i)[1:-1]
        cordi  = point_string.split(",")
        x1,y1,x2,y2 = int(cordi[0]),int(cordi[1]),int(cordi[2]),int(cordi[3])
        area = [x1,y1,x2,y2]
        __black_area.append(area)
    print("black: ",__black_area)  #


    # gray_area:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    s = s[len(sub) + 2:-1]
    parts = s.split(", ")
    for i in parts:
        point_string = str(i)[1:-1]
        cordi = point_string.split(",")
        x1, y1, x2, y2 = int(cordi[0]), int(cordi[1]), int(cordi[2]), int(cordi[3])
        area = [x1, y1, x2, y2]
        __gray_area.append(area)
    print("gray: ",__gray_area)

    #log_file_directory:
    s = f.readline()
    sub = s.rsplit('=', 1)[0]
    __log_file_directory = s[len(sub) + 2:]
    print("log_file_directory: "+__log_file_directory)

    f.close()


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

def LOG_FILE_DIRECTORY ():
    return __log_file_directory

