# -*- coding: utf-8 -*-


def factorial(n):
    if n < 0:
        return "cant calculate a negative number."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number =int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial(number)}")