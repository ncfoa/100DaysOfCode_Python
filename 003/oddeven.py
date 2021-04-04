num = input("Give me a number: \n")
if type(num) == str:
    try:
        num = int(num)
        if (num % 2) == 0:
            print(f"The number {num} is even")
        else:
            print(f"The number {num} is odd")
    except TypeError:
        print("You did not provide a number...")
        exit(0)
