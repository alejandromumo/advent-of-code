"""Advent of Code 2024, day 3 - regex.

Challenge:

    It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
"""

import os
import re


def solution(fname):
    # Read data
    fpath = os.path.dirname(os.path.realpath(__file__)) + "/input/" + fname
    data = open(fpath).read()

    # Patterns
    m_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    dont_pattern = r"don't\(\).*?do\(\)|don't\(\).*"

    # Compute results
    # re.DOTALL is necessary to avoid also match newlines (which the input might contain)
    _sum = 0
    result = re.sub(dont_pattern, " ", data, flags=re.DOTALL)
    tuples = re.findall(m_pattern, result, flags=re.DOTALL)
    for tp in tuples:
        _sum += int(tp[0]) * int(tp[1])
    return _sum

if __name__ == "__main__":
    test_res = solution("p2_test_input.txt")
    assert test_res == 48, f"Wrong result, got: {test_res}"

    res = solution("input.txt")
    print(res)