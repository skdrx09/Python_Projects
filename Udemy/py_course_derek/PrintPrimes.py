def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def get_primes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes 

max_number = int(input("Enter the number up to which you wish to find primes: "))

list_of_primes = get_primes(max_number)
print(list_of_primes)

for prime in list_of_primes:
    print(prime)