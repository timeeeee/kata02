"""
Binary search for CodeKata 2

http://codekata.com/kata/kata02-karate-chop/

Unit tests from Dave Thomas in that article.

This implementation is iterative, using a while loop to reduce the search range
to a length of 0 or 1.
"""


def binary_search(value, seq):
    """Return the position of the value in the sequence, or -1 if not in
    sequence. Assumes the seq is already in order.
    """
    start = 0
    end = len(seq)
    while end - start > 1:
        center = (end + start) / 2
        if value < seq[center]:
            end = center
        else:
            start = center
    if start == end or seq[start] != value:
        return -1
    else:
        return start
