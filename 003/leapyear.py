year = input("Please enter a year as a 4 digit number: \n")

try:
    year = int(year)
    if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
        print(f"{year} is a leap year and has 366 days")
    else:
        print(f"{year} is not a leap year and has 365 days")
except TypeError:
    print("You did not enter a year as a number")