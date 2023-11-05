"""write unit tests for the 5 functions."""
__author__ = "730672573"
from exercises.ex06 import dictionary 
import pytest


def test_invert() -> None:
    """Test if it inverts the dict of letters correctly."""
    letters: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    inverted_letters: dict[str, str] = {"b": "a", "d": "c", "f": "e"}
    assert dictionary.invert(letters) == inverted_letters


def test_invert_name() -> None:
    """Test if it inverts the dict of first and last names of people."""
    names: dict[str, str] = {"Elon": "Musk", "Albert": "Einstein", "Nikola": "Tesla"}
    inverted_names: dict[str, str] = {"Musk": "Elon", "Einstein": "Albert", "Tesla": "Nikola"}
    assert dictionary.invert(names) == inverted_names


def test_duplicate_values() -> None:
    """Test it shows a error when having duplicate vaules."""
    with pytest.raises(KeyError):
        names: dict[str, str] = {"Elon": "Musk", "Albert": "Musk", "Nikola": "Tesla"}
        dictionary.invert(names)
    

def test_popular_color() -> None:
    """Test what the most popular color is."""
    colors: dict[str, str] = {"bob": "blue", "elon": "black", "newton": "orange", "einstein": "orange"}
    popular_color: str = "orange"
    assert dictionary.favorite_color(colors) == popular_color


def test_first_popular_color() -> None:
    """Test what the most popular color is and makes sure it is the first one that appears if their is a tie."""
    colors: dict[str, str] = {"bob": "blue", "Tesla": "blue", "elon": "black", "newton": "orange", "einstein": "orange"}
    popular_color: str = "blue"
    assert dictionary.favorite_color(colors) == popular_color


def test_empty_color() -> None:
    """Test what happens if the color dict is empty, should return a empty str."""
    colors: dict[str, str] = {}
    popular_color: str = ""
    assert dictionary.favorite_color(colors) == popular_color


def test_count() -> None:
    """Test the count if their is values in the list."""
    count: list[str] = ["lol", "lol", "lol"]
    count_dict: dict[str, int] = {"lol": 3}
    assert dictionary.count(count) == count_dict


def test_different_values_count() -> None:
    """Test the count if their is values in the list."""
    count: list[str] = ["lol", "lol", "hi", "hi", "hi"]
    count_dict: dict[str, int] = {"lol": 2, "hi": 3}
    assert dictionary.count(count) == count_dict


def test_incorrect_data_type() -> None:
    """Test the case where the count list contains int."""
    count: list[str] = ["lol", 3, "hi", 5, "hi"]
    count_dict: dict[str, int] = {"lol": 1, 3: 1, "hi": 2, 5: 1}
    assert dictionary.count(count) == count_dict


def test_alphabetize_matches() -> None:
    """Test to see if it returns the correct dict with the mathces."""
    word: list[str] = ["lol", "elon", "hawaii", "egg", "hi"]
    letter_sorted: dict[str, list[str]] = {"l": ["lol"], "e": ["elon", "egg"], "h": ["hawaii", "hi"]}
    assert dictionary.alphabetizer(word) == letter_sorted


def test_alphabetize() -> None:
    """Test to see if it returns the correct dict with the mathces."""
    word: list[str] = ["lol", "lake", "loop", "egg", "hi"]
    letter_sorted: dict[str, list[str]] = {"l": ["lol", "lake", "loop"], "e": ["egg"], "h": ["hi"]}
    assert dictionary.alphabetizer(word) == letter_sorted


def test_empty() -> None:
    """Test to see if it returns the a empty dict."""
    word: list[str] = []
    letter_sorted: dict[str, list[str]] = {}
    assert dictionary.alphabetizer(word) == letter_sorted


def test_new_day() -> None:
    """Test to see if it returns the correct dictby appending the new day and students."""
    attendance: dict[str, list[str]] = {"monday": ["elon", "tesla"], "tuesday": ["joe", "lex"]}
    day: str = "wednesday"
    students: str = "bob"
    new_attendance: dict[str, list[str]] = {"monday": ["elon", "tesla"], "tuesday": ["joe", "lex"], "wednesday": ["bob"]}
    assert dictionary.update_attendance(attendance, day, students) == new_attendance


def test_same_day() -> None:
    """Test to see if it returns the correct dict by adding the new student to tuesday."""
    attendance: dict[str, list[str]] = {"monday": ["elon", "tesla"], "tuesday": ["joe", "lex"]}
    day: str = "tuesday"
    students: str = "bob"
    new_attendance: dict[str, list[str]] = {"monday": ["elon", "tesla"], "tuesday": ["joe", "lex", "bob"]}
    assert dictionary.update_attendance(attendance, day, students) == new_attendance


def test_empty_dict() -> None:
    """Test to see if it returns a empty dict."""
    attendance: dict[str, list[str]] = {}
    day: str = ""
    students: str = ""
    new_attendance: dict[str, list[str]] = {"": [""]}
    assert dictionary.update_attendance(attendance, day, students) == new_attendance