"""Combining two lists into a dictionary."""
__author__ = "730672573"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """The function produces a dictionary where the key is the first list thta is paired to a value from the second list."""
    if len(list1) != len(list2):
        return {}
    if len(list1) == 0:
        return {}
    count = 0
    combine: dict[str, int] = {}
    while count < len(list1):
        combine[list1[count]] = list2[count]
        count += 1
    return combine