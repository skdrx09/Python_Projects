import random


flip_list = []
for i in range(100):
    flip_list += random.choice(['H', 'T'])

print("Heads:", flip_list.count('H'))
print("Tails:", flip_list.count('T'))