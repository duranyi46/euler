# how can i find primes?
import math

def prime(n):
    for number in range(2, int(math.sqrt(n))):
        if n % number == 0:
            return False
    return True

def LargestPrimeFactor(k):
    primes = []
    for number in range(2, int(math.sqrt(k))):
        if k % number == 0:
            primes.append(number)
    print(primes)

LargestPrimeFactor(67)
    
