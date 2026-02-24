import random
comp = random.choice([1,-1,0])

yourc = input("Enter your input: ")
yourdict = {"s": 1, "w":-1, "g": 0}
reversedict = {1:"Snake", -1:"Water", 0:"Gun"}

userc = yourdict[yourc]

print(f"You choose: {reversedict[userc]} \n Computer choosed: {reversedict[comp]}")

if userc == comp:
    print("It's a Tie!")

else:
    if userc == 1 and comp == -1:
        print("You won")

    elif userc == -1 and comp == 0:
        print("You won")

    elif userc == 0 and comp == 1:
        print("You won")
    
    elif userc == 1 and comp == 0:
        print("Computer won")
    
    elif userc == -1 and comp == 1:
        print("Computer won")

    elif userc == 0 and comp == -1:
        print("Computer won")

    else:
        print("Something went wrong...")