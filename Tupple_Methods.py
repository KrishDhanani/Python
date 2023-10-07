#  Tupple Methods
# Tupple Manupulating; tupple concatinate; count(); index(); len()

# Tupple Manupulating::
tup = ("a", "b", "c", "d", "e",)
lst = list(tup)
lst.append("f")   # add item
lst.pop(2)        # remove item
lst[2] = "g"      # set new item
tup = tuple(lst)
print(tup)


# tupple can be concatinate
tup_1 = (1, 2,)
tup_2 = (3, 4,)
tup_3 = tup_1 + tup_2
print(tup_3)


# count()::
tup_4 = (0, 0, 0, 1, 1, 2, 3, 5, 5,)
print(tup_4.count(0))


# index()::
print(f"0 accurance: {tup_4.index(0)}")
print(f"1 accurance in slising: {tup_4.index(1, 2, 5)}")  # Do slising tup from 2 to 4(5-1) and find 1 first accurance

# len()
print(len(tup_4))
