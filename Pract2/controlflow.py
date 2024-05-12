#num = int(input("Enter a num\n"))
#if num%2 == 0:
#    print(f"{num} is an even no")
#else:
#    print(f"{num} is a odd no")

height_inCm = float(input("Enter your height in cm"))
height=(height_inCm/100)**2
weight=float(input("Enter your weight in kg"))
bmi = weight/height

if bmi < 18.5:
    print("you are underweight")
elif bmi>25:
    print("You are normal weight")
elif bmi>30:
    print("You are overweight")
elif bmi>35:
    print("You are obese")
else:
    print("You are Clinically obese")

