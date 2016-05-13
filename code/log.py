import time


class log:
    def __init__(self):
        #self.file = open("LogFile - "+time.strftime("%H%M%S")+"_"+ time.strftime("%d.%m.%Y")+".txt", "w")
        self.file = open("LogFile.txt", "w")
    def addLine(self, line):
        self.file.write(line +"\n")

    def close(self):
        self.file.close()