#!/bin/python3

import os
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    previousPos = -1
    localLen = 0
    
    for i in s:
        localWeight = ord(i) - ord('a') + 1
        weights.add(localWeight)
        if previousPos == i:
            localLen += 1
            weights.add(localLen*localWeight)
        else:
            previousPos = i
            localLen = 1
    
    result = []
    
    for i in queries:
        if i in weights:
            result.append("Yes")
        else:
            result.append("No")
            
    return result
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
