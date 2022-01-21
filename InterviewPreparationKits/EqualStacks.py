#!/bin/python3

import os
import sys

def equalStacks(h1, h2, h3):
    i, j, k = 0, 0, 0
    
    for it in h1:
        i = i + it
    for it in h2:
        j = j + it
    for it in h3:
        k = k + it
    
    while i != 0 and j != 0 and k != 0 and (i!=j or j!= k) :
        if max(i,j,k) == i:
            i = i - h1[0]
            h1.pop(0)
        elif max(i,j,k) == j:
            j = j - h2[0]
            h2.pop(0)
        else:
            k = k - h3[0]
            h3.pop(0)
    else:
        if i == j and j == k:
            return i
        else:
            return 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
