import re
S = input()
m = re.search(r'([a-zA-Z0-9])\1+', S.strip())
print(m.group(1) if m else -1)
