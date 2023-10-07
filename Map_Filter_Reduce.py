# Map; filter; Reduce...
# Hiere Order Fun. : It is function which tack fun inside fun...
# map; filter; reduce all are the hiere order fun.


# MAP::
# Map mostly apply on list.
# "map fun return object so don't forget convert in list."
def cube(x):
    return x*x*x

print(cube(3))

l = [1,2,3,4,5]
l1 = []
for i in l:
    l1.append(cube(i))

print(l1)
# Insted of doing all this now see what we do....


l1 = list(map(cube, l))
print(l1)
# first: function; second: that fun. on which list you want to apply;  write like that....

print(list(map(lambda x : x * x, l)))   # like also you can pass lambda fun.





# FILTER::
# Specific type of element you want to inside the list that time use filter.
# "filter fun return object so don't forget convert in list."
# filter is work upon the "BOOLEAN" value only.

def filter_function(a):
    return a>2

l1 = list(filter(filter_function, l))
print(l1)

print(list(filter(lambda x : x>2, l)))   # like also you can pass lambda fun.





# REDUCE::
# for use reduce we need to first import it.
from functools import reduce
l = [1,2,3,4,5]


# for calculate sum of two number.
# path of running program.
# 1+2
# [3,3,4,5]
# [6,4,5]
# [10,5]
# [15]
# 

def mysum(x, y):
    return x+y

sum = reduce(mysum, l)
print(sum)

# 
print(reduce(lambda x, y : y/x , l))  # like we can also use lembda fun.


