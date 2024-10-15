"""
Summary: This project is a 9x9 Grid Sudoku solving program based on backtracking.
"""

import numpy as np

__version__ = "0.1"
__author__ = "Ismail B."

N = 9
my_grid = np.array(
    [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]
)


class GridSolver:
    def __init__(self, grid):
        self.grid = grid

    def grid_size(self):
        return np.size(self.grid)

    def is_safe(self, grid, row, col, num):
        # Check if 'num' is not in the given row and column
        if num in grid[row] or num in grid[:, col]:
            return False

        # Check if 'num' is not in the 3x3 subgrid
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_grid(self, grid, row=0, col=0):
        # If we've reached the end of the grid, the puzzle is solved
        if row == N - 1 and col == N:
            return True
        if col == N:
            row += 1
            col = 0

        # Skip already filled cells
        if grid[row][col] > 0:
            return self.solve_grid(grid, row, col + 1)

        for num in range(1, N + 1):
            if self.is_safe(grid, row, col, num):
                grid[row][col] = num
                if self.solve_grid(grid, row, col + 1):
                    return True

            # Reset cell if the number is not valid
            grid[row][col] = 0

        return False


if __name__ == "__main__":
    try:
        solver = GridSolver(my_grid)
        if solver.solve_grid(my_grid):
            print("Grid Solved:")
            print(my_grid)
        else:
            print("No solution exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
