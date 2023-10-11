import mod1
import theater_mod as th
from theater_mod import price as p
import sys
import travel.thailand
from travel.vietnam import VietnamPackage as viet

num = mod1.add(5,2)
a = mod1.Math()
num2 = a.solv(2)
print(num, num2)

th.price(5)
th.price_morning(4)
p(10)

print(sys.path)



trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
viet().detail()

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
import bs4

print(inspect.getfile(bs4))
print(inspect.getfile(thailand))