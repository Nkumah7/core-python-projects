import numpy as np

# Board taken from Sudoku.com -> https://sudoku.com/evil/
BOARD = [
    [1, " ", " ", " ", " ", " ", 6, " ", " "],
    [" ", 8, " ", " ", 9, 7, " ", " ", 3],
    [" ", " ", " ", 4, " ", " ", " ", " ", " "],
    [" ", 7, " ", " ", 2, 3, " ", " ", 9],
    [" ", " ", " ", " ", " ", 5, " ", " ", " "],
    [" ", " ", 8, " ", " ", " ", " ", 7, " "],
    [" ", 2, " ", 5, " ", " ", " ", " ", " "],
    [" ", " ", " ", 8, " ", " ", " ", " ", 4],
    [" ", " ", 6, " ", 4, 2, 3, " ", " "]
]


def get_empty_space(board, row, column, num):
    """
    *   Function to check for empty space in the board
        -   Returns False if all spaces are filled vertically, horizontally and in each square.
        -   Returns True if empty space is found. 
    """
    
    # Check if there is empty space along the row
    for i in range(len(board)):
        if board[row][i] == num:
            return False

    # Check if there is empty space along the column
    for i in range(len(board)):
        if board[i][column] == num:
            return False
        
    # Check if there is empty space in the square
    square_y = (row // 3) * 3
    square_x = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[square_y+i][square_x+j] == num:
                return False
    return True
print(np.matrix(BOARD), "\n")
     
     
def sudoku_solver(board):
    """
    *   Function to solve the Sudoku board and print the result
        -   Backtracking algorithm is implemented to solve Sudoku board
        -   The function to invoked recursively to solve the number to be inserted in each empty space of the board       
    """
    
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == " ":
                for num in range(1, 10):
                    if get_empty_space(board, row, column, num):
                        board[row][column] = num
                        sudoku_solver(board)
                        board[row][column] = " "
                return 
            
    print(np.matrix(board))


if __name__ == "__main__":
    print("Solved Sudoku Board")
    print("--------------------")
    sudoku_solver(BOARD)