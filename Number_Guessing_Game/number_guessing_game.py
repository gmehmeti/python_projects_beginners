
# Number Guessing Game
import random as rn

secret_number = rn.randint(1, 100)

while True:
    guessNumber = input("Guess the nummber between 1 and 100: ")

    if guessNumber.isdigit() == False:
        print("Please enter a valid number")
        continue

    guessNumber = int(guessNumber)
    if guessNumber == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guessNumber > secret_number:
        print("Too hight!")
    elif guessNumber < secret_number:
        print("Too low!")

