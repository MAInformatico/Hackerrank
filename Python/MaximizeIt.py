from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
result = map(lambda f: sum(i**2 for i in f) % M, product(*N))
print(max(result))
