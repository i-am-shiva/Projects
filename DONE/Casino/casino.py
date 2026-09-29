# ### 3. 🎰 Mini Casino

# Start with:

# Coins = 100

# The player can repeatedly choose:
# 1. Guess the number
# 2. Coin flip
# 3. Quit

# For guessing:
# -  Computer chooses 1–10. 
# -  Player guesses. 
# -  Correct → +30 coins 
# # -  Wrong → -10 coins 

# 🪙 Coin Flip Rules
# Computer randomly chooses Heads or Tails.
# Player chooses Heads or Tails.
# If the player is correct → +20 coins
# If the player is wrong → -10 coins
# The game continues after the result.
# If coins reach 0, the casino stops.

# Stop if:
# Coins = 0
# Use functions:
# guess_game()
# coin_flip()

import random 
coin = 100
def guess_game(coins):
    number = random.randint(1, 10) 
    #CHEATING - print ("the number is: ", number)
    num = int(input("Enter the number: "))
    if number == num :
        coins += 30
    else:
        coins -= 10
    return coins

def coin_flip(coins):
    choice = random.choice(["heads", "tails"])
    inp = input("Enter Heads or Tails :").lower()
    if choice == inp:
        coins += 20
    else:
        coins -= 10
    return coins
    
while True:
    print("1. Guess the number")
    print("2. Coin flip")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        coin = guess_game(coin)
        print(coin)
        if coin == 0:
            print("Oops out of coins...")
            break


    elif choice == "2":
        coin = coin_flip(coin)
        print(coin)
        if coin == 0:
            print("Oops out of coins...")
            break


    elif choice == "3" :
        print("Thanks for playing 😊!!") 
        break

    else:
        print("Invalid Input")
