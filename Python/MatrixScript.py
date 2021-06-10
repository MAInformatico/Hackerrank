#!/bin/python3

import re

n, m = map(int, input().split())

matrix = []
result = ""

for _ in range(n):
    matrix.append(input())

for i in zip(*matrix):
    result += "".join(i)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", result))
