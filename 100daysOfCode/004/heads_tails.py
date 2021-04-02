import math
import random

callit = input("Call whether you think it will be 'heads' or 'tails'\n").lower()
if callit != "heads" and callit != "tails":
    print("You didn't choose a side")
    exit(0)
coin_toss = math.floor(random.random() * 2 + 1)

if coin_toss == 1 and callit == "heads":
    print("The coin landed on Heads! You Won!")
elif coin_toss == 2 and callit == 'tails':
    print("The coin landed on Tails. You Won")
elif coin_toss == 1 and callit == 'tails':
    print("The coin landed on Heads. Sorry, please try again!")
else:
    print("The coin landed on Tails. Sorry, please try again!")

