
print("Welcome to the tip calculator...")
total = float(input("What was the total bill?\n"))
split = int(input("How many people to split the bill?\n"))
tip = float(input("What percentage top would you like to give? 10, 12, or 15?\n")) / 100
full_total = total + ( total * tip)
pay = full_total // split
print("Each person should contribute:\n" + str(pay))
