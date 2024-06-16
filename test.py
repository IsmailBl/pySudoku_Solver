import numpy as np
import random as rnd
def grid_gen():
    x = rnd.randint(0, 9)
    print (x)
    grid = np.array(([1,9,0,7,0,5,0,0,0],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,0],[6,5,0,0,0,1,4,0,0],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7],[6,5,0,0,0,1,4,0,7] ))
    shape = grid.shape
    print(f'Shape is : {shape}') 
    return (grid)


grid_gen(
    
)