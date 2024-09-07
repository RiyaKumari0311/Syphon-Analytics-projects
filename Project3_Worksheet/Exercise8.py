'''
8. We have been given a list of whole numbers which represents the color of each gloves, determine
how many pairs of gloves with matching colors there are. For example, there are 7 gloves with
colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd gloves
left, one of each color. The number of pairs is 2. Create a function that returns an integer representing
the number of matching pairs of gloves that are available.

'''

def count_glove_pairs(gloves):
    from collections import Counter
    
    # Count occurrences of each color
    color_counts = Counter(gloves)
    
    # Calculate number of pairs
    pairs = 0
    for count in color_counts.values():
        pairs += count // 2
    
    return pairs

# Example usage
gloves = [1, 2, 1, 2, 1, 3, 2]
print(count_glove_pairs(gloves))  # Output: 2
