# factorial(7) = 7*6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(0) = 1

# factorial(n) = n*factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))


# Fibonachhi:
lst = []
def fibo(n):
    lst.insert(0, 0)  # index, value
    lst.insert(1, 1)
    for i in range(0,n):
        lst.append(lst[i]+lst[i+1])
        
fibo(10)
print(lst)

