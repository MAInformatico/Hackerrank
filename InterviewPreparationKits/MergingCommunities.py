#!/bin/python

import sys
from collections import deque

N, Q = map(int,input().strip().split(' '))
sList = [i for i in range(N+1)]
lst = [0] + [1 for i in range(N)]

for i in range(Q):
    inputValue = input().strip().split(' ')
    query = inputValue[0]
    aux = sorted(map(lambda x: int(x),inputValue[1:]))
    i = aux[0]
    if query == 'M' and sList[i] != sList[aux[1]]:
        j = aux[1]
        temp = deque()
        while i != sList[i]:
           temp.append(i) 
           i = sList[i]
        while j != sList[j]:
           temp.append(j) 
           j = sList[j]
        if sList[i] != sList[j]:
            lst[sList[i]] += lst[sList[j]]
            temp.append(j)
            for k in temp:
                sList[k] = sList[i]
    elif query == 'Q':
        temp = deque()
        while i != sList[i]:
           temp.append(i) 
           i = sList[i]
        for k in temp:
            sList[k] = sList[i]
        print(lst[i])
