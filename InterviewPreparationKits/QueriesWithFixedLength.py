#!/bin/python3

n,q = [int(number) for number in input().split()]
values = [int(number) for number in input().split()]

for i in range(q):
    result = 0 #min(max(aj))
    d = int(input())
    maxLocal = 0
    
    for j in range(n):
        if values[j] >= maxLocal:
            maxLocal = values[j]
            
        elif j >= d:
            if values[j-d] == maxLocal:
                maxLocal = max(values[j-d+1:j+1])
                
        if j >= d-1:
            if result == 0 or result > maxLocal:
                result = maxLocal

    print(result)
