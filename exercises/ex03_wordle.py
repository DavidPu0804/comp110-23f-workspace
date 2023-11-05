"""EX03 - Wordle - The completed game."""

__author__ = "730672573"


def contains_char(word: str, char: str) -> bool:
    """Check to see if the letter is found in the word."""
    assert len(char) == 1
    for i in range(len(word)):
        if word[i] == char:
            return True
       
    return False


def emojified(quess: str, secret: str) -> str:
    """See how closely the two strings match."""
    assert len(quess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result = ""
    "box colors"
    for i in range(len(quess)):
        if quess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, quess[i]):
            result += YELLOW_BOX
        else: 
            result += WHITE_BOX
    return result


def input_guess(length: int) -> str:
    """Prompts the user for a guess for the specified length."""
    quess: str = input(f"Enter a {length} character word: ")
    while len(quess) != length:
        quess = input(f"That wasn't {length} chars! Try again: ")
    return quess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    count = 1
    secret_word = "codes"
    length = len(secret_word)
    match = "\U0001F7E9" * length
    while count <= 6:
        "number of turns"
        print(f"=== Turn {count}/6 ===")
        emoji: str = emojified(input_guess(length), secret_word)
        print(emoji)
        "display result"
        if emoji == match:
            print(f"you won in {count}/6 turns!")
            return
        else:
            count += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()   