# Breaking the problem step-by-step

from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    account_name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{account_name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    # Take the user guess and follower counts and returns if they got it right
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Display Logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue: 
    # Generate a randon account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count for each account

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # User if statement to check if user is correct

    os.system('clear')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score}")