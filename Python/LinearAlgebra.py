import numpy
numpy.set_printoptions(legacy='1.13')

N = input()

lst = []
for i in range(int(N)):
    lst.append(input().split())

arr = numpy.array(lst, float)
print (numpy.linalg.det(arr))
