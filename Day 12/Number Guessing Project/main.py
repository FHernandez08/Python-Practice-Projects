import random
import art

easy_level = 10
hard_level = 5

def random_number():
    return random.choice(range(1, 101))

guess_to_match = random_number()

def compare(user_guess):
    if user_guess > guess_to_match:
        print("Your guess is to high!")
    else:
        print("Your guess is to low!")

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choose_level == 'hard':
        print(f"You have {hard_level} attempts remaining to guess the number.")
        lives = hard_level
    elif choose_level == 'easy':
        print(f"You have {easy_level} attempts remaining to guess the number.")
        lives = easy_level

    while lives > 0:
        guess = int(input("Make a guess: "))

        compare(guess)

        if guess == guess_to_match:
            print(f"You have guessed the correct number. The number was {guess_to_match}.")
            break

        if guess != guess_to_match:
            lives -= 1

        if lives == 0:
            print(f"You ran out of lives and lost the game. The correct number was {guess_to_match}.")
        else:
            print(f"You have {lives} attempts to guess the number.")

while input("Do you want to play a guessing number game? Type 'yes' or 'no': ").lower() == 'yes':
    play_game()