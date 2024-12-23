Word Guessing Game
The Word Guessing Game is a fun and interactive project where players try to
guess a secret word, one letter at a time. The word is selected randomly from a list
of words stored in a text file. The player has six attempts to guess the word, with
each incorrect guess reducing the remaining attempts. Correctly guessed letters
are revealed in their respective positions, while incorrect guesses prompt the
player to try again.

Optional Enhancements
• Implement a hint feature that the player can use once or twice per game to
reveal a letter in the word. This can make the game a bit easier and more fun.
• Offer different difficulty levels that change the length of the words to be
guessed. Longer words could be for more advanced players, while shorter
words could be for beginners.
• Keep a record of how many games the player has won or lost during their
session. Display this information at the end of each game.

Instructions:

# Read the list of words from a file (words.txt)
# Choose a random word
# attemps = 6
# Loop attempts > 0
#   Display word
#       For each letter in secret word
#           If user guessed that letter
#                print it
#            Else
#                print _
#   Ask the user to enter a letter
#   Validate user input
#       Single character
#       Only a - z
#       Not a duplicate
#   If a letter is in the secret word      
#       print good guess
#       Check if letter is guessed
#            print congratulation
#            break
#   Else
#       Print wrong guess
#       Decrement attempts
