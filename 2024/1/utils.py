"""Common utilities for day one of advent-of-code."""

import os


def yield_data(fname="input.txt"):
    """Yield the input data in tuples."""
    fpath = os.path.dirname(os.path.realpath(__file__)) + "/input/" + fname
    with open(fpath, "r") as f:
        for data in f.readlines():
            data = data.strip().split("   ")
            yield int(data[0]), int(data[1])
