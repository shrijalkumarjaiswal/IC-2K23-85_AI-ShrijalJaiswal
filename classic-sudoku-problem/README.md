# Classic Sudoku Solver (9×9) in Python

## 1. Introduction

Sudoku is a popular number-placement puzzle and a common example of a constraint satisfaction problem in Artificial Intelligence (AI).

The objective is to fill a 9×9 grid with numbers from 1 to 9 while following specific rules.

This Python program automatically solves a Sudoku puzzle using the **Backtracking Algorithm**. It checks possible numbers, verifies the constraints, and finds a valid solution.

## 2. Problem Description

A classic Sudoku puzzle consists of:

- **Grid Size:** 9×9
- **Numbers:** 1 to 9
- **Empty Cells:** Represented by 0
- **Subgrids:** Nine smaller 3×3 boxes

The objective is to fill all empty cells while ensuring that no number is repeated in any row, column, or 3×3 box.

## 3. Features

- Solves a classic 9×9 Sudoku puzzle automatically.
- Uses the Backtracking Algorithm.
- Finds empty cells in the puzzle.
- Checks whether a number can be placed.
- Validates row, column, and 3×3 box constraints.
- Reverses an incorrect choice and tries another number.
- Displays the original and solved Sudoku grids.
- Displays a message if no solution exists.

## 4. Sudoku Rules and Constraints

| Constraint | Description |
|---|---|
| Row Constraint | Numbers 1–9 must not repeat in a row. |
| Column Constraint | Numbers 1–9 must not repeat in a column. |
| 3×3 Box Constraint | Numbers 1–9 must not repeat in a 3×3 box. |
| Empty Cell | Represented by 0. |
| Valid Numbers | Only numbers from 1 to 9 can be placed. |

## 5. Technologies Used

- **Programming Language:** Python
- **Algorithm:** Backtracking
- **Concepts:** Functions, Lists, Loops, Conditional Statements, Recursion, and Constraint Checking.

## 6. How to Run the Program

1. Install Python on your computer.
2. Save the program in a file named `sudoku_solver.py`.
3. Open the terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the following command:

```bash
python sudoku_solver.py
```

6. The program displays the original Sudoku puzzle.
7. It automatically solves the puzzle and displays the completed grid.

## 7. Algorithm Explanation

The program uses the Backtracking Algorithm to solve Sudoku.

The basic steps are:

1. Find an empty cell in the Sudoku grid.
2. Try placing a number from 1 to 9.
3. Check whether the number follows all Sudoku rules.
4. If valid, place the number in the cell.
5. Recursively solve the remaining empty cells.
6. If the number leads to an incorrect solution, reset the cell to 0.
7. Try another number.
8. Continue until the puzzle is solved or no solution exists.

## 8. Important Functions

| Function | Purpose |
|---|---|
| `print_board()` | Displays the Sudoku grid. |
| `find_empty()` | Finds the next empty cell. |
| `is_valid()` | Checks whether a number follows Sudoku rules. |
| `solve()` | Solves the puzzle using backtracking. |

## 9. Learning Outcomes

By implementing this program, we understand:

- The concept of Constraint Satisfaction Problems (CSP) in AI.
- How the Backtracking Algorithm works.
- How recursion can be used to solve problems.
- How to check and apply constraints.
- How to explore possible solutions systematically.
- How to reverse an incorrect decision and try another option.

## 10. Conclusion

The Classic Sudoku Solver demonstrates an important Artificial Intelligence problem-solving technique called Backtracking.

The program systematically tries possible numbers, checks constraints, and reverses incorrect choices until it finds a valid solution.

It provides a practical understanding of recursion, constraint satisfaction, and search techniques in Artificial Intelligence.