#!/bin/python3

import os
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    itera = 0
    iterb = 0
    iterc = 0    
    result = 0
    
    while iterb < len(b):
        while itera < len(a) and a[itera] <= b[iterb]:
            itera += 1
        
        while iterc < len(c) and c[iterc] <= b[iterb]:
            iterc += 1
        
        result += itera * iterc
        iterb += 1
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
