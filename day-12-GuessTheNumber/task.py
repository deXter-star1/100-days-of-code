import random
from art import logo

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5

def check_answer(guess, random_number, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if guess < random_number:
        print("Too low! Try again")
        return turns - 1
    elif guess > random_number:
        print("Too high! Try again!")
        return turns - 1
    else:
        print(f"You guessed correctly! {random_number} was the number!")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY_ATTEMPTS
    else:
        return HARD_DIFFICULTY_ATTEMPTS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(random_number)

    turns = set_difficulty()

    guess = 0
    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        
game()








