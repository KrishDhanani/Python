# When You write method and constructor inside the class don't forgot to add self as argumrnt.


# constructor:
# For constructor you need to use special method called: "__init__(self)"
# When you make object that every time constructor is called.
# main purpose of the constructor is value return krna; and it always return None.


class Person:
    name = "krish"
    age = 19
    def fun(self):
        print(f"My name is {self.name} and my age was {self.age}")

p = Person()
p.fun()

p.name = "Dhruv"
p.age = 20
p.fun()

print(".................................................................")
# Constructor::

class Person1:
    def __init__(self):
        print("I am Constructor...")

a = Person1()
b = Person1()


print(".................................................................")
        
# 
class Human:
    def __init__(self, name, work):
        self.names = name 
        self.works = work
    
    def fun(self):
        print(f"My name is {self.names} and my work was {self.works}")

h = Human("krish", "HR")    # first argument self automatically pass 
h.fun()
h1 = Human("Dhruv", "Software Dev.")
h1.fun()
# h2 = ()   <--- Through error 2 require argument not provided





print(".................................................................")
# DEFAULT CONSTRUCTOR::
# When constructor don't accept any argument from the object and require only self argument 
# then it's known as ...

class Car:
    def __init__(self):
        print("hi i am the constructor...")

c1 = Car()



