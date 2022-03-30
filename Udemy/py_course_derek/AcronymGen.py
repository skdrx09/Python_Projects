from posixpath import split


name_list = (input("Convert to acronym: ").upper()).split()

acronym = ''

for letter in name_list:
     acronym += letter[0]

print("Your acronym is:", acronym)