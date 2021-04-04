import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))

if player > len(game) -1 or player < 0:
    print("You made an invalid selection. Please try again...")
    exit(0)

computer = random.randint(0,2)
print("Player:")
print(game[player] + "\n")
print("Computer:")
print(game[computer] + "\n")


if computer == 0 and player == 2:
    print("You Lose..")
elif computer == 2 and player == 0:
    print("You Win")
elif computer > player:
    print("You Lose..")
elif computer == player:
    print("This game is a draw")
else:
    print("You Win")
