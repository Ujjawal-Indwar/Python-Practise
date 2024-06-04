import  random

row1=["👀", "👀", "👀"]
row2=["👀","👀","👀"]
row3=["👀","👀","👀"]

crissCross = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n" )

x = input("Enter the position of X" )
rowPos = int(x[0])
colPos = int(x[1])

selected_row = crissCross[colPos-1]
selected_row[rowPos-1]="X"

print("*****************")
print(f"{row1}\n{row2}\n{row3}\n" )
