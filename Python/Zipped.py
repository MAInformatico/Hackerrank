n, x = map(int, input().split()) 

lista = []
for _ in range(x):
    lista.append(map(float, input().split())) 

for i in zip(*lista): 
    print(sum(i)/len(i))
