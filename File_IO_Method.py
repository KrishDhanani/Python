# Now we see some method::
# readline();  writeline();




# readline()::
# write bellow three line in file "file_name.txt" (before it remove all content of file)::
# 45,56,89
# 75,94,23
# 32,45,65


f = open('file_name.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()


print("\n")


f = open('file_name.txt', 'r')
# e.g.
j=0
while True:
    j = j+1
    line1 = f.readline()
    if not line1:
        break

    m1 = int(line1.split(",")[0])
    m2 = int(line1.split(",")[1])
    m3 = int(line1.split(",")[2])

    print(f"Marks of student {j} in Maths is:{m1*2}")
    print(f"Marks of student {j} in English is:{m2*2}")
    print(f"Marks of student {j} in SST is:{m3*2}")

    print(line1)
    
















# Writline()::
# For write sequence of string to a file.
f = open("file_name.txt", 'w')
line = ['line 1\n','line 2\n','line 3\n']
f.writelines(line)
f.close()
# Note: after write string line not go automatically to next for that you need to use: (\n) or (loop inside \n)
