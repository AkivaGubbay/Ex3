from code.Point import Point
from code.Zone import Zone
from code.Robot import Robot
from code.log import log
from code.Global_Parameters import *

"""
#Test Point:
print('Test Point:')
p = Point(4,3)
print(p.toString())

#Test Robot:
print('Test Robot:')
r = Robot(12)
print('initial battery: '+str(r.battery_status))
r.messages.append('Joey: How you doing..')
print(r.messages.pop())
print("tostring: "+ r.toString())



#log
Mylog = log()

#Test Zone:
print('Test Zone:')
z=Zone(Mylog)
z.PrintRobot_By_XY()
#z.PrintType_by_XY()

#close log
Mylog.close()


#String test:
s1 = "akiva = 24"
s2 = s1.rsplit('=', 1)[0]
print (s1.rsplit('=', 1)[0])
print ( s1[len(s2)+2:])
readParameters()
print(BATTARY_CAPACITY())
print(TRANSMISSION_RANGE())   """


readParameters()
print(BATTARY_CAPACITY())
print(ARENA_X())
print(TRANSMISSION_RANGE())
print(ROBOTS_NOT_MOVE())
print(ROBOTS_MOVE())
print(ARENA_X())
print(ARENA_Y())
print(BLACK_AREA())
print(GRAY_AREA())
print(LOG_FILE_DIRECTORY())


#s = "246800"
#print(int(s[2]))
