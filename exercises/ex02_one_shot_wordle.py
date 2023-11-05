"""Ex02 one shot wordle - w wordle."""
__author__ = "730672573"
print("\U0001F7E9" * 6)
secret_word: str = "python"
length: int = len(secret_word)
"users quess of the word"
quess: str = input(f"What is your {length}-letter guess? ")
"Check to make sure it is 6 letters"
while len(quess) != len(secret_word):
    quess = input(f"That was not {length} letters! Try again: ")
i = 0
emoji = ""
while i < len(secret_word):
    "Characters at that index are equal"
    if quess[i] == secret_word[i]:
        emoji += "\U0001F7E9"
    else:
        exist = False
        alternate = 0
        "loop through the word to see if the character apprears anywhere else"
        while not exist and alternate < len(secret_word):     
            if quess[i] == secret_word[alternate]:
                exist = True
            else:
                alternate += 1
        if exist:
            "yellow emoji"
            emoji += "\U0001F7E8"
        else:
            "white emoji"
            emoji += "\U00002B1C"
    i += 1
print(emoji)
"not equal to secret word"
if quess != secret_word:
    print("Not quite. Play again soon!")
else: 
    "equal to secret word"
    print("Woo! You got it!")