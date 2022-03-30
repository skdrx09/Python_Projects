# Generate a random list of 5 values between 1 and 9

from random import randrange

rand_list = []
for i in range(5):
    rand_list.append(randrange(1, 10, 1))

print("The random list is: ")
for num in rand_list:
    print(num)