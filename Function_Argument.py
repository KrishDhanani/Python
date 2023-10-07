def avg(a,b):
    print("The avg is:", (a+b)/2)

avg(10,20)

# Default Argument:  Inside the fun. we provide value of argument.
def avg(a=8,b=9):
    print("The avg is:", (a+b)/2)

avg()
# 
def avg(a=8,b=9):
    print("The avg is:", (a+b)/2)

avg(a=9)  # now a = 9 is consider.



# Keyword Argument: At function call time not matter in calling time in which order you pass the value of Argument.
def avg(a,b):
    print("The avg is:", (a+b)/2)

avg(b=20, a=10) # It's impoprtant to you give here at right argument to right value.



# Required Arguments: It means that you "must' give argument value.
def avg(a,b=20):    # It means that at variable calling time you must need to give the value of a incase you not give the value of b than it concide rfrom here. 
    print("The avg is:", (a+b)/2)

avg(a=10)