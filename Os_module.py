# NOTE: "///////DON'T RUN THIS FILE///////"

import os




# For make folder::
if (not os.path.exists("data")):
    os.mkdir("data")     

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")      # in the data folder it make 1 to 100 name another 100 folder





# For change the name of folder::
# rename::

for i in range(0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")     # first sourse name then destination name.






# For getting info. at perticular data which are the folder is there::

folder = os.listdir("data")

print(folder)
# for again go inside all that folder:: means go inside folder and see which kind of file are there for it::
# first make one file in any tutorial folder. 
for folder in folder:
    print(folder)
    print(os.listdir(f"data/{folder}"))





# For getting info in which directory you are::
print(os.getcwd())




# For changing directory::
os.chdir("/User")




# Explore more feature of os Module.