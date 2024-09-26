# Pig Dice Game

import random as rn


def play_turn(player_name: str):
    score_point = 0
    print(f"\nPlayer {player_name}'s turn")
    while True:
        roll_dice = rn.randint(1, 6)
        print(f"You rolled a {roll_dice}")

        if roll_dice == 1:
            return 0

        score_point += roll_dice

        play_again = input("Roll again? (y/n): ").lower()
        if play_again != "y":
            return score_point


def main():
    scores = {"1": 0, "2": 0}
    current_player = "1"

    while True:
        points = play_turn(current_player)
        scores[current_player] = scores.get(current_player) + points

        print(f"\nYou scored {points} points this turn.")
        print(f"Current scores: Player 1: {
              scores["1"]}, Player 2: {scores["2"]}\n")

        if scores[current_player] >= 100:
            print(f"Player {current_player}'s wins!")
            break
        else:
            current_player = "1" if current_player == "2" else "2"


if __name__ == "__main__":
    main()
