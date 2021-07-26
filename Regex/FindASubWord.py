import re

data = '\n'.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    regexp = re.compile(rf'\w{input()}\w')
    print(len(re.findall(regexp, data)))
