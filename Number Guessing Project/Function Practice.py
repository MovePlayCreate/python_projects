import arts
from random import randint


# Function for starting the game and getting their difficulty. return difficulty
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5

# Function for deciding if the guess was too high or low, and determining if the game is over or continues
def deciding_step(guess, attempts_remaining):
    """Function takes in the guess and attempts remaining and returns updated turns remaining."""
    if guess != random_number and attempts == 1:
        print("You've run out of guesses. Refresh the page to run again.")
        return 0
    elif guess < random_number:
        print("Too low.\nGuess again.")
        attempts_remaining -= 1
    elif guess > random_number:
        print("Too high.\nGuess again.")
        attempts_remaining -= 1
    elif guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        attempts_remaining = 0
    return attempts_remaining


# Print logo and start the game
print(arts.logo)
random_number = randint(1, 100)
attempts = start_game()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = deciding_step(guess, attempts)