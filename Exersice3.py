# Create game which is kon bnega crorpati.
# Use only list datatype.
# Also print user reward amount.

import random
Questions = [
    ["Who is the Father of our Nation?","Mahatma Gandhi"],
    ["Who was the first President of India?","Rajendra Prasad"],
    ["Which is the most sensitive organ in our body?","Skin"],
    ["Brain of computer is?","Cpu"]
]
flag = True
reward = 100
while flag:
    count = random.randint(0,3)
    print(Questions[count][0])
    ans = input("\nAnswer: ").title()
    if Questions[count][1] == ans:
        reward += 100
    else:
        print("Your reward is", reward, "Rs.")
        flag = False