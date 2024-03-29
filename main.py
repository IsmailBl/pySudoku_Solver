from __future__ import barry_as_FLUFL
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
"""This project is a 9x9G Grid Sdoku solving program based on a backtracking
algorithm. 
"""
__version__ = '0.1'
__author__ = 'Ismail B.'

def grid_gen():
    x = rnd.randint(0, 9)
    print (x)
    grid = np.array(([1,9,0,7,0,5,0,0,0],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,0],[6,5,0,0,0,1,4,0,0],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7] ))
    shape = grid.shape
    print(f"Shape is : {shape}") 
    return (grid)
def check_grid(grid):
    shape = grid.shape
    i = shape [0]
    j = shape [1]
    zeros = 0 
    for x in range(i):
        for y in range(j): 
            if grid [x][y] == 0: 
                zeros = zeros +1
    return (print (f'Number of zeros is : {zeros}'))

def is_valid(grid, num,  row= 9 , col=9):
    x = 0 
    for i in range (row):
        for j in range (col):
            if grid[i][j] == num :
                x += 1
            if x > 1 : 
                print ('Grid is unsolveable !')
                break 
if __name__ == '__main__':
    grid =grid_gen()
    check_grid(grid)
    print(grid)
    is_valid (grid, 7)