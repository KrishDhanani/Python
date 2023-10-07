# append(); sort(); revrse-sort(); index(); count(); copy(); 
# insert(); extend(); concatinating_list; shuffle(); 


l = [1, 5, 3, 6, 76, 4, 34]
print(l)


# append()::
# it's for the add single element to the list.
l.append(4) 
print(l)


# assending / dessending order sorting()::
l.sort()  # For assending Order.
print(l)

l.sort(reverse=True)  # For reverse sorting.
print(l)


# index()::
l = [1, 5, 3, 6, 76, 4, 34]
print(l.index(5))


# count()::
print(l.count(4))


# copy()::
m = l.copy()
m[0] = 0
print(l)
print(m)


# insert()::
# list_name.insert(index, new-element)
l.insert(1,899)
print(l)


# extend()::
# Use for add multiple element in the list.
m = [1000, 200, 300]
l.extend(m)
print(l)


# concatinate_list::
k = l + m
print(k)


# shuffle()::
# For change randomly position of list element
import random
lst = [1,3,2,4]
random.shuffle(lst)
print(lst)


# pop()::
# It is use for delet element randomly or specified element from the list.
l = [1, 5, 3, 6, 76, 4, 34]
l.pop()  #<-- it remove random element from list
l.pop(0)  #<-- at provided index element remove.
print(l)


