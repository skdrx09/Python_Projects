from nis import match
import re

rand_str = "@ Get this string"
regex = re.compile(r"[^@\s].*$")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches:
    print(i)
    