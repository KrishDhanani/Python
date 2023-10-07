# conditional Operator:
# >,<,>=,<=,==,!=

a = int(input("Enter your age: "))
if a>18:
    print("You can Drive")
else:
    print("You can not Drive")

# Here Indentation is important.


# with elif::
a = int(input("Enter the num: "))
if a < 0:
    print("Number is negative.")
elif a == 0:
    print("Number is equal to zero.")
else:
    print("Number is positive.")
print("i am Happy Now.") # This line every time exicute.


# Nested if - else:
a = 20
b = 1
if a == 20:
    if b >= 0:
        print("I am b")
else:
    print("Try again.")


# Now we try one Exercise:
# In this Exsercise you need to say user to Good_Morning; Good_Afternoon; Good_Night acording to current time.
# Baki.

import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if (hour>0 and hour<12):
    print("Good Morning!!!")
elif (hour>=12 and hour<17):
    print("Good Afternoon!!!")
else:
    print("Good Night!!!")





# Example:

# 1.
# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
year = int(input("Enter your service year in our company: "))
salary = int(input("Enter your salary: "))
if year > 5:
    salary = salary + (salary*0.05)
    print(f"You get personal Bonus and so your final this year incom is:{salary}Rs. ")







# 2.
# Take values of length and breadth of a rectangle from user and check if it is square or not.
length = int(input("Enter the length of rectangle: "))
bredth = int(input("Enter the bredth of rectangle: "))
if length == bredth:
    print("It is squre")







# 3. A 4 digit number is entered through keyboard. 
# Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895
n = int(input("Enter the number: "))
n1 = 0
while n != 0:
    rem = n%10
    n1 = n1*10 + rem 
    n = int(n/10)

print(n1)






# 4. Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".

age = int(input("Enter your age: "))
sex = input("Enter your sex(M or F): ").lower()
marital = input("Enter your marital status(Y or N): ").lower()
if sex == 'f':
    print("she will work only in urban areas")
elif sex == 'm':
    if 20 < age < 40:
        print("You can work either urbun or rural areas.")
    elif 40 < age < 60:
        print("You can work only urban area.")
    else:
        print("Error")







# 5.
# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but 
# if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

# Remember below code is according to upper condition.
year = int(input("Enter year you want to check: "))
if year % 4 == 0:
    if 1900 < year < 2100:
        if year % 400 == 0:
            print("It ia leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")
