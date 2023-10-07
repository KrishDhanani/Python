# is vs ==
# Basically "is" was compare to exact location of memory.
# and
# "==" was compare to value.

a = 4
b = '4'
c = 4
d = '4'
print(a is b)  # Exact location in memory
print(a == b)  # value

print(a == c)
print(b == d)


# 
print("......")

# case1:
x = 2
y = 2
print(x is y)
print(x == y)

# case2:
x = [1,2,3]
y = [1,2,3]
print(x is y)
print(x == y)

# Here basically  in case1 the variable value is constant which is immutable so python think that not to wast space and assign at one location.
# But
# in second case list may be mutable so python assign both the list at different location.

print("///////")
x = (1,2,3)
y = (1,2,3)
print(x is y)  # true because tupple was not changeble.
print(x == y)