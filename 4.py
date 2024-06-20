# palindromic number

def largest_palindromic(n):
    max_number = int('9' * n)
    min_number = int('1' + '0' * (n-1))
    max_palindromic = 0
    print(max_number)
    print(min_number)
    for number in range(min_number, max_number):
        for number2 in range(max_number, min_number, -1):
            potential_palindromic = str(number * number2)
            if potential_palindromic[0:n] == potential_palindromic[:n-1:-1]:
                if int(potential_palindromic) > max_palindromic:
                    max_palindromic = int(potential_palindromic)
                

    print('max:', max_palindromic)


largest_palindromic(3)



    

