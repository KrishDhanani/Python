# else statement use with if.
# Also it is use with the "for loop".

for i in range(0,10):
    print(i)
else:
    print("for loop over.")

# e.g. Guess the ans.
# loop ko break kiya gya he so else ka content print hoga ya nhi hoga??
# ans: nhi hoga
print("/////")
for i in range(0,5):
    print(i)
    if i == 4:
        break

else:
    print("loop is over")


