import math as m

x = -1

y= 1

move = 0.5

oldpos = m.sqrt((x)**2+(y)**2)

newpos = m.sqrt((x+move)**2 + (y)**2)

difference = newpos/oldpos

print(difference)


