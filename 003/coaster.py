print("Welcome to the roller coaster")
height = int(input("Enter your height in inches \n"))
if height >= 48:
    print("Congratulations, You may ride the coaster!")
    age = int(input("Enter your age: \n"))
    total = 0
    if age <= 12:
        total = total + 5
    elif age <= 18:
        total = total + 7
    else:
        total = total + 12

    picture = input("Would you like a picture? Type yes or press enter for no. \n")
    if picture == "yes" or picture == "YES" or picture == "Yes":
        total = total + 3
        print(f"Your total is ${total}")
    else:
        print(f"Your total is ${total}")
else:
    print('You must be at least 48" to ride this ride')