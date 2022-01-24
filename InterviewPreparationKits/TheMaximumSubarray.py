#!/bin/python3

test = int(input())
while test:
    test -= 1
    input()
    numList = [int(i) for i in input().split()]
    maxSum = 0
    current = 0
    localMax = 0
    maxIntoList = max(numList)
    if maxIntoList < 0:
        print(str(maxIntoList) + " " + str(maxIntoList))
        continue
    for i in range(len(numList)):
        if current < 0:
            current = 0
        current += numList[i]
        if current > maxSum:
            maxSum = current
        if numList[i] > 0:
            localMax += numList[i]
    print(str(maxSum) + " " + str(localMax))
