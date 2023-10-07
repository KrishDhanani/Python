# seek(); tell(); truncate();


# seek() and tell():
# in file: file_name1.taxt first write "1234567890abcdefghi" then see this both fun.

with open('file_name1.txt', 'r') as f:
    print(type(f))

    # Move to the 10th byte of the file and start reading from there.
    f.seek(10)   # seek provide facility to not start reading line from the start you can start where you want.
    # 10 byte age khiska dega and start reading from there.


    # After the seek if you wantt to know where you are for that use tell().
    print(f.tell())    # provide number

    # reed next 5 byte (start reading after the seek)
    data = f.read(5)
    print(data)





# truncate():
# For this fun. first upper all code comment.

with open('file_name1.txt','w') as f:
    f.write("krish dhanani")  # in file we write total 13 char
    f.truncate(5)   # after truncate see how many char left 
    # It try to in file left only 5 char.

with open('file_name1.txt', 'r') as f:
    print(f.read())