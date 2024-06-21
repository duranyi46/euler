

def square_sum(n):
    total = 0
    for number in range(1, n+1):
        total += number**2
    return total

def sum_square(n):
    total = 0
    for number in range(1, n+1):
        total += number
    return total**2

print(sum_square(100) - square_sum(100))