# This fun provide index with element

marks = [1, 20, 56, 98, 23, 78]


# index =0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Krish good job!")
#     index += 1




# Now with enumrate
for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Krish good job!")
    print(index)

# Note: first variable for index always and second is value.
# 
# 
# 
# 
for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print("Krish good job!")
    print(index)
# Here start is just for confusing:
# basically in upper program index is count from 0 but here index count from 1.
# element are all accupy in both cases. 