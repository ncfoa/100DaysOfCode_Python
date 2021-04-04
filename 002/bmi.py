print("Welcome to the BMI Calculator")

height = float(input("Please enter your height in inches. ")) * 0.0254
weight = float(input("Please enter your weight in pounds. ")) * 0.45359237

bmi = round(weight / (height ** 2), 1)
if bmi < 18.5:
    print("A person with a BMI of " + str(bmi) + " is underweight ")
elif bmi < 24.9:
    print("A person with a BMI of " + str(bmi) + " is normal weight ")
else:
    print("A person with a BMI of " + str(bmi) + " is overweight ")
