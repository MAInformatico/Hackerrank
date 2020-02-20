#!/bin/python3

# Complete the checkMagazine function below.
from collections import Counter

def checkMagazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    if checkMagazine(magazine, note) == True:
        print('Yes')
    else:
        print('No')
