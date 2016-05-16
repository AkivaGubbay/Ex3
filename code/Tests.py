from code.Global_Parameters import *


def globalParametersTest():
    readParameters()
    print("**********************globalParametersTest*****************************************")
    print("BATTARY_CAPACITY", BATTARY_CAPACITY())
    print("TRANSMISSION_RANGE", TRANSMISSION_RANGE())
    print("ROBOTS_NOT_MOVE", ROBOTS_NOT_MOVE())
    print("ROBOTS_MOVE", ROBOTS_MOVE())
    print("ARENA_X", ARENA_X())
    print("ARENA_Y", ARENA_Y())
    print("BLACK_AREA", BLACK_AREA())
    print("GRAY_AREA", GRAY_AREA())
    print("LOG_FILE_DIRECTORY", "|" + LOG_FILE_DIRECTORY() + "|")
    print("WHITE", WHITE()), print("GRAY", GRAY()), print("BLACK", BLACK())
    print("OLDER", OLDER()), print("SAME_AGE", SAME_AGE()), print("YOUNGER", YOUNGER())
    print("CURRENT", CURRENT()), print("UP", UP()), print("LEFT", LEFT()), print("DOWN", DOWN()), print("RIGHT",RIGHT())
    print("INSTANT_SENDING_CHANCE", INSTANT_SENDING_CHANCE())
    print("MAX_NUM_OF_VERSIONS", MAX_NUM_OF_VERSIONS())
    print("MESSAGE_LIFE_TIME", MESSAGE_LIFE_TIME())


globalParametersTest()
readParameters()
print(BATTARY_CAPACITY())

