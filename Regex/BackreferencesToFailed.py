Regex_Pattern = r"\d{8}|^(\d{8})|^(\d{2}-){3}\d{2}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
