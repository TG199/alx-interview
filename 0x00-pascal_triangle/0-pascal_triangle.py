#!/usr/bin/python
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    
    Args:
    n (int): The number of rows to generate.
    
    Returns:
    list of lists: Pascal's triangle represented as a list of lists of integers.
                   Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row
    
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i-1] + prev_row[i])
        
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    return triangle
