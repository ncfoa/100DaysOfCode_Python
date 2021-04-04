#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '@']

print("Welcome to the PyPassword Generator!")
max_size= int(input("How many characters would you like in your password?\n"))
require_symbols = input(f"Would you like special characters? ('y' or 'n')\n").lower()
require_numbers = input(f"Would you like numbers? ('y' or 'n')\n").lower()
sym = 2
num = 2
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

while len(password) != max_size:
    if require_symbols == "y":
        while len(password) < sym:
            sym_pick = random.randint(0, len(symbols) -1)
            password.append(str(symbols[sym_pick]))

    if require_numbers == "y":
        while len(password) < (sym + num):
            num_pick = random.randint(0, (len(numbers) - 1))
            password.append(numbers[num_pick])

    let_pick = random.randint(0, len(letters) - 1)
    password.append(letters[let_pick])

random.shuffle(password)
print("".join(password))
