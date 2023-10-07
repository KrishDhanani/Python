# Tupple is same as the list but you can not change it.
# It is write in round brecket and it is immutable.
# When you write only one element in the tupple that time it can not identify.
# for that we at the end add comma



tup = (1,)
print(type(tup), tup)

tup_1 = (1, 3, "krish", True)
print(tup_1)
print(tup_1[0])
print(tup_1[1])
print(tup_1[2])

print("Negative indexing...")
print(len(tup_1))
print(tup_1[-1])
print(tup_1[4-1])
print(tup_1[3])

if 3 in tup_1:
    print("Yes it is present in the tupple.")


# slising::
tup_2 = tup_1[1:3] # n to n-1
print(tup_2)


