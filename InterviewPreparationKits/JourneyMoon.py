#!/bin/python3

import sys

def findAstronaut(ast):
  if astronaut[ast] < 0:
    return ast
  astronaut[ast] = findAstronaut(astronaut[ast])
  return astronaut[ast]

def join(x, y):
  x = findAstronaut(x)
  y = findAstronaut(y)
  if x != y:
    astronaut[x] = y

if __name__ == '__main__':   
    n, p = sys.stdin.readline().split()
    n, p = int(n), int(p)
    astronaut = [-1 for k in range(n)]
    
    for i in range(p):
        x, y = sys.stdin.readline().split()
        x, y = int(x), int(y)
        join(x, y)

    countPairs = [0 for i in range(n)]
    
    for i in range(n):
        pair = findAstronaut(i)
    countPairs[pair] = countPairs[pair] + 1
    print(sum([x * (n - x) for x in countPairs]) // 2)
