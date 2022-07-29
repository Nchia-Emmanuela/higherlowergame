# python
# test commit
import random
import os
from arts import logo, vs
from game_data import data

def clear():
    os.system('cls')

def format_data(account):
    """Formating the account into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)