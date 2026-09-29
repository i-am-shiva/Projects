# 🎮 Level 1 — Warm-up, but not boring
# 1. 🕵️ The Secret Password

# Create a program that asks the user for a password.

# Rules:

# Password must be at least 8 characters.
# Must contain at least one digit.
# Must contain at least one uppercase letter.
# Must contain at least one lowercase letter.
# If all conditions are satisfied → "Password accepted"
# Otherwise tell the user exactly what is missing.

# Example:

# Enter password: hello123

# ❌ Password rejected
# Missing: uppercase letter

# Hint: Strings + loops + conditions.

password = input("Enter the Password:")
length = len(password)
missing = []
if length < 8:
    missing.append("Password must be at least 8 characters.")

if not any(char.isupper() for char in password):
    missing.append("No Uppercase letter")
if not any(char.islower() for char in password):
    missing.append("No Lowercase letter")
if not any(char.isdigit() for char in password):
    missing.append("No  Atleast One Digit")

if not missing :
    print("Password Accepted ✅")   
else:
    print("""❌ Password rejected
Missing:""")
    for i in missing:
        print(f"-{i}")