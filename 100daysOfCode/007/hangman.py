import requests
import random
from hangman_ascii_art import stages, logo
from replit import clear


link = "https://random-word-api.herokuapp.com/word?number=5"
blanks = []
word = []
stage = -1
stages = stages


def get_word():

    global word
    global link
    global blanks
    r = requests.get(url=link)
    word_list = r.json()

    word = list(random.choice(word_list))
    # word = list("firefly")
    for letter in word:
        blanks.append("_")

    guess()


guessed = []
game_started = False


def guess():
    global stage
    global blanks
    global game_started

    if not game_started:
        print(logo)
        print(*blanks, sep=" ")
        pick = input("Guess a letter: \n").lower()
        game_started = True
        clear()
    else:
        print(*blanks, sep=" ")
        print(stages[stage])
        print("guessed letters:")
        print(*guessed, sep=" ")
        print("")
        pick = input("Guess a letter: \n").lower()
        clear()
    check(pick)


def check(pick):
    global word
    global guessed
    global blanks
    i = 0
    while i < len(word):
        if word[i] == pick:
            blanks[i] = pick
            i += 1

        else:
            i += 1
    if pick in guessed:
        print("You have already chosen that letter...")
        guess()
    check_status(pick)


def check_status(pick):
    global blanks
    global stage
    if pick not in guessed and pick not in blanks:
        guessed.append(pick)
        stage -= 1
    if "_" in blanks and len(guessed) < 6:
        guess()
    elif "_" not in blanks:
        print(*blanks, sep=" ")
        print(stages[stage])
        print("You Win!")
    else:
        print(*blanks, sep=" ")
        print(stages[stage])
        print("The word was " + "".join(word))
        print("Sorry, you lost. Try again!")


get_word()


