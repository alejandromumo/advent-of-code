"""Advent of Code 2024, day 3 - regex.

Challenge:

    It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
"""

import os
import re


def read_data(fname):
    """Read the data from the file and return the lines."""
    fpath = os.path.dirname(os.path.realpath(__file__)) + "/input/" + fname
    with open(fpath, "r") as f:
        return f.readlines()


def solution(fname):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    data = read_data(fname)
    prog = re.compile(pattern)
    _sum = 0
    for line in data:
        result = prog.findall(line)
        for r in result:
            _sum += int(r[0]) * int(r[1])
    return _sum


if __name__ == "__main__":
    test_res = solution("test_input.txt")
    assert test_res == 161, f"Wrong result, got: {test_res}"

    res = solution("input.txt")
    print(res)
