w = float (input("Please enter your weight in kilograms:"))
h = float (input("Please enter your height in meters:"))

BMI = w/(h*h)

if BMI <= 18.5:
    print ("You are underweight")
elif 18.5 < BMI < 24.9:
    print ("You are normal")
elif 25 < BMI < 29.9:
    print ("You are overweight")
else:
    print ("You are obesity")