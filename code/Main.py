from code.Point import Point
from code.Robot import Robot


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