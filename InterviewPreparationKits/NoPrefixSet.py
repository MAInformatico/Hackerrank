#!/bin/python3

import bisect #https://docs.python.org/3/library/bisect.html

def solution():
    array = []

    for _ in range(int(input())):
        word = input()

        bisectRight = bisect.bisect_right(array, word)

        if bisectRight >= 1 and word.startswith(array[bisectRight - 1]):
            print("BAD SET")
            print(word)
            return

        if bisectRight < len(array) and array[bisectRight].startswith(word):
            print("BAD SET")
            print(word)
            return

        array.insert(bisectRight, word)

    print("GOOD SET")

solution()
