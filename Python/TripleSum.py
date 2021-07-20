#!/bin/python3
import os
import random
import sys
from bisect import bisect #bisection algorithm, remember Numeric Calculus course at University

# Complete the triplets function below.
def triplets(a, b, c):
    a, b, c = sorted(set(a)), set(b), sorted(set(c))
    return sum((bisect(a, i) * bisect(c, i) for i in b))

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
