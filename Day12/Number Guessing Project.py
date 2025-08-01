# from art import logo
# import random
#
# print(logo)
#
# number = random.randint(1,100)
# print("Welcome to the number Guessing Game! \nI'm Thinking of Number Between 1 to 100")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")
# lives = 0
# if difficulty == "easy" :
#     lives += 10
# else :
#     lives += 5
# guess = 0
# while lives != 0 and guess != number:
#     print(f"You have {lives} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if number == guess:
#         print(f"You got it! The answer was {number}.")
#     elif number > guess:
#         print(f"Too low. \nGuess again.")
#         lives -= 1
#     else :
#         print(f"Too High. \nGuess again.")
#         lives -= 1
# if number != guess:
#     print(f"You've run out of guesses. The number was {number}. You lose.")

from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()