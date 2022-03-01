#!/bin/python3

import math
import os
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    dictionary = {price[i]:i for i in range(n)}
    priceSorted = sorted(price)
    minimumLoss=math.inf
    for i in range(1,n):
        if dictionary[priceSorted[i]]<dictionary[priceSorted[i-1]]:
            minimumLoss=min(minimumLoss,priceSorted[i]-priceSorted[i-1])
    return minimumLoss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
