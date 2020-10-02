#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    dictCount = dict()
    result = list()
    for i in queries: 
        if i[0] == 1:
            try:
                dictCount[i[1]] += 1
            except:
                dictCount[i[1]] = 1

        elif i[0] == 2:
            try:
                dictCount[i[1]] -= 1
                if dictCount[i[1]] == 0:
                    del dictCount[i[1]]
            except:
                continue
        
        else:
            if i[1] in set(dictCount.values()):
                result.append('1')
            else:
                result.append('0')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
