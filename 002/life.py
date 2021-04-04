print("Find out how many weeks you have lived:")

birth_year = input("What year were you born?")
current_year = input("What is the current year?")
age = int(current_year) - int(birth_year)
months_until_90 = str((90 - age) * 12)
weeks_until_90 = str((90 - age) * 52)
days_until_90 = str((90 - age) * 365)

print(f"You have {days_until_90}  days, {weeks_until_90}  weeks, and {months_until_90}  months left.")