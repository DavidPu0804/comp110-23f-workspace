"""Ex04_utils - List and Functions."""

author: str = "730672573"


def all(list: list[int], num: int) -> bool:
    """Determines if every list element is the same as num."""
    if len(list) == 0:
        return False
    count = 0
    "Returns false if one instance is not equal to num."
    while count < len(list):
        if list[count] != num:
            return False
        count += 1
    return True


def max(list: list[int]) -> int:
    """Returns biggest value in list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max = list[0]
    count = 0
    "Finds new max value."
    while count < len(list):
        if max < list[count]:
            max = list[count]
        count += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if list are equal to one another."""
    if len(list1) != len(list2):
        return False
    count = 0
    "Compares elements of different list at the same index."
    while count < len(list1):
        if list1[count] != list2[count]:
            return False
        count += 1
    return True