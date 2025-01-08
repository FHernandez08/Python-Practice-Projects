from art import vs, logo
from game_data import data
import random

def format_data(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]

    return f"{acc_name}, a {acc_desc}, from {acc_country}"

def final_decision(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_active = True
account_b = random.choice(data)

while game_active:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Account A: {format_data(account_a)}")
    print(vs)
    print(f"Account B: {format_data(account_b)}")

    guess = input("Who has more followers, 'A' or 'B'? ").lower()

    print("\n" * 20)
    print(logo)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = final_decision(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right. The current score is {score}.")
    else:
        print(f"You guessed wrong. The final score is {score}.")
        game_active = False