#!/usr/bin/env python3
"""Minimum operation"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in exactly `n` H characters in a text file.

    Operations allowed:
    1. Copy All: Copies all the characters in the file.
    2. Paste: Pastes the copied characters.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The fewest number of operations required to achieve exactly `n` H characters.
         If `n` is impossible to achieve, returns 0.
    """
    
    if n <= 1:
        return 0  # If n is 1 or less, return 0 since no operations are needed or possible.

    operations = 0  # Initialize the operation counter.
    divisor = 2  # Start with the smallest possible divisor.

    # Factorize n, and sum the corresponding operations required.
    while n > 1:
        while n % divisor == 0:
            operations += divisor  # Add the number of operations needed for this factor.
            n //= divisor  # Reduce n by dividing it by the current divisor.
        divisor += 1  # Move to the next potential divisor.

    return operations
