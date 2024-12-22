
# Cows and Bulls Game
import random as rn


def generate_secret_key():
    digits = [str(n) for n in range(0, 10)]
    rn.shuffle(digits)
    secret_key = "".join(digits[:4])
    return secret_key


def validate_secret_key(key: str):
    if len(key) == 4 and key.isdigit() and len(set(key)) == 4:
        return True
    return False


def calculate_cows_and_bulls(key, guess):
    cows = 0
    bulls = 0

    for n in range(4):
        if guess[n] == key[n]:
            bulls += 1
        elif guess[n] in key:
            cows += 1

    return cows, bulls


def main():

    secret_key = generate_secret_key()
    while True:
        guess = input(
            "Enter a 4-digits number with unique digits or 'q' for quit: ")
        if guess.lower() == 'q':
            break

        is_valid = validate_secret_key(guess)
        if is_valid:
            cows, bulls = calculate_cows_and_bulls(secret_key, guess)
            print(f"cows: {cows}, bulls: {bulls}")

            if bulls == 4:
                print("Congratulations! You guessed the correct number!")

        else:
            print(
                "Invalid guess number.\nPlease enter a 4-digits number with unique digits!")
            continue


if __name__ == "__main__":
    main()
