"""
Binary search for CodeKata 2

http://codekata.com/kata/kata02-karate-chop/

Unit tests from Dave Thomas in that article.
"""


def binary_search(value, seq):
    """Return the position of the value in the sequence, or -1 if not in
    sequence. Assumes the seq is already in order.
    """
    # Base cases-
    # The list is empty:
    if len(seq) == 0:
        return -1

    # The list has a single element
    if len(seq) == 1:
        if seq[0] == value:
            return 0
        else:
            return -1

    # Otherwise, split the list and check the right half
    center = len(seq) / 2
    if value < seq[center]:
        # value is in first half of list
        return binary_search(value, seq[:center])
    else:
        # value is in second half of list
        pos = binary_search(value, seq[center:])
        if pos == -1:
            return -1
        else:
            return pos + center
