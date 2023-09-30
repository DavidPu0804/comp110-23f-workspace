"game that completes when you quess the right number"
from random import randint

secret: int = randint(1,10)


guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 3
tries_count: int = 0

while guess != secret and (tries_count < number_of_tries-1: int):
    print("wrong!")
    if (guess<1) or (guess> 10):
        print("thats not between one and ten")
    if guess < secret:
        print("guess was to low")
    elif guess == secret:
        print("guess was equal to secret")
    else:
        print("guess was to high")
    guess = int(input("Guess again! "))
    tries_count += 1

print("you got it!")