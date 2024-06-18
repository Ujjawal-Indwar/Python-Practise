import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','%','^','&','*','(',')']

print("Welcome to password generator")

no_letters = int(input("Enter no of letters you want in your password\n"))
no_numbers = int(input("Enter no of numbers you want in your password\n"))
no_symbols= int(input("Enter no of symbols you want in your password\n"))

p_l =""
for i in range(0,no_letters):
    p_l+=random.choice(letters)

p_num =""
for j in range(0,no_numbers):
    p_num+=random.choice(numbers)


p_sym =""
for j in range(0,no_symbols):
    p_sym+=random.choice(symbols)

#easy
password = p_l+p_num+p_sym
print(password)

print("\nHard String")
#hard
hard_password =''.join(random.sample(password,len(password)))
print(hard_password)


print("\nHard List")
p_hard = []
for i in range(0,no_letters):
    p_hard+=random.choice(letters)


for j in range(0,no_numbers):
    p_hard.append(random.choice(numbers))


for j in range(0,no_symbols):
    p_hard.append(random.choice(symbols))

random.shuffle(p_hard)
#List back to string
hard_password_shuffled = "".join(p_hard)

print(hard_password_shuffled)

# import random
#
# my_string = "hello world"
#
# # Convert the string into a list of characters
# char_list = list(my_string)
#
# # Shuffle the list using the random.shuffle() function
# random.shuffle(char_list)
#
# # Join the shuffled characters back together into a string
# randomized_string = "".join(char_list)
#
# print(randomized_string)
