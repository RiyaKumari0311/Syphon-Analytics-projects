'''

3. Create a function which takes a number as its argument and return the number of digits in it. Use
of len function is not allowed. For example for 5 it should return 1, for 32 it should return 2 and 123 ,
3 should be returned and so on.

'''



def count_digits(n):
    # Handle negative numbers
    n = abs(n)
    
    # Initialize digit count
    count = 0
    
    # Special case for 0
    if n == 0:
        return 1
    
    # Loop until n becomes 0
    while n > 0:
        n //= 10  # Remove the last digit by integer division
        count += 1  # Increase the digit count
    
    return count

# Example usage
print(count_digits(5))    # Output: 1
print(count_digits(32))   # Output: 2
