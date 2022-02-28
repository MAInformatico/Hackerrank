#!/bin/python3

import sys
from collections import defaultdict
from collections import deque
import heapq

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(dictGraph, g_nodes):
    costs = [10 ** 10] * (g_nodes + 1)
    work = []
    heapq.heappush(work, (0,1))
    
    costs[1] = 0
    
    while work:
        (currentCost, currentNode) = heapq.heappop(work)
        for (neighbour, cost) in dictGraph[currentNode]:
            localCost = max(currentCost, cost)
            if localCost < costs[neighbour]:
                costs[neighbour] = localCost
                heapq.heappush(work, (localCost, neighbour))
    
    return costs[g_nodes] if costs[g_nodes] < 10 ** 10 else 'NO PATH EXISTS'    
       

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    dictGraph = defaultdict(set)
    
    for _ in range(g_edges):
        start, end, cost = map(int, input().split())
        dictGraph[start].add((end, cost))
        dictGraph[end].add((start, cost))

    print(getCost(dictGraph, g_nodes))
