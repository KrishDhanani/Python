# In this file we learn about loops.
name = "krish"
for i in name:
    print(i)

colors = ["red","yellow","green"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# range()
# I want number from 0 to 10.
for i in range(0,11):
    print(i)
# range(starting_index, ending_index+1, step)

for i in range(0,10,2):
    print(i)










# EXAMPLE:

# 1.
# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included).
print("ans 1 question.....")
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)








# 2.
# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
cel = float(input("Enter the value of celcious: "))
fer = float(input("Enter the value of ferenhit: "))
f_to_c = lambda cel : (cel/5) + 3.55  # for cel to fer
c_to_f = lambda fer : 5 * (fer - 3.55)  # for fer to cel
ferenhit = f_to_c(cel)
celcious = c_to_f(fer)
print(f"The celcious to ferenhit of value {cel} is: {ferenhit}°F")
print(f"The ferenhit to celcious of value {fer} is: {celcious}°C")







# 3.
# Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *














# 4.
# Write a Python program that accepts a word from the user and reverses it.
print("ans of 4 ...")
word = input("Enter the word: ")
lst = list(word)
lst1 = []
x = len(lst)-1
for i in range(len(lst)):
    index = x - i
    lst1.append(lst[index])
print(''.join(lst1))







# 5.
# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd = 0
even = 0 
for i in numbers:
    if i % 2 == 0 or i == 0:
        even +=1
    else:
        odd += 1
print(odd, even)







# 6.
# Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print("ans of 6 is...")
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in range(len(datalist)):
    print(f"{datalist[i]} type is : {type(datalist[i])}")






# 7.
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
print("ans of 7 is.... ")
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i)







# 8.
# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
print("ans of 8 is...")
lst = []
def fibo(n):
    lst.insert(0, 0)  # index, value
    lst.insert(1, 1)
    for i in range(0,n):
        lst.append(lst[i]+lst[i+1])
        
fibo(10)
print(lst)








# 9.
# Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
print("ans of 9 is...")
for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 








# 10.
# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
print("ans of 10 is...")
m = int(input("Enter row: "))
n = int(input("Enter column: "))
lst = []
for i in range(m):
    index = i
    lst1 = []
    for j in range(n):
        lst1.append(i*j)
    lst.insert(index, lst1)
print(lst)








# 11.
# Write a Python program that accepts a sequence of lines 
# (blank line to terminate) as input and prints the lines as output (all characters in lower case).
print("ans of 11 is...")











# 12.
# Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
# The program will print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
print("ans of 12 is...")
Data = input("Enter the numbers: ")
lst = list(Data.split(","))
for i in lst:
    if int(i) % 5 == 0:
        print(i)









# 13.
# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
print("ans of 13 is...")
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digit = ["1","2","3","4","5","6","7","8","9","0"]
str = input("Enter what you want check: ")
l = 0
d = 0
for i in str:
    if i in letter:
        l += 1
    elif i in digit:
        d += 1
print(f"letter are {l} \n digits are {d}")










# 14.
# Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. 
# After that, each dog year equals 4 human years.
# Expected Output:
# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73
print("ans of 14 is...")
x = int(input("Enter the dog year in human years: "))
d_age = 0
for i in range(1,x+1):
    if i == 1 or i == 2:
        d_age += 10.5
    else:
        d_age += 4
print(f"Your dog age in human years: {d_age}")
