from unittest import TestCase
from random import sample, randint

import chop1
import chop2
import chop3


class BinarySearchMixin(object):
    """Tests binary search functions. To use, make a class inheriting from this
    class and from unittest.TestCase with a method "search" that performs a
    binary search.
    """
    def test_base_cases(self):
        """Test binary search base cases"""
        self.assertEqual(self.search(3, []), -1)
        self.assertEqual(self.search(3, [1]), -1)
        self.assertEqual(self.search(1, [1]), 0)

    def test_odd_list(self):
        """Test binary search on list of odd length"""
        self.assertEqual(self.search(1, [1, 3, 5]), 0)
        self.assertEqual(self.search(3, [1, 3, 5]), 1)
        self.assertEqual(self.search(5, [1, 3, 5]), 2)
        self.assertEqual(self.search(0, [1, 3, 5]), -1)
        self.assertEqual(self.search(2, [1, 3, 5]), -1)
        self.assertEqual(self.search(4, [1, 3, 5]), -1)
        self.assertEqual(self.search(6, [1, 3, 5]), -1)

    def test_even_list(self):
        """Test binary search on list of even length"""
        self.assertEqual(self.search(1, [1, 3, 5, 7]), 0)
        self.assertEqual(self.search(3, [1, 3, 5, 7]), 1)
        self.assertEqual(self.search(5, [1, 3, 5, 7]), 2)
        self.assertEqual(self.search(7, [1, 3, 5, 7]), 3)
        self.assertEqual(self.search(0, [1, 3, 5, 7]), -1)
        self.assertEqual(self.search(2, [1, 3, 5, 7]), -1)
        self.assertEqual(self.search(4, [1, 3, 5, 7]), -1)
        self.assertEqual(self.search(6, [1, 3, 5, 7]), -1)
        self.assertEqual(self.search(8, [1, 3, 5, 7]), -1)

    def test_rand_lists(self):
        """Test binary search in some randomized lists"""
        for _ in xrange(10):
            l = sample(range(100), randint(4, 50))
            l.sort()

            # Binary search on all values in list
            for pos, value in enumerate(l):
                self.assertEqual(self.search(value, l), pos)

            # Test values that aren't in the list
            for x in range(100):
                if x not in l:
                    self.assertEqual(self.search(x, l), -1)


class Chop1Tests(TestCase, BinarySearchMixin):
    def search(self, value, seq):
        return chop1.binary_search(value, seq)


class Chop2Tests(TestCase, BinarySearchMixin):
    def search(self, value, seq):
        return chop2.binary_search(value, seq)


class Chop3Tests(TestCase, BinarySearchMixin):
    def search(self, value, seq):
        return chop3.binary_search(value, seq)
