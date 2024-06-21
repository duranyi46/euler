# 10 001st prime number
import math
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


primes = []

for number in range(1, 120000):
        if prime(number) == True:
            if len(primes) <= 10000:
                primes.append(number)


print(len(primes))
print(primes[-1])




