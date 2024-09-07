'''
5. Write a function which takes any number of arguments from a user and return the result which
should be output of a 2 + b 2 + c 2 +… if a , b ,c are numbers supplied ..i.e if 1,2,3 are supplied then result
returned should be 14. But user may supply any number of inputs so make the function to adapt to
that.

'''

def sum_of_squares(*args):
    result = 0
    for num in args:
        result += num ** 2
    return result

# Example usage
print(sum_of_squares(1, 2, 3))  # Output: 14
