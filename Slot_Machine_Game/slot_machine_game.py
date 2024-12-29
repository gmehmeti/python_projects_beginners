# Slot Machine Game
import random as rn
from collections import Counter


def validate_starting_balance(balance: str):
    if not balance.isdigit():
        raise ValueError("Balance should be only numbers!")

    balance = int(balance)
    if balance <= 0:
        raise ValueError("Balance should be greater than zero!")

    return balance


def get_bet_amount(balance):
    while True:
        try:
            bet = input("Enter your bet: ")
            if not bet.isdigit():
                raise ValueError("Bet should be only numbers!")

            bet = int(bet)
            if bet <= 0:
                raise ValueError("Bet should be greater than zero!")

            if bet > balance:
                raise ValueError("Bet must be less than balance!")

            return bet
        except ValueError as e:
            print(e)


def get_starting_balance():
    while True:
        try:
            starting_balance = input("Enter your starting balance: ")
            starting_balance = validate_starting_balance(starting_balance)
            return starting_balance
        except ValueError as e:
            print(e)


def get_spin_reels():
    symbols = ['🍒', '🍋', '🔔', '⭐', '🍉']
    result = []
    # for _ in range(3):
    #     result.append(rn.choice(symbols))

    # result = [rn.choice(symbols) for _ in range(3)]

    result.extend(rn.choices(symbols, k=3))
    return result


def calculate_payout(reels, bet_amount):
    # match = len(set(reels))

    if reels[0] == reels[1] == reels[2]:
        return bet_amount * 10
    elif reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet_amount * 5
    return 0


def main():
    balance = get_starting_balance()
    print("Welcome to the Slot Machine Game!")
    print(f"You stard with balance of :{balance}\n")

    while balance > 0:
        print(f"Your current balance: {balance}")
        bet = get_bet_amount(balance)
        spin_reels = get_spin_reels()
        print(" | ".join(spin_reels))

        payout = calculate_payout(spin_reels, bet)
        if payout > 0:
            print(f"You won {payout}!")
        else:
            print(f"You lost!")

        balance += payout - bet
        if balance <= 0:
            print("You are out of money. Game Over!")
            break

        play_continue = input("Do you want to play again (Y/N)? ").lower()
        if (play_continue != "y"):
            print(f"You walk away with {balance}")
            break


if __name__ == "__main__":
    main()
