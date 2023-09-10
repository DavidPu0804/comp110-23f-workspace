"""EX01 - Chardle - A cute step toward Wordle."""

__author__="730672573"

word=input("Enter a 5-character word:")
letter=input("Enter a single character:")
print("Searching for " + letter+ " in " +word)

count=0
for w in word:
    if w==letter:
        print(letter + " found at index " + word.index(w))
        count+1
if count==0:
    print("No instances of " + letter+  " found in " + word)
else:
    print(count +" instances of " + letter+  " found in " + word)


