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


def test_base_cases():
    """Test binary search base cases"""
    assert(binary_search(3, []) == -1)
    assert(binary_search(3, [1]) == -1)
    assert(binary_search(1, [1]) == 0)


def test_odd_list():
    """Test binary search on list of odd length"""
    assert(binary_search(1, [1, 3, 5]) == 0)
    assert(binary_search(3, [1, 3, 5]) == 1)
    assert(binary_search(5, [1, 3, 5]) == 2)
    assert(binary_search(0, [1, 3, 5]) == -1)
    assert(binary_search(2, [1, 3, 5]) == -1)
    assert(binary_search(4, [1, 3, 5]) == -1)
    assert(binary_search(6, [1, 3, 5]) == -1)


def test_even_list():
    """Test binary search on list of even length"""
    assert(binary_search(1, [1, 3, 5, 7]) == 0)
    assert(binary_search(3, [1, 3, 5, 7]) == 1)
    assert(binary_search(5, [1, 3, 5, 7]) == 2)
    assert(binary_search(7, [1, 3, 5, 7]) == 3)
    assert(binary_search(0, [1, 3, 5, 7]) == -1)
    assert(binary_search(2, [1, 3, 5, 7]) == -1)
    assert(binary_search(4, [1, 3, 5, 7]) == -1)
    assert(binary_search(6, [1, 3, 5, 7]) == -1)
    assert(binary_search(8, [1, 3, 5, 7]) == -1)


def test_rand_lists():
    from random import sample, randint

    for _ in xrange(10):
        l = sample(range(100), randint(4, 50))
        l.sort()

        # Binary search on all values in list
        for pos, value in enumerate(l):
            assert(binary_search(value, l) == pos)

        # Test values that aren't in the list
        for x in range(100):
            if x not in l:
                assert binary_search(x, l) == -1
