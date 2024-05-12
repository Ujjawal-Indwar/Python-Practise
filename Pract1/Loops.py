x = 0
y = 0
while x<5:
    print (x)
    x+=1

print("\n")

while y<5:
    y+=1
    print(y)

#infinite loop
# while ture:

'''
for in similar to for each loop in other prg lang
Python for loop is mainly used for iterating through a sequence
such as List, Tuple, Dictionary, Set or Even String

'''

Fruits = ["Banana", "Apple","Mango", "Orange", "Grapes", "Pineapple", "Peach", "Guava"]

for i in Fruits:
    print(i)

for i in range(2,6):
    print(i)

print("Nested for Loop")
for i in range(7):
        for j in range(0,i+1):
            print('@ ',end=" ")

        print("\r")
        

myarr=[]

for i in range(1,11,3):
     my_ar=i**2
     myarr.append(my_ar)
     print(myarr)
    
print(f"Final array is {myarr}")