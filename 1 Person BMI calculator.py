Name = input("What is your name?: ")

Height_m = float(input("Please enter your height in meters: "))

Weight_kg = float(input("Please enter your weight in Kilograms: "))
#the equation being used is weight-kg divided by height-m to the power of 2
BMI = Weight_kg / (Height_m ** 2)
print("bmi: ")
print(BMI)
if BMI < 18.5:
    print('is under weight')
else:
    if BMI < 25:
        print(Name)
        print("is not over weight")
    else:
        print(Name)
        print("is over weight")
