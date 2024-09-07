'''
1.Write a python function which should be capable of finding the factorial of any given number as an
argument.
'''


def factorial(n):
    # Factorial is only defined for non-negative integers
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

# Example usage
number = 5
print(f"Factorial of {number} is {factorial(number)}")
