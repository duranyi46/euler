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

def LargestPrimeFactor(k):
    MaxF = -1
    primes = []

    # Check for the factor 2
    while k % 2 == 0:
        MaxF = 2
        k //= 2
        primes.append(2)

    # Check for the factor 3
    while k % 3 == 0:
        MaxF = 3
        k //= 3
        primes.append(3)

    # Check for all odd factors from 5 onwards
    for number in range(5, int(math.sqrt(k)) + 1, 6):
        while k % number == 0:
            MaxF = number
            k //= number
            primes.append(number)
        while k % (number + 2) == 0:
            MaxF = number + 2
            k //= number + 2
            primes.append(number + 2)

    # If k is still greater than 1, then k is a prime number
    if k > 1:
        MaxF = k
        primes.append(k)

    print('Max Factor is', MaxF)
    print(primes)

LargestPrimeFactor(600851475143)





    
