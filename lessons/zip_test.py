"""Test my zip function."""

__author__ = "730672573"

from lessons.zip import zip


def test_age() -> None:
    """Tests if the person dict is equal to the function zip(name,age)."""
    name: list[str] = ["elon", "tesla", "einstein"]
    age: list[int] = [50, 30, 35]
    person: dict[str, int] = {"elon": 50, "tesla": 30, "einstein": 35}
    assert zip(name, age) == person


def test_product_prices() -> None:
    """Tests if the grocery_list dict is equal to the function zip(product_name,product_prices)."""
    product_name: list[str] = ["apples", "oranges", "peaches"]
    product_prices: list[int] = [2, 3, 5]
    grocery_list: dict[str, int] = {"apples": 2, "oranges": 3, "peaches": 5}
    assert zip(product_name, product_prices) == grocery_list


def test_not_same_size() -> None:
    """Tests if it outputs a empty dict if the list are different sizes."""
    list1: list[str] = ["oranges", "peaches"]
    list2: list[int] = [2, 3, 5]
    combine: dict[str, int] = {}
    assert zip(list1, list2) == combine