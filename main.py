#BMI Calculator

print("Welcome to the BMI Calculator")

weight = float(input("Please enter your weight in lbs: "))
height = float(input("Please enter your height in inches: "))

BMI = weight / (height * height) * 703
BMIformatted = format(BMI,".1f")
print()

if BMI >= 18.5 and BMI <= 25:
    print(f"Your BMI is {BMIformatted}. You are within the ideal weight range.")
else:
    print(f"Your BMI is {BMIformatted}. Your current weight is outside of ideal health guidelines. Please consult your doctor.")
