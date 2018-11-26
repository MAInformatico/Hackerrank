#!/bin/python3

N, Q = map(int, input().split())
lastAnswer = 0
seqList = [[] for _ in range(N)]

for __ in range(Q):
    q, x, y = map(int, input().split())
    index = (x ^ lastAnswer) % N
    seq = seqList[index]
    if q == 1:
        seq.append(y)
    elif q == 2:
        size = len(seq)
        lastAnswer = seq[y % size]
        print(lastAnswer)
    else:
        raise ValueError()
