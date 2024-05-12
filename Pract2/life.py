age=input("Enter your age\n")
PresentAge = int(age)
TotalAge  = int(90)
print(type(TotalAge))
yrs=TotalAge-PresentAge
weeks=52*yrs
days=yrs*365
months = yrs*12
print(f"You have {days} days {weeks} weeks {months}months left to live")

print(type(yrs))
