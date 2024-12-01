"""Part 1 - difference between two sets of numbers.

Challenge:
Maybe the lists are only off by a small amount! 
To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Solutions:
1) List sort approach
    - Load all the left values into a list
    - Load all the right values into a list
    - Sort both lists
    - Zip both lists and compute the difference

2) Tree approach
    - Create two Binary Search Trees and insert the values
    - Traverse in order both trees, zip the values and compute the difference

"""

from utils import yield_data


class TreeNode:
    """Implementation of a BST node."""

    def __init__(self, value):
        """Initialize the node with a value."""
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert a value in the BST."""
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def traverse(root):
    """Traverse the BST in order."""
    if root is None:
        return

    yield from traverse(root.left)
    yield root.value
    yield from traverse(root.right)


def _use_tree(fname):
    ltree = None
    rtree = None
    for lval, rval in yield_data(fname):
        ltree = insert(ltree, lval)
        rtree = insert(rtree, rval)
    # Tree sort and result
    res = 0
    for lv, rv in zip(traverse(ltree), traverse(rtree)):
        res += abs(lv - rv)
    return res


def _use_list_sort(fname):
    lvals = []
    rvals = []
    for lval, rval in yield_data(fname):
        lvals.append(lval)
        rvals.append(rval)
    lvals.sort()
    rvals.sort()
    res = 0
    for lv, rv in zip(lvals, rvals):
        res += abs(lv - rv)
    return res


if __name__ == "__main__":
    # Test example yields 11
    test_res = _use_tree("test_input.txt")
    assert test_res == 11, f"Test failed: {test_res}"
    test_res = _use_list_sort("test_input.txt")
    assert test_res == 11, f"Test failed: {test_res}"
    res = _use_tree("input.txt")
    print(f"Result: {res}")
