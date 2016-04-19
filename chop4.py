"""
Binary search for CodeKata 2

http://codekata.com/kata/kata02-karate-chop/

Unit tests from Dave Thomas in that article.

Create a tree, with all elements on left smaller than all on right.
"""


def binary_search(value, seq):
    """Return the position of the value in the sequence, or -1 if not in
    sequence. Assumes the seq is already in order.
    """
    tree = BinaryTree(seq)
    try:
        return tree.find(value)
    except ValueError:
        return -1


class BinaryTree(object):
    """ """
    def __init__(self, seq):
        length = len(seq)
        if length == 0:
            self.value = None
        else:
            center = length / 2
            if length > 0:
                self.value = seq[center]
            self.left_length = center

            # Make children
            self.left = BinaryTree(seq[:center])
            self.right = BinaryTree(seq[center + 1:])

    def find(self, value):
        """Find index of value in list of all values in order"""
        if self.value is None:
            raise ValueError("Value {} not in tree")

        if self.value == value:
            return self.left_length

        elif value < self.value:
            # Value is in left side of tree
            return self.left.find(value)

        else:
            # Value is in right side of tree
            return self.right.find(value) + self.left_length + 1

    def __str__(self):
        if self.value is None:
            return "_"
        else:
            return "[{}, {}, {}]".format(
                str(self.left), self.value, str(self.right))
