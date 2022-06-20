import os

PLAYER1 = "X"  # 1          0 1 2
PLAYER2 = "O"  # -1         3 4 5
#                           6 7 8
"""def print_board(table):
    final_print = ""
    for i in range(len(table)):
        player_print_value = " "
        if table[i] == 1:
            player_print_value = PLAYER1
        elif table[i] == -1:
            player_print_value = PLAYER2
        elif i < 6:
            player_print_value = "_"
        if (i+1) % 3 == 0:
            final_print = final_print + player_print_value + "\n"
        else:
            final_print = final_print + player_print_value + "|"
    print(final_print)
"""


def print_board(table):
    board = []
    for i in range(9):
        if table[i] > 0:
            board.append(PLAYER1)
        elif table[i] < 0:
            board.append(PLAYER2)
        elif table[i] == 0:
            if i > 5:
                board.append(" ")
            else:
                board.append("_")
    print(f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}")


"""def check_if_win_v(board, player):
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    return False

def check_if_win_v(board, player):
    added = 0
    for i in range(3):
        for j in range(0, 9, 3):
            added = added + board[i+j]
            if added == player*3:
                return True
    return False
def check_if_win_h(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    return False
def check_if_win_h(board, player):
    added = 0
    for j in range(0, 9, 3):
        for i in range(3):
            added = added + board[i+j]
            if added == player*3:
                return True
    return False

def check_if_win_d(board, player):
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False
def check_if_win_d(board, player):
    added = 0
    for i in range(0, 3, 4):
        added = added + board[i]
        if added == player * 3:
            return True
    added = 0
    for j in range(2, 4, 2):
        added = added + board[j]
        if added == player*3:
            return True
    return False
def win_condition(board, player):
    if check_if_win_v(board, player) or check_if_win_d(board, player) or check_if_win_h(board, player):
        return True
    return False"""


def win_condition(board, player):
    # Diagonal
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    # Horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Vertical
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    return False


def make_move(board, player):
    if player > 0:
        player_display = PLAYER1
    else:
        player_display = PLAYER2
    try:
        position = int(input(f"{player_display} make a move [1-9]: "))
        if 0 < position <= 9:
            if board[position - 1] == 0:  # if cell is free
                board[position - 1] = player
                return True
            else:
                print("This spot is not available! Try again")
                return make_move(board, player)
        else:
            print("This spot is outside the board! Try again")
            return make_move(board, player)
    except ValueError:
        print("Input not a number! Try again")
        return make_move(board, player)


def play_game():
    board = [0] * 9
    print_board(board)
    player = 1
    for i in range(9):
        make_move(board, player)
        os.system('cls')
        print_board(board)
        if win_condition(board, player):
            if player > 0:
                print(f"{PLAYER1} won!")
            else:
                print(f"{PLAYER2} won!")
            break
        else:
            if i >= 8:
                print("It's a Draw!")
                break
        player = player * -1
    return True


def main():
    while True:
        os.system('cls')
        play_game()
        answer = input("Replay? y/n")
        if answer.lower() == "y":
            continue
        elif answer.lower() == "n":
            print("Thanks for Playing")
            break
    """board = [0]*9
    print_board(board)
    player = 1
    for i in range(9):
        make_move(board, player)
        print_board(board)
        if win_condition(board, player):
            if player > 0:
                print(f"{PLAYER1} won!")
            else:
                print(f"{PLAYER2} won!")
            break
        else:
            if i >= 8:
                print("It's a Draw!")
                break
        player = player * -1"""


if __name__ == '__main__':
    main()
