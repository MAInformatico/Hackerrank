import numpy

n, m, p = map(int,input().split())
matrixA = numpy.array([input().split() for _ in range(n)],int)
matrixB = numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((matrixA, matrixB), axis = 0))
