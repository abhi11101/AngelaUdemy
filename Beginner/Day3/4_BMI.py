
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = round(weight/ (height*height),2)
print(f"Your BMI is {bmi}")

if bmi < 30:
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")
else:
    if 30 >= bmi < 35:
        print("Obese")
    else:
        print("Clinically Obese")
