# Word Guessing Game
import random as rn


def get_secret_word():
    with open("./Word_Guessing_Game/words.txt", mode="r") as file:
        words = file.readlines()
        word = rn.choice(words).strip()
        # print(word)
        return word


def validate_input(guess_letter, show_word, secret_word):

    try:
        if len(guess_letter) != 1:
            raise ValueError("Enter only one letter!")

        if not guess_letter.isalpha():
            raise ValueError("Enter only letters from a to z!")

        if guess_letter in show_word:
            raise ValueError("You already guessed this letter!")

        guess_count = secret_word.count(guess_letter)
        if guess_count == 0:
            raise ValueError("Wrong guess!")

        return True
    except Exception as e:
        print(e)
        return False


def main():
    secret_word = get_secret_word()
    show_word = ["_" for x in range(len(secret_word))]
    # for _ in range(len(secret_word)):
    #     show_word.append("_")

    print("".join(show_word))

    attempts = 6
    while attempts > 0:
        guess_letter = input(f"Enter a letter ({attempts}): ").lower()

        is_valid = validate_input(guess_letter, show_word, secret_word)
        if is_valid:
            for i in range(len(secret_word)):
                if secret_word[i] == guess_letter:
                    show_word[i] = guess_letter
            print("Good guess!")
        else:
            attempts -= 1

        print("".join(show_word))
        if "_" not in show_word:
            print("Congratulation! You guessed the word!")
            break

        if (attempts == 0):
            print("Game over! No more attempts!")


if __name__ == "__main__":
    main()
