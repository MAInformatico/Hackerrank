#!/bin/python3

import random
import collections

if __name__ == '__main__':
    for i in collections.Counter(sorted(input())).most_common(3):
      print(*i)
