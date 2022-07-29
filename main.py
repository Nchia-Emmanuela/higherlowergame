# python
# test commit
import random
import os
from arts import logo, vs
from game_data import data

def clear():
    os.system('cls')

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and followers count and returns if they gote it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
# Display art
print(logo)

# Generate a random account
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

guess = input("who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Giving user feedback
if is_correct:
    print("Your're right!")
else:
    print("Sorry, that's wrong.")