def print_board(board):
    for row in board:
        print(" ".join(row))

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def is_game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_full(board)

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while not is_game_over(board):
        print_board(board)

        if current_player == 'X':
            row, col = map(int, input("Enter your move (row and column separated by space): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            move = get_best_move(board)
            board[move[0]][move[1]] = 'O'
            current_player = 'X'

    print_board(board)

    if is_winner(board, 'X'):
        print("You win!")
    elif is_winner(board, 'O'):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
