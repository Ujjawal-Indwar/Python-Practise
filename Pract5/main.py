print("Pizza Deliveries")
size = input("What size pizza do you want? S, M, L\n")
add_pperoni = input("Do you want pepperoni? Y , N\n")
extr_cheese = input("Do you want extra cheese? Y, N\n")
final_bill = 0

if(size == 'S' or size =='s'):
    final_bill+=15


elif(size == "M" or size=="m"):
    final_bill+=20

else:
    final_bill+=25

if (add_pperoni == 'y' or add_pperoni == 'Y'):
    if (size == 'S' or size == 's'):
        final_bill += 2
    else:
        final_bill+= 3


if(extr_cheese == 'y' or extr_cheese=='Y'):
    final_bill+=1


print(f"Your final bill is : ${final_bill}")