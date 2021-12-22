w = float (input("Please enter your weight in kilograms:"))
h = float (input("Please enter your height in meters:"))

BMI = w/(h*h)

if BMI <= 18.5:
    print ("underweight")
elif 18.5 < BMI < 24.9:
    print ("normal")
elif 25 < BMI < 29.9:
    print ("overweight")
else:
    print ("obesity")