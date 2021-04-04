# Number Guessing Game - guess number between 1 and 100 that is randomly chosen.

import random

def start_game():
    number = random.randint(1, 100)
    print("I'm think of a number between 1 and 100...")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guess(number, difficulty)

def guess(number, difficulty):
    game_running = True
    if difficulty == "easy":
        chances = 10
    else:
        chances = 5
    while chances > 0 and game_running:
        print(f"You have {chances} chances remaining.")
        my_chance = int(input("Make a guess: "))
        if my_chance < number:
            chances -= 1
            print("Too Low... ")
            print("Guess again.")
        elif my_chance > number:
            chances -= 1
            print("Too High... ")
            print("Guess Again.")
        else:
            print("You got the number!")
            game_running = False


start_game()