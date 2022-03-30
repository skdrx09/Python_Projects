def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

how_many = int(input("How many Fibonacci values should we find?"))

i = 1

while i < how_many:
    print(fib(i))
    i += 1