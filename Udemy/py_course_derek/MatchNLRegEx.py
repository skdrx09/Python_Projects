import re

long_str = '''Just some words
and some more\r
and more
'''

matches = re.findall(r"[\w\s]+[\r]?\n", long_str)

print("Matches:", len(matches))

for i in matches:
    print(i)