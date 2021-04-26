import numpy

n, m = map(int, input().split())
matrix = numpy.array([input().strip().split() for _ in range(n)], int)
print (matrix.transpose())
print (matrix.flatten())
