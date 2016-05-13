from code.Global_Parameters import *


class log:
    def __init__(self):
        #self.file = open("LogFile - "+time.strftime("%H%M%S")+"_"+ time.strftime("%d.%m.%Y")+".txt", "w")
        self.file = open(LOG_FILE_DIRECTORY(), "w")

    def addLine(self, line):
        self.file.write(line +"\n")

    def close(self):
        self.file.close()