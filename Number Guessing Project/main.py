# Number guessing game computer randomly generates a number from 1 to 100 and will tell user if their
# guess is too high or too low until they guess it (win) or have no more guesses left (lose)
import arts
import random
print(arts.logo)

attempts = 0
random_number = random.randint(1, 100)
#print(f"giving it away for science: {random_number}")
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess != random_number and attempts == 1:
        print("You've run out of guesses. Refresh the page to run again.")
    elif guess < random_number:
        print("Too low.\nGuess again.")
    elif guess > random_number:
        print("Too high.\nGuess again.")
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        attempts = 0
    attempts -= 1

