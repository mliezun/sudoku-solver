# sudoku-solver
Python Sudoku Solver

![Python application](https://github.com/mliezun/sudoku-solver/workflows/Python%20application/badge.svg)

## How to use

```python
import solver

# Zeroes represent empty cells
board = solver.Board([
    [1, 0, 6, 0, 0, 2, 3, 0, 0],
    [0, 5, 0, 0, 0, 6, 0, 9, 1],
    [0, 0, 9, 5, 0, 1, 4, 6, 2],
    [0, 3, 7, 9, 0, 5, 0, 0, 0],
    [5, 8, 1, 0, 2, 7, 9, 0, 0],
    [0, 0, 0, 4, 0, 8, 1, 5, 7],
    [0, 0, 0, 2, 6, 0, 5, 4, 0],
    [0, 0, 4, 1, 5, 0, 6, 0, 9],
    [9, 0, 0, 8, 7, 4, 2, 1, 0],
])

solved_board = solver.SudokuSolver.solve(board)
```
