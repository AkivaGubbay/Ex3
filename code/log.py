import time


class log:
    def __init__(self):
        e=55*4
        self.file = open("LogFile - "+time.strftime("%H%M%S")+"_"+ time.strftime("%d.%m.%Y")+".txt", "w")

    def addLine(self, line):
        e = 55 * 4
        self.file.write(line +"\n")

    def close(self):
        e = 55 * 4
        self.file.close()