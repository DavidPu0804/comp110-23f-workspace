"""Summing the elements of a list using different loops."""


__author__: str = "730672573"


def w_sum(vals: list[float]) -> float: 
    """Loop Through List of float and return the sum using a while loop."""
    count = 0 
    sum: float = 0
    while count < len(vals):
        sum += vals[count]
        count += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Loop Through List of float and return the sum  using a for in."""
    sum: float = 0 
    for idx in range(len(vals)):
        sum += vals[idx]
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Loop Through List of float and return the sum using a for in range."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum   