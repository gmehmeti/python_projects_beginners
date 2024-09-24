
# Tic Tac Toe Game

from termcolor import cprint, colored

PLAYER_X = "X"
PLAYER_O = "O"

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def get_colored_cell(value):
    if value == PLAYER_X:
        return colored(value, 'green')

    return colored(value, 'red')


def display_board():
    line = "---+---+---"
    print(line)
    for row in board:
        print(f" {get_colored_cell(row[0])} | {
              get_colored_cell(row[1])} | {get_colored_cell(row[2])}")
        print(line)


def check_winner():
    # Check winner in rows
    for row in board:
        if row[0] == row[1] == row[2] == PLAYER_X:
            return True
        elif row[0] == row[1] == row[2] == PLAYER_O:
            return True

    # Check winner in columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_X:
            return True
        elif board[0][col] == board[1][col] == board[2][col] == PLAYER_O:
            return True

    # Check winner in diagonals
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == PLAYER_O:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == PLAYER_X:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == PLAYER_O:
        return True

    return False


def is_full():
    # Check if board is full
    for row in board:
        if ' ' in row:
            return False

    return True


def get_user_input(caption):
    while True:
        try:
            user_value = row = int(input(f"Enter {caption} (0-2): "))
            if user_value < 0 or user_value > 2:
                raise ValueError()

            return user_value
        except ValueError:
            print(f"User input is not valid!")


def get_user_move(current_player):
    print(f'Player {current_player}\'s turn')
    while True:
        row = get_user_input("row")
        column = get_user_input("column")

        cell = board[row][column].strip()
        if cell != '':
            print('This spot is already taken!')
            continue
        else:
            board[row][column] = current_player
            break


def main():
    current_player = PLAYER_X
    display_board()

    while True:

        get_user_move(current_player)

        display_board()

        if check_winner():
            print(f'Player {current_player} wins!')
            break

        if is_full():
            print(f"The board is full!")
            break

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        print()


# Run main program
main()
