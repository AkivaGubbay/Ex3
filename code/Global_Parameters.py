class Parameters_const():

    def BATTARY_CAPACITY(self):
        return 50

    def Transmission_range(self):
        return 500

    def Robots_not_move(self):
        return 10

    def Robots_move(self):
        return 90

    def AREANA_X(self):
        return 1000

    def AREANA_Y(self):
        return 1000

    def BLACK_AREA(self):
        # x1 = 0
        #y1 = 0
        # x2 = 999
        #y2 = 0

        #b = [[x1][y1][x2][y2]][[x1][y1][y2][x2]]
        black = [[0][0][999][0]][[0][0][0][999]][[999][0][999][999]][[0][999][999][999]][[2][2][3][6]][[2][3][4][6]]
        return black

    def GRAY_AREA(self):
        gray = [[20][20][50][50]]
        return gray

