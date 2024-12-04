"""Part 2 - sequence tolerate one mistake.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
"""

from utils import yield_data


def is_safe(data: list) -> bool:
    """Check if the data is safe.

    Return the index of the fault level if the report is not safe.
    """
    prev = None
    flow = 0  # 1 is increasing, -1 is decreasing, 0 is unknown
    for idx, curr in enumerate(data):
        if prev is not None:
            diff = curr - prev
            curr_flow = 1 if diff > 0 else -1

            # Check if the flow is increasing or decreasing
            if flow == 0:
                flow = curr_flow
            elif curr_flow != flow:
                return False, idx

            # Check if difference is between 1 and 3
            abs_diff = abs(diff)
            if abs_diff < 1 or abs_diff > 3:
                return False, idx
        prev = curr
    return True, None

def solution(fname):
    """Get the number of safe reports.

    This function will try the following strategies until it finds a safe report (or not):
    - Check the report as is
    - Remove the fault level and check if the report is safe
    - Remove one level at the time from the back and check if the report is safe for each of them
    """
    data = yield_data(fname)
    res = 0
    for report in data:
        safe, idx = is_safe(report)
        if safe:
            res += 1
            continue

        # Try sequence except fault idx
        safe, _ = is_safe(report[:idx] + report[idx + 1 :])
        if safe:
            res += 1
            continue

        # Try sequence in back, removing one level at the time
        for i in range(0, idx):
            safe, _ = is_safe(report[:i] + report[i + 1 :])
            if safe:
                res += 1
                break
    return res

if __name__ == "__main__":
    # Test data returns 5 (I added a report to the test_input.txt)
    res = solution("test_input.txt")
    assert res == 5, f"Test failed: {res}"

    # # Challenge
    res = solution("input.txt")
    print(res)
