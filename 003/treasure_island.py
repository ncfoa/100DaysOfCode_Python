print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You are at a cross road. Where do you want to go? ('left' or 'right')\n").lower()

if direction != "left":
    print("You fell into a hole!")
    print("GAME OVER")
    exit(0)
else:
    print("Good choice...")

direction = input('''You come to a lake with an island in the distance. Would you like to wait for a 
boat or swim? ("wait" or "swim")\n''').lower()

if direction != "wait":
    print("You were attacked by rabid Trout!")
    print("GAME OVER")
    exit(0)
else:
    print("Good Choice... ")

direction = input('''You come to a shack with 3 doors, a red door, a yellow door, and a blue door. 
Which door do you choose? ('red', 'yellow', or 'blue)\n''').lower()

if direction == "red":
    print("You got trapped in a room of fire!")
    print("GAME OVER")
    exit(0)
elif direction == "blue":
    print("You were attacked by a horde of angry monsters!")
    print("GAME OVER")
    exit(0)
elif direction == "yellow":
    print("Congratulations! You found the treasure!!")
    print("GAME OVER")
    exit(0)
else:
    print("GAME OVER")
    exit(0)
