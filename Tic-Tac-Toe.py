def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
        col = int(input(f"Player {players[current_player]}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)

            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            elif check_tie(board):
                print("It's a tie!")
                break

            current_player = (current_player + 1) % 2
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
