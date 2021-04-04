#Black Jack Game
import random
import subprocess

def clear():
    subprocess.call(['tput', 'reset'])

def logo():
    art = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(art)

def deal_card():
    cards = ["A", "2","3","4","5","6","7","8","9","J","Q","K"]
    card = random.randint(0, 11)
    return cards[card]


dealer_turn = False
game_over = False


def play_game():
    global game_over
    global dealer_turn
    game = {"player": {"cards": [], "value": 0}, "dealer": {"cards": [], "value": 0}}
    game["player"]["cards"].append(deal_card())
    game["dealer"]["cards"].append(deal_card())
    game["player"]["cards"].append(deal_card())
    game["dealer"]["cards"].append(deal_card())

    while not dealer_turn:
        clear()
        logo()
        pv = calculate_value(game["player"]["cards"], game["player"]["value"])
        game["player"]["value"] = pv
        dv = calculate_value(game["dealer"]["cards"], game["dealer"]["value"])
        game["dealer"]["value"] = dv
        print(f'Your Cards: {game["player"]["cards"]}, current score {pv}')
        if dv == 21:
            print(f'Dealer {game["dealer"]["cards"]}, BlackJack!')
            dealer_turn = True
            game_over = True
        else:
            print(f'Dealers first card {game["dealer"]["cards"][0]}')
            if pv > 21:
                print("You busted")
                print(f'Dealer had {game["dealer"]["cards"]}, score: {dv}')
                dealer_turn = True
                game_over = True
            else:
                if input("Type 'h' to get another card, type 's' to stand. ") == "h":
                    game["player"]["cards"].append(deal_card())
                else:
                    dealer_turn = True
                    game_over = False

    while not game_over:
        dv = calculate_value(game["dealer"]["cards"], game["dealer"]["value"])
        game["dealer"]["value"] = dv
        if dv <= 15:
            game["dealer"]["cards"].append(deal_card())
        else:
            print(f'Your final hand {game["player"]["cards"]}, final score: {game["player"]["value"]}')
            print(f'Dealer final hand {game["dealer"]["cards"]}, final score: {game["dealer"]["value"]}')
            if dv > 21:
                print("You Win!")
                game_over = True
            elif pv > dv:
                print("You Win!")
                game_over = True
            elif dv == pv:
                print("You Tied...")
                game_over = True
            else:
                print("You Lose...")
                game_over = True


def calculate_value(cards, prev_value):
    prev_value = prev_value
    value = 0
    for card in cards:

        if (card == "A" and value <= 10) or (card == "A" and prev_value <= 10):
            value += 11
        elif (card == "A" and value > 10) or (card == "A" and prev_value > 10):
            value += 1
        elif card == "K" or card == "Q" or card == "J":
            value += 10
        else:
            value += int(card)

    return value


play = True
logo()
while play:
    if input("Would you like to play a game of BlackJack? Type 'y' or 'n': ") == "y":
        game_over = False
        dealer_turn = False
        play_game()
    else:
        print("It was great playing with you! Goodbye... ")
        play = False
