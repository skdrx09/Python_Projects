# 1, 1, 2, 3, 5, 8 ...

# The fib Sequence is defined by :
# Fn = (Fn - 1) + (Fn - 2)
# Where F(0) = 0 and F(1) = 1


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

print(fib(3))
print(fib(4))
print(fib(5))