import numpy

numpy.set_printoptions(legacy = '1.13')
data = numpy.array(input().strip().split(), float)
print(numpy.floor(data), numpy.ceil(data), numpy.rint(data), sep = "\n")
