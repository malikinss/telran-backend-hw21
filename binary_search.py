# binary_search.py

from typing import List


def b_search_sorted_list(lst: List[int], num: int) -> int:
    """
    Binary search in a sorted list with first-occurrence lookup and insertion
    index.

    Performs a binary search over a sorted list of integers and returns:
        - the index of the **first occurrence** of the searched number if
          it exists;
        - a **negative value** `-(insertion_index + 1)` if the number
          is not found.

    The insertion index is the position at which the searched number could
    be inserted while preserving the sorted order.

    This implementation keeps O(log N) time complexity.

    Args:
        lst (List[int]): Sorted list of integers (ascending order).
        num (int): Number to search for.

    Returns:
        int: Index of the first occurrence of `num`,
             or negative value encoding the insertion point as `-(index + 1)`.

    Examples:
        >>> b_search_sorted_list([1, 2, 3, 4, 5], 3)
        2
        >>> b_search_sorted_list([20, 20, 20], 20)
        0
        >>> b_search_sorted_list([10, 20, 30], 25)
        -3
    """
    left: int = 0
    right: int = len(lst) - 1

    while left <= right:
        middle: int = (left + right) // 2

        if lst[middle] == num:
            if middle == 0 or lst[middle - 1] < num:
                return middle
            right = middle - 1

        elif num < lst[middle]:
            right = middle - 1

        else:
            left = middle + 1

    return -(left + 1)


TEST_CASES: list[dict] = [
    {'list': [1, 2, 3, 4, 5], 'num': 3, 'res': 2},
    {'list': [10, 20, 30, 40], 'num': 10, 'res': 0},
    {'list': [10, 20, 30, 40], 'num': 40, 'res': 3},
    {'list': [20, 20, 20, 20, 20], 'num': 20, 'res': 0},
    {'list': [1, 5, 20, 20, 20, 30], 'num': 20, 'res': 2},
    {'list': [20, 30, 40, 50, 60], 'num': 45, 'res': -4},
    {'list': [10, 20, 30], 'num': 5, 'res': -1},
    {'list': [10, 20, 30], 'num': 40, 'res': -4},
    {'list': [], 'num': 10, 'res': -1},
    {'list': [100], 'num': 100, 'res': 0}
]


for i in range(len(TEST_CASES)):
    result = b_search_sorted_list(
        lst=TEST_CASES[i]['list'],
        num=TEST_CASES[i]['num']
    )
    assert result == TEST_CASES[i]['res']
    print(f'TEST {i+1} PASSED')
