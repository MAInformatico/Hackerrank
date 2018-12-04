from statistics import median
n=int(input())
data=[int(x) for x in input().split()]
data.sort()
t=int(len(data)/2)
if len(data)%2==0:
    L=data[:t]
    U=data[t:]
else:
    L=data[:t]
    U=data[t+1:]
    
print(int(median(L)))
print(int(median(data)))
print(int(median(U)))
