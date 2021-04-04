print("Welcome to the BMI Calculator")

height = float(input("Please enter your height in inches. ")) * 0.0254
weight = float(input("Please enter your weight in pounds. ")) * 0.45359237

bmi = round(weight / (height ** 2), 1)
if bmi < 18.5:
    print("A person with a BMI of " + str(bmi) + " is considered as underweight.")
elif bmi < 25:
    print("A person with a BMI of " + str(bmi) + " is considered as normal weight.")
elif bmi < 30:
    print("A person with a BMI of " + str(bmi) + " is considered as overweight.")
elif bmi < 35:
    print("A person with a BMI of " + str(bmi) + " is considered as obese.")
else:
    print("A person with a BMI of " + str(bmi) + " is considered as clinically obese.")
