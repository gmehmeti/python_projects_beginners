# Password Strength Checker
import re


def check_password_strength(password: str):
    strength = 0
    match = False

    if len(password) >= 8:
        strength = 1
        # print(f"Length {strength}")

    # letters a to z lowecase
    match = re.search("[a-z]", password)
    if match:
        strength = strength + 1
        # print(f"letters a to z lowecase {strength}")

    # letters a to z uppercase
    match = re.search("[A-Z]", password)
    if match:
        strength = strength + 1
        # print(f"letters a to z uppercase {strength}")

    # numbers 0 to 9
    match = re.search("[0-9]", password)
    if match:
        strength = strength + 1
        # print(f"numbers 0 to 9 {strength}")

    # special characters
    match = re.search("[@#$%+=!]", password)
    if match:
        strength = strength + 1
        # print(f"special characters {strength}")

    return strength


def main():
    password = input("Type your password: ")
    strength = check_password_strength(password)
    message = ""

    if strength == 1:
        message = "Very Weak"
    elif strength == 2:
        message = "Weak"
    elif strength == 3:
        message = "Medium"
    elif strength == 4:
        message = "Strong"
    elif strength == 5:
        message = "Very Strong"

    print(f"Password strength: {message}!")


if __name__ == "__main__":
    main()
