'''
6.Write a function which accepts 3 arguments from the user.1 .number 1, 2. Number2 and 3. An
operation. The operation supported should be +, -, *, and /. The function should return the result of
given operation. For example arguments are 3,2,+ then result returned should be 5.

'''


def calculate(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operation. Use +, -, *, or /."

# Example usage
print(calculate(3, 2, '+'))  # Output: 5
print(calculate(3, 2, '-'))  # Output: 1
print(calculate(3, 2, '*'))  # Output: 6
print(calculate(3, 2, '/'))  # Output: 1.5
print(calculate(3, 0, '/'))  # Output: Error: Division by zero is not allowed.
print(calculate(3, 2, '^'))  # Output: Error: Unsupported operation. Use +, -, *, or /.
