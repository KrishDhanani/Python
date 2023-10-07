x = 4  # Global Variable
print(x)


def fun():
    x = 5  # Local Variable
    y = 5  # Local Variable
    print("I am Function.")
    print(y , x)

fun()
# print(y)  <-- Throw error


# when function is return that time local variable is distroy and global variable is as it is


a = 10  # Global var.
def fun1():
    global a    # Now we insert global variable
    a = 20   
    print(a)

fun1()
print(a)  # return 20  because it is updated.

