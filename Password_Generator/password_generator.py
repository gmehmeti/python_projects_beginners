# Generate Password

# Enter password length:
# Include uppercase letters (Y/N):
# Include numbers (Y/N):
# Include special characters (Y/N):
import string
import random as rn


def generate_password(psw_length, uppercase_letters, has_numbers, special_characters):
    if psw_length < (uppercase_letters + has_numbers + special_characters):
        raise ValueError(
            'Password length is too short for the specified criteria.')

    password = ""

    if uppercase_letters:
        password += rn.choice(string.ascii_uppercase)

    if has_numbers:
        password += rn.choice(string.digits)

    if special_characters:
        password += rn.choice(string.punctuation)

    for _ in range(psw_length-len(password)):
        password += rn.choice(string.ascii_lowercase)

    password_list = list(password)
    rn.shuffle(password_list)
    password = "".join(password_list)
    return password


def main():
    psw_length = int(input("Enter password length: "))
    uppercase_letters = input(
        "Include uppercase letters (Y/N): ").lower() == "y"
    has_numbers = input("Include numbers (Y/N): ").lower() == "y"
    special_characters = input(
        "Include special characters (Y/N) ").lower() == "y"

    try:
        password = generate_password(
            psw_length, uppercase_letters, has_numbers, special_characters)
        print(f"Password: {password}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
