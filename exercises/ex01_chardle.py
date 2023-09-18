"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730672573"

word = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character = input("Enter a single character:")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

count = 0
if character == word[0]:
    print(character + " found at index " + str(0))
    count += 1
if character == word[1]:
    print(character + " found at index " + str(1))
    count += 1
if character == word[2]:
    print(character + " found at index " + str(2))
    count += 1
if character == word[3]:
    print(character + " found at index " + str(3))
    count += 1
if character == word[4]:
    print(character + " found at index " + str(4))
    count += 1

if count == 0:
    print("No instances of " + character + " found in " + word)
elif count == 1:
    print(str(count) + " instance of " + character + " found in " + word)
else:
    print(str(count) + " instances of " + character + " found in " + word)
print(chr(129312))