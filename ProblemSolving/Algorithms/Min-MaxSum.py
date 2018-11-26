#!/bin/python

import sys

if __name__ == "__main__":
    lst = map(int,raw_input().strip().split(' '))
    x = sum(lst)
    print (x-(max(lst))), (x-(min(lst)))
