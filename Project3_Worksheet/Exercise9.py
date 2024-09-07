'''
9 . Write a function that returns True if two arrays, when combined, form a consecutive sequence. A
consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a
consecutive sequence, but 1, 2, 4, 5 is not. Notes
•
•
The input lists will have unique values.
The input lists can be in any order.
'''

def is_consecutive_sequence(arr1, arr2):
    # Combine the two arrays
    combined = arr1 + arr2
    
    # Sort the combined array
    combined.sort()
    
    # Check if the sequence is consecutive
    for i in range(1, len(combined)):
        if combined[i] - combined[i - 1] != 1:
            return False
    
    return True

arr1 = [1, 3, 2]
arr2 = [4, 5]
print(is_consecutive_sequence(arr1, arr2))  # Output: True

arr1 = [1, 3, 2]
arr2 = [5, 7]
print(is_consecutive_sequence(arr1, arr2))  # Output: False
