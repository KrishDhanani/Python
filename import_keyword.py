import math
print(math.floor(4.9597))

print(math.sqrt(9))

# If we want specific math function then we use "from" keyword
from math import pi, sqrt
print(math.sqrt(4))
print(math.pi)
# now you can not use floor like function from math because you import specific function from the math library.



# from math import *
# when we write like this then all the fun. is import.



# "as" keyword:
from math import sqrt as s
print(s(9))

from math import sqrt, floor as f
# here floor is import as f and sqrt is as it is.




# for see which are the fun in math.
print(dir(math))       # similarlly for other library we can write like this.
print(type(math.comb))



# e.g.
from Function import g_mean     # see Function file.
x = g_mean(10, 20)
print(x)


import Function as gm
p = gm.g_mean(10, 20)
print(p)


