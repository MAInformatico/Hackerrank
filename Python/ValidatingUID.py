import re

F = int(input())
while(F>0):
    UID = input()
    print('Valid' if all([re.search(r, UID) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', UID) else 'Invalid')
    F-=1
