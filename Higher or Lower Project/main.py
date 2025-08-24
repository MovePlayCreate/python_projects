from game_data import data
from art import logo, vs
import random

score = 0
compare_a = random.choice(data)
compare_b = random.choice(data)

def game(compare_a, compare_b, message, score):
    """Takes in both Comparable Celebrities, a message to output, and the score and calls the check answer function when it's time"""
    if compare_a == compare_b:
        compare_b == random.choice(data)
    print(logo)
    print(message)
    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"].lower()}, from {compare_a["country"]}")
    print(vs)
    print(f"Against B: {compare_b["name"]}, a {compare_b["description"].lower()}, from {compare_b["country"]}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 25)
    answer(compare_a, compare_b, choice, score)

def answer(person_a, person_b, choice, score):
    """Takes in the two candidates, the choice the user made, and the score, and updates whether the user is correct and game continues or if the game is over"""
    if person_a["follower_count"] > person_b["follower_count"]:
        if choice == "a":
            score += 1
            message = f"You're right! Current score: {score}"
            return game(person_b, random.choice(data), message, score)
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
    elif person_b["follower_count"] > person_a["follower_count"]:
        if choice == "b":
            score += 1
            message = f"You're right! Current score: {score}"
            return game(person_b, random.choice(data), message, score)
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

# call functions that run the game 
game(compare_a, compare_b, "", 0)
