# Guess the number game
import random

print("Hello, what is your name?")
name = input()

print("Hello, " + name + ", I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

# Player guesses number, up to 6 try's
for guessesTaken in range(1, 7) :
    print("Take a guess!")
    guess = int(input())

    if guess < secretNumber :
        print("Your guess is too low.")
    elif guess > secretNumber :
        print("Your guess is too high.")
    else :
        break    # This happens if they guess correctly

if guess == secretNumber :
    print("Good job, " + name + "! You guessed it in " + str(guessesTaken) + " guesses!")
else :
    print("Nope, sorry. The number I was thinking of was " + str(secretNumber))
