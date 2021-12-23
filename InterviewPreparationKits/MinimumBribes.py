#!/bin/python3

import math
import os
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    result = 0
    swaps = 1
    for i, value in enumerate(q):
        if value > i + 3:
            print("Too chaotic")
            return

    while (swaps != 0):
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                swaps += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                result += 1
    print(result)

    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
