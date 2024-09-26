Pig Dice Game
The Pig Dice Game is a fun, strategic game where two players compete to be the
first to reach 100 points. In this project, you’ll build a simplified version of the
game where each player rolls a die repeatedly to accumulate points. However, if
they roll a 1, they lose all points accumulated in that turn and must pass the die to
the other player. The game requires players to decide whether to keep rolling to
increase their score or to hold and secure their points before risking a roll of 1.

Optional Enhancements
• Allow players to set a custom target score before starting the game.
• Modify the program to support more than two players, with each player taking
turns to roll the dice and accumulate points.
• Implement a feature that tracks the total score of each player over multiple
rounds or games, allowing for a cumulative competition.
• Introduce a rule where rolling two 6s consecutively resets the player’s score
to 0, adding an extra layer of strategy.

Instructions:

# Run the game until a player wins
# Player 1 takes a trun
#   Roll a die
#   If roll == 1
#       Turn points = 0
#       Turn ends
#   Else
#       Add roll to the turn points
#       Ask the user if they want to roll again?
#       If yes, repeat
#       Else, turn ends and we return turn points
#
# Update player 1's points
# Print statistics
# Check if player 1 wins (total points >= 100)
# If yes, terminate the game
# Otherwise we swap players