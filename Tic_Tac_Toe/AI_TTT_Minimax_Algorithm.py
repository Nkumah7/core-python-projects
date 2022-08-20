import random


HUMAN_PLAYER = "X"
AI_PLAYER = "O"
BOARD = {
    key: value
    for key, value in zip(range(1, 10), map(lambda num: str(num), range(1, 10)))
}


def main():
    while not game_over():
        ai_move()
        if check_winner(AI_PLAYER):
            print_board(BOARD)
            print(f"{AI_PLAYER} wins!")
            break
        elif check_draw():
            print_board(BOARD)
            print("Tie!")
            break

        human_move()
        if check_winner(HUMAN_PLAYER):
            print_board(BOARD)
            print(f"{HUMAN_PLAYER} wins!")
            break
        elif check_draw():
            print_board(BOARD)
            print("Tie!")
            break


def print_board(board):
    """Create a new board with numbers from 1-9"""
    print(
        f"""
{board[1]}|{board[2]}|{board[3]}
-+-+-
{board[4]}|{board[5]}|{board[6]}
-+-+-
{board[7]}|{board[8]}|{board[9]}
"""
    )


def human_move():
    """Returns empty spots after human has played"""
    # Ask player for move continously until they input an available number from 1-9:
    print_board(BOARD)
    while True:
        try:
            spot = int(input(f"Please pick a number from {available_spots()}: "))
            if take_spot(HUMAN_PLAYER, spot):
                return
            else:
                raise ValueError
        except (KeyError, ValueError):  # Reprompt if user input is invalid
            print_board(BOARD)
            print(f"Player {HUMAN_PLAYER} - Unavailable number")


def check_winner(player):
    # Check along rows
    if (
        (BOARD[1] == BOARD[2] == BOARD[3] == player)
        or (BOARD[4] == BOARD[5] == BOARD[6] == player)
        or (BOARD[7] == BOARD[8] == BOARD[9] == player)
    ):
        return True

    # Check along columns
    if (
        (BOARD[1] == BOARD[4] == BOARD[7] == player)
        or (BOARD[2] == BOARD[5] == BOARD[8] == player)
        or (BOARD[3] == BOARD[6] == BOARD[9] == player)
    ):
        return True

    # Check along diagonals
    if (BOARD[1] == BOARD[5] == BOARD[9] == player) or (
        BOARD[3] == BOARD[5] == BOARD[7] == player
    ):
        return True


def check_draw():
    for spot in BOARD.keys():
        if BOARD[spot] != "X" and BOARD[spot] != "O":
            return False
    return True


def game_over():
    return check_winner(HUMAN_PLAYER) or check_winner(AI_PLAYER) or check_draw()


def evaluate_board():
    if check_winner(AI_PLAYER):
        return 1
    elif check_winner(HUMAN_PLAYER):
        return -1
    elif check_draw():
        return 0


def take_spot(player, spot):
    if BOARD[spot] not in "XO":  # Check if move is valid
        BOARD[spot] = player
        return True
    return False


def ai_move():
    best_score = -float("Inf")
    best_spot = 0

    board_spots = list(BOARD.keys())
    random.shuffle(board_spots)
    for spot in board_spots:
        if BOARD[spot] not in "XO":
            BOARD[spot] = AI_PLAYER
            score = minimax(BOARD, False)
            BOARD[spot] = str(spot)
            if score > best_score:
                best_score = score
                best_spot = spot
    take_spot(AI_PLAYER, best_spot)
    return


def minimax(board, is_maximizing):
    if game_over():
        return evaluate_board()

    if is_maximizing:
        best_score = -float("Inf")
        for spot in board.keys():
            if board[spot] not in "XO":
                board[spot] = AI_PLAYER
                score = minimax(board, False)
                board[spot] = str(spot)
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = float("Inf")
        for spot in board.keys():
            if board[spot] not in "XO":
                board[spot] = HUMAN_PLAYER
                score = minimax(board, True)
                board[spot] = str(spot)
                if score < best_score:
                    best_score = score
        return best_score


def available_spots():
    return [spot for spot in BOARD.keys() if BOARD[spot] not in "XO"]


if __name__ == "__main__":
    main()
