"""Part Two - Similarity Score.

Challenge:
 - This time, you'll need to figure out exactly how often each number from the left list
   appears in the right list. 
   Calculate a total similarity score by adding up each number in the left list after multiplying
     it by the number of times that number appears in the right list.

Solution:
    - Yield the data from the file and store both values in different structures:
        Left: Load all the left values into a list
        Right: Load all the right values into a frequency dictionary
    - Iterate over the left values and multiply by the known frequency in the right dictionary
    - Return the sum of the multiplications
"""

from utils import yield_data


def _similarity_score(fname):
    lvals = []
    rfeq = {}
    for lval, rval in yield_data(fname):
        lvals.append(lval)
        curr_freq = rfeq.setdefault(rval, 0)
        rfeq[rval] = curr_freq + 1
    res = 0
    for lval in lvals:
        freq = rfeq.get(lval, 0)
        res += lval * freq
    return res


if __name__ == "__main__":
    # Test example yields 31
    test_res = _similarity_score("test_input.txt")
    assert test_res == 31, f"Test failed: {test_res}"
    res = _similarity_score("input.txt")
    print(f"Result: {res}")
