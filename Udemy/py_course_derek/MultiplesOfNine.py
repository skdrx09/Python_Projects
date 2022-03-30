import random

rand_list = list(random.randint(1, 1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), rand_list)))

# Using List Comprehensions
print([x for x in [(random.randint(1, 1001)) for i in range(100)] if x % 9 == 0])
