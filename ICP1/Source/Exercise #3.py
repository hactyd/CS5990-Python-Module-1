"3"


replay = True
import random
luckyNumba = random.randint(0,9)

while replay:
    print("This program allows you to guess a random number from 0-9. If your input is too low or too high it will inform you.")
    guess = int(input("Guess the random number from 0-9: "))
    if guess > luckyNumba:
        print(guess, "is too high.")
    elif guess < luckyNumba:
        print(guess, "is too low.")
    else:
        print("Congratulations", guess, "is correct!")
        replay = False
