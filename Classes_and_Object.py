# Class:
# Class is made by "class" keyword:
class Person:
    name = "Krish"
    Occupation = "Software Devlopment"
    networth = 10

a = Person()   # Making class object
print(a.name, a.networth)    # Try to access variable through object.

# for change inside class data through object:
a.name = "Dhruv"
a.networth = 20
print(a.name, a.networth)  



class Car:
    engine = "400cc"
    tyres = 6
    def fun(self):          # for use class variable must write self inside argument part.
        print(f"My car has {self.engine} engine and {self.tyres} tyres.")       # Here if we want to use class variable then write "self.var_name" so it aumaticaly detect through object variable.

c = Car()
c.fun()







# SELF keyword:
# self means vo object jiske liye class call kiya ja rha he.
# self means that object for which class being called.

class Person1:
    name = ""
    age = 0
    def print(self):
        print(f"My name is {self.name} and my age was {self.age}")

p1 = Person1()
p2 = Person1()

p1.name = "Akash"
p1.age = 20

p2.name = "Mayur"
p2.age = 40

p1.print()    # It output print like that value with method for which object being called
p2.print()













# e.g.
# 1.
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
print("Ans of 1 Question...")
class Vehical:
    def fun(self, max_speed, mileage):   # Here 2, 5 (max_speed and mileage) are both instance attribute
        self.max_speed = max_speed
        self.mileage = mileage

v = Vehical()
v.fun(2, 5) 






# 2.
# Create a Vehicle class without any variables and methods
print("Ans of 2 Question...")
class Vehical:
    pass





