# In this exersice we try to solve snack; water; Gun game.

import random
import os
os.system('cls||clear')


lst = ["snack", "water", "gun"]

user_choice = input("What you want to choose(Snack; Water; Gun): ").lower()
if user_choice not in lst:
    print("You choose wrong try some thing new....")
# print(lst.index(user_choice))


computer_choice = random.choice(lst)
print(f"Computer choice is: {computer_choice}")

u_index = lst.index(user_choice)
c_index = lst.index(computer_choice)

if user_choice == computer_choice:
    print("Draw 😒")
elif (u_index == 0 and c_index == 1) or (u_index == 1 and c_index == 2) or (u_index == 2 and c_index == 0):
    print("You win the match...😃 ")
else:
    print("Computer win the game 💔")



# 
#              S W G
# com=         0 1 2
# player=  S 0 D W L
#          W 1 L D W
#          G 2 W L D

# snack; water; gun

