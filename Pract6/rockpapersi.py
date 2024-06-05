import random

print(random.randrange(3, 9))

rock = "Rock"
paper = "Paper"
scissor = "Scissor"

Listu = [rock,paper,scissor]

print("Enter your choice 0-Rock 1-Paper 2-Scissor \n")

yourval = int(input())
compval = random.randrange(0,2)


if(yourval==compval):
    print(f"Draw both are {Listu[yourval]}")

elif(yourval==0) and (compval==1):
    print(f"You Loose...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

elif((yourval==0) and (compval==2)):
    print(f"You Win Congrats...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

elif((yourval==1) & (compval==2)):
    print(f"You Loose...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

elif ((yourval == 1) & (compval == 0)):
    print(f"You Win Congrats...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

elif((yourval == 2) & (compval == 0)):
    print(f"You Loose...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

elif((yourval==2) & (compval==1)):
    print(f"You Win Congrats...... Computer choose {Listu[compval]} and your choise was {Listu[yourval]}")

else:
    print("Something went wrong")
