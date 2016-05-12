from code.Point import Point
from code.Zone import Zone
from code.Robot import Robot
from code.Global_Parameters import *



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

#Test Zone:
print('Test Zone:')
z=Zone()
z.PrintRobot_By_XY()
#z.PrintType_by_XY()

