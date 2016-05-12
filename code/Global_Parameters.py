

def BATTARY_CAPACITY():
    return 50

def Transmission_range():
    return 500

def Robots_not_move():
    return 10

def Robots_move():
    return 90

def AREANA_X():
    return 1000

def AREANA_Y():
    return 1000

def BLACK_AREA():
    # format: [X Top][Y Top][X Bottom][Y Bottom]
    p1 = [0, 0, 999,0]
    p2 = [0, 0, 0, 999]
    p3 = [999, 0, 999, 999]
    p4 = [0, 999, 999, 999]
    p5 = [2, 2, 3, 6]
    p6 = [31, 32, 33, 36]

    black = [p1, p2,p3,p4,p5,p6]

    return black

def GRAY_AREA():
    # format: [X Top][Y Top][X Bottom][Y Bottom]
    gray = [[20,20,30,30]]
    return gray

