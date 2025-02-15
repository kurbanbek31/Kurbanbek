#Ex1 m  Write a Python program to subtract five days from current date.
from datetime import *
print(date.today())
x = date.today() - timedelta(5)
print (f"5 days before:{x}")
 
#Ex 2
import datetime
x= datetime.datetime.now()
u = x.day-1
z= x.day +1
x1 = datetime.date(x.year, x.month,u )
x2 = datetime.date(x.year, x.month,z )
print(x1)
print(x)
print(x2)

#Ex 3 Write a Python program to drop microseconds from datetime.

import datetime
d = datetime.datetime.now().replace(microsecond=0)

print(d)

#Ex 4 Write a Python program to calculate two date difference in seconds.


import datetime 

x = datetime.datetime.now()
y = datetime.datetime(2023, 5, 17, 17,41,15)

print((x-y).total_seconds())