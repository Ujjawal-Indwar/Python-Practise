name1 = input("Enter your name")
name2 = input("Enter your crush's name")

concat_names= name1+name2;
lower_concat_names = concat_names.lower()

t = lower_concat_names.count('t')
r = lower_concat_names.count('r')
u = lower_concat_names.count('u')
e = lower_concat_names.count('e')

true = t+r+u+e

l = lower_concat_names.count('l')
o = lower_concat_names.count('o')
v = lower_concat_names.count('v')
ee = lower_concat_names.count('e')

love = l+o+v+ee

true_love = int(str(true)+str(love))

print(true_love)

if(true_love<10)or(true_love>90):
    print(f"your score is {true_love}% you go like coke and mentos")
elif(true_love>=40)or(true_love<=50):
    print(f"your score is {true_love}% you are alright together")
else:
    print(f"your score is {true_love}%")
