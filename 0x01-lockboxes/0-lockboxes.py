#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list where each element is a list of keys.
                           The index of the outer list
                           represents the box number.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
