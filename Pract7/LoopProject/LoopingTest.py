num  = int(input("Enter no of friends you have \n"))
height = [int (x) for x in input(f"Enter height of {num} friends of your\n").split()]

sumHeight = 0

for i in height:
    sumHeight+=i


ans = round(sumHeight/num)
print(f"average height is {ans} of your friends group")
