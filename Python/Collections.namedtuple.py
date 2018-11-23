from collections import namedtuple
(n, categories) = (int(input()), input().split())
Data = namedtuple('Grade', categories)
marks = [int(Data._make(input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
