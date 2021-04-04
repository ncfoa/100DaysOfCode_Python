print("Welcome to RedNeck Pizzaria")

size = input("What size pizza would you like? (S, M, L)\n")
pepperoni = input("Would you like pepperoni? (Y or N)\n")
extra_cheese = input("Would you like extra cheese? (Y or N)\n")
total = 0
if size == "S":
    total = total + 15
elif size == "M":
    total = total + 20
else:
    total = total + 25

if pepperoni == "Y" and size == "S":
    total = total + 2
elif pepperoni == "Y" and (size == "M" or size == "L"):
    total = total + 3
else:
    pass

if extra_cheese == "Y":
    total = total + 1
else:
    pass

tip = float(input("What percentage top would you like to give? 10, 12, or 15?\n")) / 100
total = "{:.2f}".format(total + (total * tip))
if tip <= 0:
    print(f"Your total bill is ${total} with no tip.")
else:
    print(f"Your total bill is ${total} including tip.")