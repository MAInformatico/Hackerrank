#!/bin/python3

import math
import os
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    PossibleSquares = [   [ [8,1,6],[3,5,7],[4,9,2] ],
            [ [6,1,8],[7,5,3],[2,9,4] ],
            [ [4,9,2],[3,5,7],[8,1,6] ],
            [ [2,9,4],[7,5,3],[6,1,8] ],
            [ [8,3,4],[1,5,9],[6,7,2] ],
            [ [4,3,8],[9,5,1],[2,7,6] ],
            [ [6,7,2],[1,5,9],[8,3,4] ],
            [ [2,7,6],[9,5,1],[4,3,8] ]
        ]
    
    result = 99999999
    for i in range(len(PossibleSquares)):
        currentCost = 0
        for j in range(len(PossibleSquares[i])):
            for k in range(len(PossibleSquares[i][j])):
                currentCost += abs(PossibleSquares[i][j][k] - s[j][k])
        result = min(result, currentCost)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
