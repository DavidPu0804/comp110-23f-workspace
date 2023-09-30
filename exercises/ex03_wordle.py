"""EX03 - Wordle - The completed game."""

__author__ = "730672573"

def contains_char(word: str,char : str) -> bool:
    assert len(char) == 1
    """Check to see if the letter is found in the word"""
    for i in len(word)-1:
        if word[i] == char:
            return True
        
    return False
