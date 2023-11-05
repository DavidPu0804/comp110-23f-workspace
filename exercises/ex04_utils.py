"""Ex04_utils - List and Functions"""

author: str = "730672573"

def all(list: list[int], num: int) -> bool:
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i] != num:
            return False
    return True

def max(list: list[int]) -> int:
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max= list[i]
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

