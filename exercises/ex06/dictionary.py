"""Combining two lists into a dictionary."""

__author__ = "730672573"


def invert(d1: dict[str, str]) -> dict[str, str]:
    """Returns a inverted dict where the the values are the keys and the keys are the values."""
    inverted_dict: dict[str, str] = {}
    
    for key in d1:
        value = d1[key]
        if value in inverted_dict:
            raise KeyError("Duplicate values found.")
        inverted_dict[value] = key
    
    return inverted_dict
        
     
def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most popular color in a dict of str."""
    color_list: list[str] = []
    max_count: int = 0
    most_popular_color: str = ""

    for color in colors:
        color_list.append(colors[color])
    
    for i in range(len(color_list)):
        count: int = 0
        current_color = color_list[i]
        for j in range(len(color_list)):
            if current_color == color_list[j]:
                count += 1
        if count > max_count:
            max_count = count
            most_popular_color = current_color
        
    return most_popular_color
    

def count(list1: list[str]) -> dict[str, int]:
    """Returns the count of unique words in a list."""
    dict_count: dict[str, int] = {}
    for elem in list1:
        if elem in dict_count:
            dict_count[elem] += 1
        else: 
            dict_count[elem] = 1
    return dict_count


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Returns a dict with a letter as the key and the words that start with it as the value."""
    letter: str = ""
    word_dict: dict[str, list[str]] = {}
    same_letter: list[str] = []
    for word in list1:
        letter = word[0].lower()
        for elem in list1:
            if letter == elem[0].lower():
                same_letter.append(elem)
        word_dict[letter] = same_letter  
        same_letter = []  
    return word_dict
  

def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance of the dictionary by adding the name associated with the date."""
    new_name: list[str] = []
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        new_name.append(student)
        attendance[day] = new_name
    return attendance