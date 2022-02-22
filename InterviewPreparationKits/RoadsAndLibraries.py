from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(set)
        
    def clone(self):
        g = Graph()
        g.nodes = self.nodes[:]
        for n in self.nodes:
            for e in self.edges[n]:
                g.edges[n].add(e)
        return g

def countClusters(g):
    numCluster = 0
    visited = set()
    n = len(g.nodes)

    clusterSize = []
    
    for node in g.nodes:
        if node in visited: continue
        visited.add(node)

        size = 1
        queue = deque()
        queue.appendleft(node)
        while queue:
            cur = queue.pop()
            for neighbour in g.edges[cur]:
                if neighbour in visited: continue
                visited.add(neighbour)
                queue.appendleft(neighbour)
                size += 1
        numCluster += 1
        clusterSize.append(size)

    return numCluster,clusterSize

if __name__ == '__main__':    

    q = int(input())

    for _ in range(q):
        n,m,clib,croad = [int(x) for x in input().split()]
        edges = [[int(x) for x in input().split()] for _ in range(m)]

        if clib < croad:
            print(clib*n)
            continue
        
        localGraph = Graph()
        localGraph.nodes = range(1,n+1)
        for i,j in edges:
            localGraph.edges[i].add(j)
            localGraph.edges[j].add(i)

        nCluster,cSize = countClusters(localGraph)
        print(nCluster*clib + sum((x-1)*croad for x in cSize))
