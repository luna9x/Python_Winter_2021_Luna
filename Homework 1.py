# Please write a program that prints the first n prime numbers.
# n should be declared as a variable at the beginning of your code or provided as input from the user

import math


def isPrimeNumber(n):
    if n < 2:
        return False
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if n % i == 0:
            return False
    return True


listFirstPrimeNumber = []
print(" First prime numbers:")
for i in range(0, 100):
    if isPrimeNumber(i):
        listFirstPrimeNumber.append(i)
print(listFirstPrimeNumber)
