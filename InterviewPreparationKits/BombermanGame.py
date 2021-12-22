#!/bin/python3

import os
import sys

def flip(g):
    matrix = g.copy()
    m = len(matrix)
    n = len(matrix[0])
    fgrid = []
    for i in range(m):
        value = ''
        for j in range(n):
            if matrix[i][j] == 'O' or matrix[i][j] == '*' or (i-1 >=0 and matrix[i-1][j] == 'O') or (i+1 < m and matrix[i+1][j] == 'O') or (j-1 >=0 and matrix[i][j-1] == 'O') or (j+1 < n and matrix[i][j+1] == 'O'):
                value += '*'
            else:
                value += '.'
        fgrid.append(value)
    ugrid = []
    for i in range(m):
        value = ''
        for j in range(n):
            value += '.' if fgrid[i][j] == '*' else 'O'
        ugrid.append(value)
    return ugrid
def plant_all(g):
    grid = g.copy()
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        grid[i] = 'O'*n
    return grid


def bomberMan(n, grid):
    if (n==1) : return grid
    if (n-1) % 4 == 0: return flip(flip(grid))
    if n % 2 == 0 : return plant_all(grid)    
    return flip(grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
