# Exception Handling::
# Basically it is usefull when the error is accure.
# 
# we can catch error through "try" & "except".



# In this code if user input "charecter" insted of "int" then error is accured.

a = input("Enter the number: ")
print(f"The multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except Exception as e:                                      # e is object. Also for printing e you can see that which type of error is accured.
    print(e)
    print("Error is accured. Invalid Input!!!")

print("Program run successfully.")   # if error is accured but still we try to run this line.





# Try to catch more exception::
# e.g.
try:
    a = int(input("Enter the value: "))
    lst = [3, 5, 9]
    print(lst[a])
except ValueError:
    print("You entered insted of number anything else.")
except IndexError:
    print("Index is out of range.") 