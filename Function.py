# Funciton define with "dif" keyword.
def g_mean(a,b):
    mean = (a*b)/a+b
    return mean

x = g_mean(10,20)
print(x)

# 
def is_greater(a,b):
    if a>b:
        print("a is greater than b.")
    elif b>a:
        print("b is greater than a.")

print(is_greater(20,30))

# 
def fun():
    pass  # When you write "pass" inside the function that time no need to write body.

# Ther is two types of function are therre::
# 1.Built_in function
# 2.User_define function

# e.g. Built-in function:
# min(),max(),...

# e.g. user define function:
# which is user need to write with def keyword
