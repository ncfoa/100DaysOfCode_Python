def is_leap(year):
    """Returns if a specific year is a leap year."""
    try:
        year = int(year)
        if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
            return True
        else:
            return False
    except TypeError:
        return ValueError("You did not enter a year as a number")


def days_in_month(year, month):
    """Returns the number of days in a month of a particular year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return month_days[1] + 1
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
days = days_in_month(y, m)
print(days)
