from art import logo , vs
from game_data import data
import random

def select_profile(a, b):
    a = random.choice([a, b])
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    return a, b

def verify(winner, guess, score):
    if winner == guess:
        score += 1
        print(f"You're right! Current score: {score}.")
        return True, score
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        return False, score

def get_winner(a, b):
    return a if a['follower_count'] > b['follower_count'] else b

def game():
    continue_game = True
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    while continue_game:
        print(logo)

        print(f"\nCompare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

        actual_winner = get_winner(account_a, account_b)

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 20)
        guessed_profile = account_a if guess == 'A' else account_b

        continue_game, score = verify(actual_winner, guessed_profile, score)
        if continue_game:
            account_a, account_b = select_profile(account_a, account_b)

game()
