import random

target = random.randint(1, 100)

guess = int(input("Guess the number between 1-100: "))

while guess != target:
    if guess > target:
        print("Too high!")
        guess = int(input("Try again: "))
    if guess < target:
        print("Too low!")
        guess = int(input("Try again: "))
    if guess == target:
        print(f"You guessed it! it was {target}")