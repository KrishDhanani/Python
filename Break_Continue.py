# For at perticuler iteration if user want to exit the loop that time we use break.
for i in range(0,5):
    if i == 3:
        break
    print(i)

# For at perticuler iteration if user want to skip that iteration than use continue.
print("/////")
for i in range(0,5):
    if i == 3:
        continue
    print(i)