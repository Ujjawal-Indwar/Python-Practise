import random
fruits = ["Bannana", "Mango", "Grapes", 1, 100]
print(fruits[4])
print(fruits[0])

name = input(" Enter the name of your crushes \n")

crush = name.split(" ")

print(f"You are going to marry {crush[random.randint(0, len(crush)-1)]}")


Fru = ["Strawberries","Apples",
    "Grapes",
    "Peaches"
    "Cherries"
    ]
Vegs = ["Spinach","Pears",
    "Tomatoes",
    "Celery",
    "Potatoes"]

List_dirtyDozen = [Fru, Vegs]
print(List_dirtyDozen)