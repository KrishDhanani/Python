# For that we use "raise" keyword.

a = int(input("enter any number between 5 to 10"))

if a<5 or a>10:
    raise ValueError("Value should be between 5 and 10")



# Quick quize:
# same as upper program but if user input "quit" then don't show error otherwise for all the string give error.

value = input("Enter any number between 5 to 10").lower()

if value == 'quit':
    print("program is getting quit...")
if int(value)<5 or int(value)>10:
    raise ValueError("Value should be between 5 and 10")