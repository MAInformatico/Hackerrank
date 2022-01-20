#!/bin/python3

import os
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    maxProfit, period = 0, 0
    localMax = max(prices)
    while len(prices) > 0 :
        day = prices.pop(0)
        if day == localMax: 
            maxProfit += day*period
            period = 0
            if len(prices) > 0 :
                localMax = max(prices)
        elif day < localMax:
            maxProfit -= day
            period += 1
    return maxProfit
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
