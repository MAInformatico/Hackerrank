#!/bin/python3

from collections import defaultdict
from collections import deque
import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def bfs(graph,x,visited):
    path = []
    queue = deque()
    path.append(x)
    queue.append(x)
    visited[x] = True
    while len(queue) != 0:
        aux = queue.popleft()
        for i in graph[aux]:
            if visited[i] == False:
                path.append(i)
                queue.append(i)
                visited[i] = True
    return path
        

def componentsInGraph(gb):
    graph = defaultdict(list)
    visited = defaultdict(bool)
    result = []
    
    
    for i in range(len(gb)):
        graph[gb[i][0]].append(gb[i][1])
        graph[gb[i][1]].append(gb[i][0])
        

    for i in graph:
        result.append(len(bfs(graph,i,visited)))
    
    print(result)
    result = list(filter(lambda x: x != 1,result))
    print(result)
    return [min(result),max(result)]

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
