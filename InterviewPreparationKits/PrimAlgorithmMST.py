#!/bin/python3

import os
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    
    def findMinDistance(distances,visited):
        minDistance = float('inf')
        result = None
        for i in range(n):
            if not visited[i] and distances[i] < minDistance:
                minDistance = distances[i]
                result = i
        return (result,minDistance)
    
    distances = [float('inf')]*n
    distances[start-1] = 0
    visited = [0]*n
    dictionary = {}
    for x,y,z in edges:
        dictionary[(x-1,y-1)]=z
        dictionary[(y-1,x-1)]=z
    result=0
    for _ in range(n):
        x,minDistance = findMinDistance(distances,visited)
        result += minDistance
        visited[x] = 1
        for i in range(n):
            if not visited[i] and (x,i) in dictionary and distances[i]>dictionary[(x,i)]:
                distances[i] = dictionary[(x,i)]
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
