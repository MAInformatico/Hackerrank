import numpy

N,M = input().split()

lst = []
for i in range(int(N)):
    lst.append(input().split())

arr = numpy.array(lst, int)
rowSum = numpy.sum(arr, axis = 0)
print(numpy.prod(rowSum))
