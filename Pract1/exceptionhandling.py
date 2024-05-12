#exception events
try:
    print(name)
except NameError:
    print("some error regarding name")

try: 
    divide=10/0
    print(divide)
except ZeroDivisionError:
    print("number is not divisible by 0")
finally:
    print("finally exist here and it is useful to close objects and clean up resources\n")
