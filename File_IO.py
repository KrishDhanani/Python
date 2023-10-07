# Several ways to manupulate file.
# 'r' for reading
# 'w' for writing
# 'a' for appending
# 'w+' for create file
# 
# 
# syntax:
# file_object = open('file_name','mode')
# 
# Reading file::
f = open('myfile.txt', 'r')     # (file_name, mode)
# 'r' mode is default mode if you write like this::
# f = open('myfile.txt')    
# also it is fine to write like this.
text = f.read()
print(text)
f.close()
# 
# 
# 
# 
# 
# Writing file::
f = open('myfile.txt', 'w')
f.write("I am Fine.")
f.close()
# Note: if file_name writen file is not exist then it automatically made that name file and write data inside it.
# when you run this file that time all previous writen data is delete and add new text.
# 
# 
# 
# 
# 
# 
# File Append mode::
# insted of using write for add new data with not previous data we use this fun.
f = open('myfile.txt', 'a')
text = f.write("How are You?")
f.close()
# 
# 
# 
# 
# 
# 
# File create mode::
# In this mode we are create file and if file was already exist then return error.
f = open('file_name.txt', 'w+')
# 
# 
# 
# 
# 
# "with" Keyword:
# no need of write long code....
with open('myfile.txt', 'a') as f:
    f.write("hey i am inside the file.")