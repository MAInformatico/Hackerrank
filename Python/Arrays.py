import numpy

def arrays(arr):
    numArray = numpy.array(arr,float)
    return numArray[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
