# Dictionary::
# we need to write it in curly brecket.
# After version 3.7 dictionary are ordered before it is unOrdered.


dic = {
    "human being":"krish",
    "key":"value",
    23 : "neha"
}
print(dic)
print(dic["human being"])   # It return's the value of key.


# Accessing element::
print(dic[23])                     # If we try to retrive like this then if item not present in dic then show "key error"
print(dic.get(24))                 # If we try to retrive like this and if item is not present in dic then show "None" (Not give error) 



# for retrive Keys and value::
print(dic.keys())  # return all the keys
print(dic.values())  # return all the values
print(dic.items())    # return all the item with key and value  

# retrive all the values:
for key in dic.keys():
    print(dic[key])

for key,value in dic.items():
    print(f"{key}:{value}")