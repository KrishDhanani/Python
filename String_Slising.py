name = "Mukesh_Ambani"
print(name[0:5]) 
# It's like 0 to n-1
# Starting index to ending index - 1
print(name[0:4])
print(name[:4]) # Auto start from 0
print(name[:])  # Provide 0 to n-1 string
print(name[-1:1])

# length fun. : len()
# "MUST REMEMBER LENTH FUNCTION START COUNTING 1 NOT 0".
print(len(name)) # "len()" fun. provide length of string

# print(name[0:len(name)-3]) "is eqal to" print(name[0:-3]) output:Mukesh_Amb
print(name[0:len(name)-3])
print(name[0:-3]) # python automaticaly do length-3.

fruit = "Mango"
print(fruit[-2:-1]) # 3:4 

nm = "harry"
print(nm[-4:-2]) # (5-4):(5-2)=1:3