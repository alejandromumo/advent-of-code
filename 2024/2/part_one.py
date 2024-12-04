"""Part 1 - sequences of increasing or decreasing numbers.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
"""
from utils import yield_data


def is_safe(data: list) -> bool:
    """Check if the data is safe."""
    prev = None
    flow = 0  # 1 is increasing, -1 is decreasing, 0 is unknown
    for curr in data:
        if prev is not None:
            diff = curr - prev
            curr_flow = 1 if diff > 0 else -1
            # Check if the flow is increasing or decreasing
            if flow == 0:
                flow = curr_flow
            elif curr_flow != flow:
                return False

            # Check if difference is between 1 and 3
            abs_diff = abs(diff)
            if abs_diff < 1 or abs_diff > 3:
                return False
        prev = curr
    return True


if __name__ == "__main__":
    # Test example returns:
    # True, False, False, False, False, True
    test_data = yield_data("test_input.txt")
    res = sum(is_safe(report) for report in test_data)
    assert res == 2, f"Test failed: {res}"

    # Challenge
    data = yield_data("input.txt")
    res = sum(is_safe(report) for report in data)
    print(res)
