"""
Binary search for CodeKata 2

http://codekata.com/kata/kata02-karate-chop/

Unit tests from Dave Thomas in that article.

"Tail recursive" implementation- binary search by decreasing the range to
search through.
"""


def binary_search(value, seq, start=0, end=None):
    """Return the position of the value in the sequence, or -1 if not in
    sequence. Assumes the seq is already in order.

    start is the index of the first spot in the list to search.
    end is the index+1 of the last spot in the list to search.
    """
    print("search for {} in {} in range {}".format(value, seq, (start, end)))

    # If this is the top call, search the whole list
    if end is None:
        end = len(seq)

    # Base cases
    # No elements to search:
    if start == end:
        return -1

    # Only one element to search:
    if start + 1 == end:
        if seq[start] == value:
            return start
        else:
            return -1

    # Otherwise, search half of this range
    center = (start + end) / 2
    if value < seq[center]:
        # Search first half of list
        return binary_search(value, seq, start, center)
    else:
        # Search second half of list
        return binary_search(value, seq, center, end)
