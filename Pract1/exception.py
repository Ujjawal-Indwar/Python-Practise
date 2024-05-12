#raising exception
#exception alias
#else

try:
    user_input = int(input("Enter a number between 1-10 \n"))

except ValueError as e:
    print(e)


'''
if user_input<1 or user_input>10:
    raise ValueError("only values between 1 to 10 is allowed")

'''
try:
    name = 1
    print(name)

except NameError:
    print("the variable is not defined")
else:
    print("the try block didnot execute for some reason")