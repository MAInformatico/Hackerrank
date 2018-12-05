a , b = input().split()
prob =int(a)/int(b)
inspc = int(input())

print(round((1-prob)**(inspc-1)*prob,3))
