import random

# Dave Pat Bailey Pop Trixie Kitty
names = input("What are the names of the people at the table? \n").split(" ")
num = random.randint(0, len(names) -1)

print(f"The person who gets to pay is {names[num]}")