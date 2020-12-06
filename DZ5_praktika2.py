from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return n
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return n
def prime_square(n):
    return (is_prime(n))**2
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_prime_numbers = list(map(prime_square, numbers))
print(squared_prime_numbers)