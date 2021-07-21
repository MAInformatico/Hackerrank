import re,sys

string = sys.stdin.read()

regex = r'(?<=<)\s?\w+(?=\s)?'

match = re.findall(regex, string)
matchs = sorted(list(set(match)))

print(';'.join(matchs))
