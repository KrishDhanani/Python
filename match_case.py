# It's like switch statement::
x = int(input("Enter number: "))
# x is the variable to match
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 5")
    case _ if x == 3:
        print("It's 0")
    case _:
        print(x)
    

# for default case we use "_"(UnderScore).
# In python "break" keyword is no need to use here. which case is match that case only run.
# In python only one default case is allow.








# Exercise:

# 1.Print all 7 day according to number.
x = int(input("Enter day number: "))
match x:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednsday")
    case 5:
        print("Tuesday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Input")




# 2.Basic calculator.
x = int(input("Enter the first number: "))
exp = input("Enter the expression(+,-,*,/): ")
y = int(input("Enter the second number: "))
match exp:
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '*':
        print(x * y)
    case '/':
        print(x / y)
    case _:
        print("There is no such kind of Expression in our list.")