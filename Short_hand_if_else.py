# It goes left to right.

a = 10 
b = 20
print('a') if a>b else print('b')
print("a") if a>b else print('=') if a==b else print('b') 

c = 9 if a>b else 10
print(c)