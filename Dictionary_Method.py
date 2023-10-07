# update(); clear(); pop(); popitem(); del()

ep1 = {
    122 : 45,
    123 : 89,
    567 : 69,
    670 : 69
}

ep2 = {
    222 : 56,
    856 : 75,
    56 : 45,
    85 : 7
}

# It return the ep1 + ep2 
ep1.update(ep2)  # ep1 getting updated
print(ep1)


# clear()::
# remove all the data from the dic.
ep1.clear()  # empty dic provide
print(ep1)

# pop()::
ep2.pop(222)
print(ep2)

# popitem()::
# it remove last key;value pair from the dic.
ep2.popitem()
print(ep2)


# del()::
# for delete entier dic.
del ep1
# print(ep1)  <-- throw error

del ep2[85]
# for remove perticular data
print(ep2)