from art import logo
from art import vs
from game_data import data
import random
import subprocess

# I am not using the repl.it online environment. For a Mac, you need to invoke the subprocess to properly clear
# the screen and all scroll-back. While this works in the terminal, it does not work properly in the Pycharm IDE but
# does not affect running of the code. I have not tested on Windows.


def clear():
    subprocess.call(['tput', 'reset'])


score = 0
# I made this more with more functions than needed for the practice.


def logo_art():
    print(logo)


def versus():
    print(vs)


def start_game():
    a = get_choices(data)
    b = get_choices(data)
    de_duplicate = True
    while de_duplicate:
        if a == b:
            b = get_choices(data)
        else:
            de_duplicate = False
    pick = choose(a, b)
    compare(a, b, pick)


def get_choices(info):
    return info[random.randint(0, len(info) -1)]


def choose(a, b):
    print(f'Choice A: {a["name"]} a {a["description"]} from {a["country"]}')
    versus()
    print(f'Choice B: {b["name"]} a {b["description"]} from {b["country"]}')
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return choice


def compare(a, b, choice):
    global score
    right = True
    if choice == "a" and a["follower_count"] > b["follower_count"]:
        score += 1

    elif choice == "b" and a["follower_count"] < b["follower_count"]:
        score += 1
    else:
        right = False

    if right:
        clear()
        logo_art()
        print(f'You were right! Current score: {score}')
        start_game()
    else:
        clear()
        logo_art()
        print(f'Sorry, that\'s wrong. Final score: {score}')


logo_art()
start_game()

