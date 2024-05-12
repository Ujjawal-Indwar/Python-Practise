print("Hi Sir")

"""

This is multiple line comment
Comments

"""

#Python collection (Arrays)
#Sequence--Set, List, Tuple, Dictionary

#set
'''
A set is a collection which is unordered, unchangeable and unindexed
Set items are unchangable, but you can remove items add new items 
NO duplicate members are allowed

'''
set1 = {"abc", 23, True, 20,'f'}
print(type(set1))
print ("set1", set1)

'''
The set() constructor 
It is also possible to use the set() constructor to make a set
'''
#NOTE: the set list is unordered, so the result will display the items in a random order
thisset = set(("apple", "banana", "cherry"))
print("The set() constructor", thisset)



#LIST
'''
List is a collection which is ordered and changable.
Allows duplicate members.

del List(1)
List.pop()
List.remove("value")
sorted(List)

'''

#TUPLE
'''
Tuple is a collection which is ordered and unchangable.
Allows duplicate members.
Reassigning a tuple is valid
tup=(20,30)
tup=(52,62,20)
'''

#DICTIONARY
'''
Dictionary is a collection which is ordered** and changeable.
No duplicate members.
**Python 3.7 dictionaries are ordered.
In Python 3.6 and earlier dictionaries are unordered
'''

List = [1,2,3,'o']
Tuple = (1,2,3,"u","in")
Dictionary = {1:"ujj","citizen":"Indian","age":30,"staus":"Single"}

print(type(List))
print(List)
for i in List:
    print(f"This is a List of {i}\n")

print(type(Tuple))
print(Tuple)

print(type(Dictionary))
print(Dictionary)
print("keys")
for x in Dictionary:
    print(x)

print("values\n")
for y in Dictionary.values():
    print(y)

name=input("Enter your name \n")
age = int(input("Enter your age \n"))
print(name,age)
print("your age is ",age)

age = str(age)
print("Your age is "+age)

name = "Ujjawal Indwar"
print(name[1])

for i in name:
    print(i)

#f String
print(f'This is me {age}')