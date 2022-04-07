import re

rand_str = "412-555-1212 412-555-1213 412-555-1214"

regex = re.compile(r"412-(.{8})")
matches = re.findall(regex, rand_str)
print("Matches:", len(matches))
for i in matches:
    print(i)
