name1 = input("What is person 1's name?: ")
height_m1 = float(input("What is person 1's height in meters?: "))
weight_kg1 = float(input("What is person 3's weight in Kilograms?: "))

name2 = input("What is person 2's name?: ")
height_m2 = float(input("What is person 2's height in meters?: "))
weight_kg2 =  float(input("What is person 2's weight in Kilograms?: "))


name3 = input("What is person 3's name?: ")
height_m3 = float(input("What is person 3's height in meters?: "))
weight_kg3 = float(input("What is person 3's weight in Kilograms?: "))

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 18.5:
        return name + " is under weight"
    else:
        if bmi < 25:
            return name + " is not over weight"
        else:
            return name + " is over weight"
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(result1)
print(result2)
print(result3)
