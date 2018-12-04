#!/usr/bin/python
import math
def displayPathtoPrincess(n,grid):
    p_loc = [0,0]
    
    if grid[0][0] == 'p':
        p_loc = [0,0]
    elif grid[0][n-1] == 'p':
        p_loc = [0,n-1]
    elif grid[n-1][0] == 'p':
        p_loc = [n-1, 0]
    else:
        p_loc = [n-1,n-1]
    
    b_loc = [int(math.floor(n/2)) , int(math.floor(n/2))]
    
    
    while (b_loc != p_loc):
        if p_loc[0] == 0 and p_loc[1] == 0:
            print("UP")
            print("LEFT")
            b_loc[0] = b_loc[0]-1
            b_loc[1] = b_loc[1]-1
        
        elif p_loc[0] == 0 and p_loc[1] == n-1:
            print("UP")
            print("RIGHT")
            b_loc[0] = b_loc[0]-1
            b_loc[1] = b_loc[1]+1
            
        
        elif p_loc[0] == n-1 and p_loc[1] == 0:
            print("DOWN")
            print("LEFT")
            b_loc[0] = b_loc[0]+1
            b_loc[1] = b_loc[1]-1
        
        elif p_loc[0] == n-1 and p_loc[1] == n-1:
            print("DOWN")
            print("RIGHT")
            b_loc[0] = b_loc[0]+1
            b_loc[1] = b_loc[1]+1
            
    
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)