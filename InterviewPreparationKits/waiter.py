#!/usr/bin/env python3

import sys

def generatePrimes(total):
    root = int(total**(0.5))
    values = list(range(total+1))
    values[1] = 0
    
    for i in range(2, root+1):
        if values[i] != 0:
            m = total//i - i
            values[i*i: total+1:i] = [0] * (m+1)
    
    return [x for x in values if x !=0]

if __name__ == "__main__":
    nums, q = input().strip().split(' ')
    nums, q = [int(nums), int(q)]
    numbers = list(map(int, input().strip().split(' ')))
    primes = generatePrimes(10000)
    
    stackB = []
    stackNumbers = [numbers, []]
    for i in range(q):
        indexA = int(i % 2)
        b = []
        while len(stackNumbers[indexA]) > 0:
            value = stackNumbers[indexA].pop()
            if value % primes[i] == 0:
                b.append(value)
            else:
                stackNumbers[1 - indexA].append(value)
        stackB.append(b)
            
    for j in stackB:
        if len(j) > 0:
            print(*j[::-1], sep='\n')
    for k in stackNumbers:
        if len(k) > 0:
            print(*k[::-1], sep='\n')
