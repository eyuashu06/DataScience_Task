# Welcome to your Python project!
# Simple Tic-Tac-Toe CLI
board = [str(i) for i in range(1, 10)]

def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_cond)

current_player = "X"
for _ in range(9):
    display_board()
    move = int(input(f"Player {current_player}, choose (1-9): ")) - 1
    if board[move] not in ["X", "O"]:
        board[move] = current_player
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Spot taken, try again.")
else:
    display_board()
    print("It's a draw!")