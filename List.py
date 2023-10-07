# List; in keyword; List comprehention.
# List write in squre brecket; it is muttable.

marks = [3,5,6]   # List are start from 0 index.
print(marks)
print(type(marks))

print(marks[0])   # It's first index element provide
print(marks[1])

List = [1,2,3,"krish",True,"kk",3,56,7,8]

print(List[-2])  # Negative Index
print(List[len(List)-2])  #Positive Index
print(List[5-2])
print(List[3])  # Output: "krish"

# "in" keyword:
# Through it you can find out keyword inside list or not.
if 7 in List:
    print("Yes")
else:
    print("no")

print(List)
print(List[1:])
print(List[1:6])  # Goes: n to n-1 
print(List[1:6:2])



# list comprehention::
# It basically on the time make new list.
lst = [i for i in range(0,10)]
print(lst)

lst_1 = [i*i for i in range(0,10)]
print(lst_1)

lst_2 = [i for i in range(0,10) if i%2==0]
print(lst_2)





















# Example:
# 1.
# Write a Python program to sum all the items in a list.
print("Ans of 1 quistion...")
lst = [1,2,3,4]
s = sum(lst)
print(s)






# 2.
# Write a Python program to multiply all the items in a list.
print("Ans of 2 Question...")
mul = 1
lst = [1,2,3,4]
for i in lst:
    mul *= i
print(mul)






# 3.
# Write a Python program to get the largest number from a list.
# Write a Python program to get the smallest number from a list.
import math
print("Ans of 3 Question...")
largest = -math.inf 
smallest = math.inf                     # minus infinite
for i in lst:
    if largest < i:
        largest = i
    if smallest > i:
        smallest = i
print(largest)
print(smallest)






# 4.
# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
print("Ans of 4 Quedtion...")
count = 0
str = ['abc', 'xyz', 'aba', '1221']
for i in str:
    if i[0] == i[len(i)-1]:
        count += 1
print(count)






# 5.
# Write a Python program to get a list, 
# sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
print("Ans of 5 Question...")
lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for index,value in enumerate(lst):
    for i in range(index+1, len(lst)):
        if lst[index][1] > lst[i][1]:
            temp = lst[index]
            lst[index] = lst[i]
            lst[i] = temp
print(lst)









# 6.
# Write a Python program to remove duplicates from a list.
print("Ans of 6 Question...")
lst = [1,6,3,5,1,2,8,6,9]
s = set(lst)
print(s)







# 7.
# Write a Python program to check if a list is empty or not.
print("Ans 7 of Question...")
lst = []
if len(lst) == 0:
    print("The list was empty")
# another answer... 
if not lst:
    print("The list is empty...")






# 8.
# Write a Python program to clone or copy a list.
print("Ans of 8 Question...")
lst = [1,3,5,7,9]
lst1 = list(lst)
print(lst1)






# 9.
# Write a Python program to find the list of words that are longer 
# than n from a given list of words.
print("Ans of 9 Question...")
lst = ["krish dhanani", "ab", "dhruv dhanani", "mahi", "sneha", "yash"]
for i in lst:
    if len(i) > len(lst):
        print(i)






# 10.
# Write a Python function that takes two lists and returns True 
# if they have at least one common member.
print("Ans of 10 Question...")
lst = [1, 4, 6, 8]
lst1 = [5, 4, 8, 0]
for i in lst:
    if i in lst1:
        print("True")
        break







# 11.
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
print("Ans of 11 Question...")
lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in lst:
    if lst.index(i) == 0 or lst.index(i) == 3 or lst.index(i) == 5:
        lst.pop(i)
print(lst)








# 12.
# Write a Python program to generate a 3*4*6 3D array whose each element is *.













# 13.
# Write a Python program to shuffle and print a specified list.
import random
lst = [1,3,2,4]
random.shuffle(lst)
print(lst)