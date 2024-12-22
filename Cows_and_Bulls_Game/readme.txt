Cows and Bulls Game
The Cows and Bulls Game is a fun number-guessing challenge that tests your
logical thinking and problem-solving skills. In this project, you’ll build a game
where the computer comes up with a secret 4-digit number, and your job is to
guess it. After each guess, you’ll get feedback in the form of "cows" and "bulls"
a "bull" means you’ve guessed the right digit in the right spot, while a "cow"
means the digit is correct but in the wrong spot.

Optional Enhancements
• Allow the player to choose a difficulty level at the start of the game, 
which changes the length of the secret number or the number of attempts allowed.

• Implement a system that offers hints after a certain number of incorrect
guesses, providing more guidance to the player.


Instructions:

# Generate a secret number with unique digits
# Loop
#   Ask the user to make a guess
#   Validate the guess (4 digits - unique)
#   If invalid
#       Print an error
#       Continue
#   Else
#       Calculate cows and bulls
#       For each digit in the guess
#           If digit exists in the same position in the secret
#               Increment bulls
#           If digit exist in the secret
#               Increment cows
#       Print cows and bulls
#       If bulls == 4
#           Print message
#           Break