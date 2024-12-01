"""Times approaches for the advent of code day 1 solutions."""

import timeit

# Part 1
print("---- Part 1 ----")
d_res = timeit.timeit(
    "_use_list_sort('input.txt')",
    setup="from part_one import _use_list_sort",
    number=1,
)
t_res = timeit.timeit(
    "_use_tree('input.txt')", setup="from part_one import _use_tree", number=1
)
print(
    """
List sort approach took {} seconds
Tree sort approach took {} seconds
        """.format(
        d_res, t_res
    )
)

# Part 2
print("---- Part 2 ----")
res = timeit.timeit(
    "_similarity_score('input.txt')",
    setup="from part_two import _similarity_score",
    number=1,
)
print(
    """
Similarity score approach took {} seconds
      """.format(
        res
    )
)
