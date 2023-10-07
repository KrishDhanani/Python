# Finally keyword
# whether error is accure or not finally keyword under written code "must run".

try:
    l = [5, 6, 78, 45]
    x = int(input("Enter the index: "))
    print(l[x])
except Exception as e:
    print("Some eror is accure.")

finally:
    print("I am always exicuted.")



# When it is use::
# After return keyword in fun. fun. is ended but if we want to still run the code then we use finally keyword.

def fun(x):
    l = [5, 6, 78, 45]
    try:
        print(l[x])
        return 0
    except:
        print("Some error is accured")
        return 1
    finally:
        print("I am always exicuted.")

x = fun(0)
print(x)