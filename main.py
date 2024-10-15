"""_Summary : This project is a 9x9 Grid Sudoku solving program based on 
backtracking
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rnd


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


class GridSolver ():
    def __init__(self, grid):
        self.grid = grid
        pass
    
    def grid_size (self):
        return np.size(self.grid)
    
    def is_safe (self, grid, row, col, num):
        for i in range (N):
            if grid [row][i] == num: return False            
        for j in range (N):
            if grid [j][col] == num: return False 
        
        start_row = row + row % 3
        start_col = col + col % 3
        
        for i in range (3):
            for j in range (3): 
                if grid [i + start_row][j+start_col] == num:
                    return False 
        return True
    
    def solve_grid (self, grid, row, col):
        if col == N and row == N-1 : return True
        if col == N :
            row = row + 1 
            col = 0
            
        if grid[row][col]>0:
            return self.solve_grid(grid, row, col+1)
        for num in range (1, N+1, 1):
            if self.is_safe(grid, col, row, num):
                grid [row][col] = num 
                if self.solve_grid(grid, row, col + 1):
                    return True
            else :
                grid [row][col] = 0 
        return False

if __name__ == "__main__":
    try :
        solver = GridSolver(my_grid)
        if solver.solve_grid(my_grid, 0, 0):(print ("Grid Solved"))
    except :
        print(Exception)