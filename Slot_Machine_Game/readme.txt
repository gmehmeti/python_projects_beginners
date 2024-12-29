Slot Machine Game
The Slot Machine Game is a fun and simple project that simulates a classic slot
machine. The player starts with a balance, places bets, and spins the reels. If the
symbols on the reels match, the player wins a payout based on their bet. The
game continues until the player either runs out of money or decides to walk away
with their winnings.

Payout Rules:
• If all three symbols match, the player wins 10 times their bet.
• If two out of three symbols match, the player wins 2 times their bet.
• If none of the symbols match, the player loses their bet.

Optional Enhancements
• Introduce new payout combinations, such as matching two specific symbols,
for more chances to win.

Instructions:

# Ask the user for the starting balance
# Validate the balance
#   Positive nummber (a, 0 and -1 not allowed)
# Loop (while balance > 0)
#   Print the current balance
#    Ask the user to bet
#    Validate the bet
#        Greater than 0
#        Less then the balance
#    Spin the reels
#        Generate three random symbols
#    Display the reels
#    Calculate the payout
#        If three symbols match, payout = bet x 10
#        If two symbols match, payout = bet x 2
#        Else, payout = 0
#   Recalculate the balance
#        balance += payout - bet
#    If balance <= 0
#        Print message
#        Break
#    Else
#        Ask the user if they want to continue playing?
#        If not
#            Break