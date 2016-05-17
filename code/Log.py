from code.Global_Parameters import *


class Log:
    def __init__(self):
        global file
        #self.file = open("LogFile - "+time.strftime("%H%M%S")+"_"+ time.strftime("%d.%m.%Y")+".txt", "w")
        file = open(LOG_FILE_DIRECTORY(), "w")

    def addLine(line):
        file.write(line +"\n")

    def close(self):
        file.close()
