import numpy

N, M = map(int, input().strip().split())

lst = numpy.array([ input().strip().split() for _ in range(N) ], int)

print (numpy.mean(lst, axis = 1))
print (numpy.var(lst, axis = 0))
print (round(numpy.std(lst, axis = None),11))
