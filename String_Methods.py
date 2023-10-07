# Strings are immutable
a = "Krish"
print(len(a))

# Upper case
print (a.upper())

# lower case
print(a.lower())

# rstrip() : "It removes ANY trailing character".
b="krish!!!"
print(b.rstrip("!"))

# replace()
print(b.replace("krish","romil"))

# split() : basically its convert string to list (from space) 
c="krish dhanani"
print(c.split(" "))

# capitlize() : it convert every first letter of the string into capital form
# and other all letter if capital then it conver to small form 
print(c.capitalize())

d = "hello,How are you?"
print(d.capitalize()) 

# center() : it align string to center at the output
print(d.center(23)) # here 23 space after it print the String

# count() : it return how many time perticular character/string is accur in the string
print(d.count("h"))

# endswith() : return boolean value 
a1 = "krish is clever boy"
print(a1.endswith("boy"))
print(a1.endswith("is",4,8))

# find() : return string starting index // if there is no accurence string in main string then it "return -1".
print(a1.find("clever"))

# index() :
print(a1.index("clever")) #if there is no accurence string in main string then it return "exeption".

# isalnum() : for check the string is alphanumeric or not?
# alphanumeric are: A-Z,a-z,0-9
print(a1.isalnum())

# isalpha(): for check the string is alphametic or not?
# alphametric: A-Z,a-z
print(a1.isalpha())

# islower(): for check string is in lowercase or not?
print(a1.islower())

# isprintable(): check the string not contain any /n or like that character inside string
print(a1.isprintable())
# if inside string like /n character is there then it return faulse

# isspace(): check "all over" string contain space or not
print(a1.isspace())

# istitle():
# check wether the string is like title form
print(a1.istitle())

# isupper():
print(a1.isupper())

# startwith():
print(a1.startswith("krish"))

# swapcase(): It means that check if the cha. is lower then convert to upper & vise varsa.
print(a1.swapcase())

# title(): convert string to title
print(a1.title())