
# Sudoku Solver using Backtracking

# 0 represents an empty cell
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Function to print the Sudoku board
def print_board():
    for row in board:
        print(row)


# Function to find an empty cell
def find_empty():
    for i in range(9):
        for j in range(9):

            # Return the position of an empty cell
            if board[i][j] == 0:
                return i, j

    # Return None if no empty cell is found
    return None


# Function to check whether a number is valid
def is_valid(num, row, col):

    # Check the entire row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the entire column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Find the starting position of the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 box
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    # Number is valid if no duplicate is found
    return True


# Function to solve the Sudoku puzzle
def solve():

    # Find an empty cell
    empty = find_empty()

    # If no empty cell exists, Sudoku is solved
    if empty == None:
        return True

    row, col = empty

    # Try numbers from 1 to 9
    for num in range(1, 10):

        # Check whether the number can be placed
        if is_valid(num, row, col):

            # Place the number in the empty cell
            board[row][col] = num

            # Try solving the remaining puzzle
            if solve():
                return True

            # If solution is not found, remove the number
            board[row][col] = 0

    # No number works, so go back to the previous cell
    return False


# Main program
print("Original Sudoku:")
print_board()

print("\nSolved Sudoku:")

# Call the solving function
if solve():
    print_board()
else:
    print("No solution exists!")
