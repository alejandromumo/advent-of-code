"""Utility functions for the Advent of Code 2024, day 2."""

import os


def yield_data(fname):
    """Read the data from the file and return each line mapped to a list of integers."""
    fpath = os.path.dirname(os.path.realpath(__file__)) + "/input/" + fname
    with open(fpath, "r") as f:
        for line in f.readlines():
            yield list(map(int, line.strip().split(" ")))

class TreeNode:
    """Implementation of a BST node."""

    def __init__(self, value, parent=None):
        """Initialize the node with a value."""
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

def traverse(root):
    """Traverse the BST in order."""
    if root is None:
        return

    yield from traverse(root.left)
    yield root.value
    yield from traverse(root.right)
