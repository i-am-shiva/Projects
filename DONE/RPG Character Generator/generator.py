# 2. 🧙‍♂️ RPG Character Generator

# Create a function:
# create_character()
# Ask the player for:
# Name
# Class: warrior, mage, or rogue
# Age
# Give each class different stats.
# Example:

# Name: Shiva
# Class: mage
# Age: 19

# ⚔️ CHARACTER CREATED ⚔️
# Shiva
# Class: Mage
# Health: 70
# Attack: 90
# Defense: 40
# Store the character using a dictionary.

# def create_character():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     clas = input("Enter your class: ").lower()

#     warrior = dict(Class = "Warrior", Health = 100, Attack = 70, Defense = 90)
#     mage  = dict(Class = "Mage", Health = 70, Attack = 90, Defense = 40)
#     rouge = dict(Class = "Rouge", Health = 80, Attack = 85, Defense = 60)

#     print("⚔️ CHARACTER CREATED ⚔️")
#     print(name)
#     if clas == "warrior":
#         for key, value in warrior.items():
#             print(key, value)
#     elif clas == "mage":
#             for key, value in mage.items():
#                 print(key, value)
    
#     elif clas == "rouge":
#             for key, value in rouge.items():
#                 print(key, value)

# create_character()

def create_character():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    clas = input("Enter your class (warrior/mage/rogue): ").lower()

    warrior = {
        "Class": "Warrior",
        "Health": 100,
        "Attack": 70,
        "Defense": 90
    }

    mage = {
        "Class": "Mage",
        "Health": 70,
        "Attack": 90,
        "Defense": 40
    }

    rogue = {
        "Class": "Rogue",
        "Health": 80,
        "Attack": 85,
        "Defense": 60
    }

    if clas == "warrior":
        stats = warrior
    elif clas == "mage":
        stats = mage
    elif clas == "rogue":
        stats = rogue
    else:
        print("Invalid class!")
        return

    character = {
        "Name": name,
        "Age": age,
        **stats
    }

    print("\n⚔️ CHARACTER CREATED ⚔️")
    print(character["Name"])
    print("Class:", character["Class"])
    print("Age:", character["Age"])
    print("Health:", character["Health"])
    print("Attack:", character["Attack"])
    print("Defense:", character["Defense"])


create_character()
    

