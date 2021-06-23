import time
from random import randint

player1 = {"name": "", "mark": ""}
player2 = {"name": "", "mark": ""}
winner = False


def intro():
    print(''' 
    To play the game, you will choose need to input the numbered place on the board for the location of where you would
    like to place your mark.
    
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ''')


def pick_players():
    global player1
    global player2
    players = int(input('How many players will there be? (1 or 2) :\n'))
    if players == 2:
        player1["name"] = input('Player 1, What is your name?: \n')
        player2["name"] = input('Player 2, What is your name?: \n')
    elif players == 0:
        player1["name"] = "Computer"
        player2["name"] = 'Computer'
    choose_x_or_o(players)


def choose_x_or_o(players):
    global player1
    global player2
    
    if players == 2:
        mark = input(f'{player1["name"]}, choose your mark (X or O): \n').upper()
        if mark == "X":
            print(f'{player1["name"]}, is X\'s \n')
            print(f'{player2["name"]}, will be O\'s: \n')
            player1["mark"] = "X"
            player2["mark"] = "O"
        elif player1["mark"] == "O":
            print(f'{player1["name"]}, is O\'s \n')
            print(f'{player2["name"]}, will be X\'s: \n')
            player1["mark"] = "O"
            player2["mark"] = "X"
        else:
            print('You have made an invalid selection.')
            exit(1)
    elif players == 1:
        player1["name"] = input("What is your name?\n")
        player2["name"] = "Computer"
        mark = input(f'{player1["name"]}, choose your mark (X or O): \n').upper()
        if mark == 'X':
            print(f'{player1["name"]}, is X\'s \n')
            print(f'{player2["name"]}, will be O\'s: \n')
            player1["mark"] = "X"
            player2["mark"] = "O"
        elif mark == 'O':
            print(f'{player1["name"]}, is O\'s \n')
            print(f'{player2["name"]}, will be X\'s: \n')
            player1["mark"] = "X"
            player2["mark"] = "O"
        else:
            print('You have made an invalid selection.')
            exit(1)
    else:
        player1["mark"] = "X"
        player2["mark"] = "O"


def play_game():
    global winner
    p1_moves = 0
    p2_moves = 0
    positions = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    open_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def show_board():
        print(f'''
        {positions[1]} | {positions[2]} | {positions[3]}
        ---------
        {positions[4]} | {positions[5]} | {positions[6]}
        ---------
        {positions[7]} | {positions[8]} | {positions[9]}
        ''')

    def make_move(player):
        valid = False

        while not valid:
            if player["name"] == "Computer":
                if len(open_spots) >= 2:
                    move = randint(1, len(open_spots) - 1)
                    if 1 >= move >= 9:
                        print('Invalid Move. Choose a position between 1 and 9')
                    elif positions[open_spots[move]] != ' ':
                        print('Invalid Move. Spot on board already taken')
                        time.sleep(5)
                    else:
                        positions[open_spots[move]] = player["mark"]
                        open_spots.remove(open_spots[move])
                        valid = True

                else:
                    positions[open_spots[0]] = player["mark"]
                    valid = True
            else:
                move = int(input(f'{player["name"]}, choose your move: \n'))
                if 1 >= move >= 9:
                    print('Invalid Move. Choose a position between 1 and 9')
                elif positions[move] != ' ':
                    print('Invalid Move. Spot on board already taken')

                else:
                    positions[move] = player["mark"]
                    open_spots.remove(move)
                    valid = True
    
    def check_winner(player):
        global winner
        mark = player["mark"]
        if p1_moves + p2_moves < 5:
            pass
        elif len(open_spots) == 0:
            print("It's a draw!")
            exit(0)
        else:
            if positions[1] == mark and positions[2] == mark and positions[3] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)
            elif positions[4] == mark and positions[5] == mark and positions[6] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[7] == mark and positions[8] == mark and positions[9] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[1] == mark and positions[4] == mark and positions[7] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[2] == mark and positions[5] == mark and positions[8] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[3] == mark and positions[6] == mark and positions[9] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[1] == mark and positions[5] == mark and positions[9] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            elif positions[3] == mark and positions[5] == mark and positions[7] == mark:
                winner = True
                print(f'{player["name"]} has won!')
                exit(0)

            else:
                pass

    while not winner:
        if p2_moves < p1_moves:
            print(f"The remaining open spots are {open_spots}")
            make_move(player2)
            p2_moves += 1
            show_board()
            check_winner(player2)
                
        else:
            print(f"The remaining open spots are {open_spots}")
            make_move(player1)
            p1_moves += 1
            show_board()
            check_winner(player1)


intro()
pick_players()
play_game()
