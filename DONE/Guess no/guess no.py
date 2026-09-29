import random
num = random.randint(1, 100)
guess = 1000
no_guess = 1
#print(f"Yeah you are right!!!, The number was {num}")
while num != guess:
    guess = int(input("Enter the no: "))

    if num > guess:
        print("The guess is lower")
        no_guess += 1

    else:
        print("The guess is higher")
        no_guess += 1

print(f"Yeah you are right!!!, The number was {num}")
print("Total no of guesses: ", no_guess)