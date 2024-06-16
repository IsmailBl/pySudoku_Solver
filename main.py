from __future__ import barry_as_FLUFL
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
"""This project is a 9x9G Grid Sdoku solving program based on a backtracking
algorithm. 
"""
__version__ = '0.1'
__author__ = 'Ismail B.'

my_grid = np.array([[1,2,3],
                    [1,2,3]])

class gridSolver ():
    def __init__ (self, grid) -> None : 
        self.grid = grid
        self.size =[]
    def grid_size (self):
        m , n = np.shape(self.grid)
        self.size.append(m)
        self.size.append(n)
        return self.size 
    
    def check_solv(self, grid):
        pass     
if __name__ == "__main__":
    grid_slv = gridSolver(my_grid)
    print (grid_slv.grid_size())