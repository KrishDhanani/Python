# lembda fun is fun. which was not have name and use for 
# lembda fun is mostly use for one line of fun body. 
# they are also use as an argument.(that time it not have name)


# def double(x):
#     return x*2
# insted of writing all fun now see lambda fun.


# lambda fun. ::
# fun_name = lambda what_fun_take_variable : what_fun_return
double = lambda x : x*2

print(double(5))

# e.g.
avg = lambda x,y : int((x+y)/2)
cube = lambda x : x**3
print(avg(2,4))
print(cube(4))



# inside fun pass another fun.
def sum(fx, value):
    return fx + value

square = lambda x : x * x 

print(sum(square(2), 6))

# another e.g.
def fun(fx, value):
    return 6 + fx(value)

print(fun(lambda x : x * x, 2))












print("Practice Questions...")
# e.g.
# 1.
# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48
print("Practice 1 ans....")
# 15 to add number
val = lambda x: x+15
print(val(4))

# x multiply with y
val = lambda x,y : x*y
print(val(10, 20))





# 2.
# Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
print("Practice 2 ans....")

val = lambda x,a : x**a
print(val(15,2))
print(val(15,3))





# 3.
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
print("Practice 3 ans....")