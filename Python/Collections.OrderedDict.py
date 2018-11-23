from collections import OrderedDict
Info = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    Info[item] = Info.get(item, 0) + int(price)
print(*[" ".join([item, str(price)]) for item, price in Info.items()], sep="\n")
