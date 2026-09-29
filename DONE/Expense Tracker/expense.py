# 6. 💰 Expense Tracker

# Build a mini expense tracker.

# Menu:

# ====== EXPENSE TRACKER ======

# 1. Add expense
# 2. Show expenses
# 3. Total spending
# 4. Highest expense
# 5. Category spending
# 6. Exit

# Example:

# Add expense:
# Amount: 250
# Category: Food

# Add expense:
# Amount: 120
# Category: Transport

# Then:

# Total spending: ₹370

# Food: ₹250
# Transport: ₹120

# Highest expense: ₹250

# Store the data using dictionaries/lists.

# Extra challenge: Create separate functions for every menu operation.
# 1. Add expense
# 2. Show expenses
# 3. Total spending
# 4. Highest expense
# 5. Category spending
# 6. Exit
food = []
transport = []

def add():
    inp = int(input("Enter the Amount : "))
    typ = input("Enter type of Expense : ").lower()
    if typ == "food" :
        food.append(inp)

    elif typ == "transport" :
        transport.append(inp)


def show():
    data = dict(fooddata = food, transportdata = transport)
    print(data)

def total():
    totalspendlist = food + transport
    totalspend = 0
    for i in totalspendlist:
        totalspend += i

    print("Total Spending = " , totalspend)

def highest():
    if not food and not transport:
        print("No expenses added yet.")
        return

    if food:
        fhigh = max(food)
    else:
        fhigh = 0

    if transport:
        thigh = max(transport)
    else:
        thigh = 0

    if thigh > fhigh:
        print(f"The Highest expense is in Transport which is {thigh}")

    elif fhigh > thigh:
        print(f"The Highest expense is in Food which is {fhigh}")

    else:
        print("Both have the same highest expense:", fhigh)
    
def catspend():
    totalfood = sum(food)
    totaltransport = sum(transport)

    print(f"Food Expense : {totalfood}")
    print(f"Transport Expense : {totaltransport}")


while True:
    print("""====== EXPENSE TRACKER ======

1. Add expense
2. Show expenses
3. Total spending
4. Highest expense
5. Category spending
6. Exit""")

    choice = int(input("Enter your choice -"))

    if choice == 1:
        add()
        print("Added the Expense..")

    elif choice == 2 :
        show()

    elif choice == 3:
        total()

    elif choice == 4:
        highest()

    elif choice == 5:
        catspend()

    elif choice == 6:
        break

print(food)


