# set is collection of well define object.
# It is write in "curly brecket".
# It is use for "non repeted data". (It not allow repeted data)
# It is run as "UnOrder".
# set "Unchangeble".

s = {2, 4, 2, 6}
print(s)  # at run time second 2 is not consist.

info = {"krish", True, 1, 5}
print(info)  # at run time you see order is not maintain.

krish = {}
print(type(krish))  #when you run this you see it gives output dictionary not set.

krish_1 = set()
print(type(krish_1))

for value in info:
    print(value)