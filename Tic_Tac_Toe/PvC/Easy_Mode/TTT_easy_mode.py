# Global Variables
BOARD = {key: value for key, value in zip(range(1, 10), map(lambda num: str(num), range(1, 10)))}
PLAYERS = {"Current Player": "X", "Next Player": "O"}


def main():   
    moves = [] # To store moves taken on the board
    while True: # Main game loop
        print() # Create new line for better readability
        display_board() # Display board on screen:
        print(f'Player {PLAYERS["Current Player"]}') # Show current player
        
        # Get move from current player
        move = get_move()
        moves.append(move) # Keep track of positions taken on the board

        # Check if game is over
        if get_winner(): # Check for a winner
            display_board()
            print(f'{PLAYERS["Current Player"]} Wins!')
            break
        elif len(BOARD) == len(moves): # Check for a tie
            display_board()
            print("It's a Tie!")
            break
        # Switch to next player
        switch_players()
    print("Thanks for playing!")


def display_board():
    """Create a new board with numbers from 1-9"""
    print(
        f"""
{BOARD[1]}|{BOARD[2]}|{BOARD[3]}
-+-+-
{BOARD[4]}|{BOARD[5]}|{BOARD[6]}
-+-+-
{BOARD[7]}|{BOARD[8]}|{BOARD[9]}
          """
    )


def get_move():
    """Returns move taken by current player"""    
    # Ask player for move continously until they input an available number from 1-9:
    while True:
        try:
            move = int(input("Please pick a number from 1-9: "))
            if BOARD[move] in BOARD.values() : # Check if move is valid
                BOARD[move] = PLAYERS["Current Player"]
            return move            
        except (KeyError, ValueError): # Reprompt if user input is invalid
            print()
            display_board()
            print(f'Player {PLAYERS["Current Player"]} - Unavailable number')


def get_winner():
    """Returns True if winner is on the board"""
    return row_winner() or column_winner() or diagonal_winner()


def row_winner():
    # Check for marks across 3 rows
    
    return (
        (BOARD[1] == BOARD[2] == BOARD[4])
        or (BOARD[4] == BOARD[5] == BOARD[6])
        or (BOARD[7] == BOARD[8] == BOARD[9])
    )


def column_winner():
    # Check for marks across 3 columns
    return (
        (BOARD[1] == BOARD[4] == BOARD[7])
        or (BOARD[2] == BOARD[5] == BOARD[8])
        or (BOARD[3] == BOARD[6] == BOARD[9])
    )


def diagonal_winner():
    # Check for marks across 2 diagonals
    return (BOARD[1] == BOARD[5] == BOARD[9]) or (BOARD[3] == BOARD[5] == BOARD[7])


def switch_players():
    """Switches player after each turn and returns the current player"""    
    # Switch the players positions in the PLAYERS data structure
    player = PLAYERS["Current Player"]
    PLAYERS["Current Player"] = PLAYERS["Next Player"]
    PLAYERS["Next Player"] = player
    return PLAYERS["Current Player"]

if __name__ == "__main__":
    main()