'''
4. Write a function which takes a number as argument suppose 5 and gives results as multiplication
of factorial of each positive number less than or equal to the number given. i.e !5*!4*!3*!2*!1 =
34560.


'''


def factorial(n):
    # Function to compute factorial of a number
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact

def product_of_factorials(n):
    product = 1
    
    # Multiply factorials of each number from 1 to n
    for i in range(1, n+1):
        product *= factorial(i)
    
    return product

# Example usage
number = 5
result = product_of_factorials(number)
print(f"The product of factorials up to {number} is {result}")
