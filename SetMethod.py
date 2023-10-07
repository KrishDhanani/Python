# union(); update(); intersection(); intersection_update(); symetric_diffrence(); diffrence(); isdisjoint(); 
# issuperset(); issubset(); add(); update(); remove(); discard(); pop(); del();



s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# union()::
print(s1.union(s2))

# update()::
s1.update(s2)   # it means s2 is add in s1 without repitation.  (s1 is update with value of s2)
print(s1)

# intersection()::
s1.intersection(s2)

# intersection_update()::
s1.intersection_update(s2)
print(s1)

# symetric_diffrence():: (A del B : (A-B) U (A+B))
s3 = s1.symmetric_difference(s2)
print(s3)


# difference()::
s3 = s1.difference(s2)
print(s3)

# disjoint()::
# if intersection is zero then return true.
print(s1.isdisjoint(s2))


# issuperset()::
# is s2 all the element in the s1 then we can say s1 is super set.
print(s1.issuperset(s2))

# vise versa

print(s1.issubset(s2))


# add()::
# for add single item.
s1.add("r")
print(s1)

# update()::
# it is use for add more than one item in set.
s3 = {3,4,5,6}
s1.update(s3)
print(s1)


# remove():
# it is use for the remove perticular data from set.
# if item is not present in set then throw error.
s1.remove(5)


# discard()::
# if item is not present in set then "not" throw error.
s1.discard(2)

# pop()::
# it remove any index single data from the set.
item = s1.pop()
print(item)


# del()::
# for delet entire set.
del s1
# print(s1)   <-- throw error

# clear()::
# use for the clear data from the set.
s1.clear(s2)


# in keyword::
if 2 in s1:
    print("2 is present")
else:
    print("2 not present")
    
