#Sand Boxing... Just playing around.

'''4 ways to import from a module in the same directory'''
#import sand_box_objects
#import sand_box_objects as sbo
#from sand_box_objects import Point
from sand_box_objects import *

p1 = Point(4,5)
p2 = Point(2,3)


print(p2.get_x(), p2.get_y())
print(p2.distance_from_origin())
print(p2)


