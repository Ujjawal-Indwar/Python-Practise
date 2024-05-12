print("Welcome to the Bill Calculator")
bill = int(input("What was the total bill\n"))
tip = int(input("What % tip you gave 10% , 15%, 20%, 30% \n"))
split = int(input("In between how many people you wanna split the bill\n"))

#billwithtip = tip/100 *bill + bill
#billwithtip = bill * (1 +tip/100)

tip=(tip/100)+1

eachPerson = bill*tip/split
eachPerson = round(eachPerson,2)
finalAmountPerPerson = "{:.2f}".format(eachPerson)
print(f"Each person should pay {finalAmountPerPerson}rs")