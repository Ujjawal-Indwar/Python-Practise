def fun_u():
    print("Have fun")
    for i in range(10):
        print(100)

fun_u()

def fun(name,occupation):
    print(name,occupation)


fun(name="Ujjawal", occupation=1)
fun('Indwar', "To achieve Greatness")

#Arbitary Function
'''
Python Arbitrary Arguments –
As the name suggests, sometimes the programmer does not know the number 
of arguments to be passed into the function. 
In such cases, Python arbitrary arguments are used. In this, 
we use the asterisk (*) to denote this method before the parameter 
in the function.
'''
def myFun(*args):
    print(args[2])

myFun(1,"Ui",'I',100,99)


def addn(a,b):
    return a+b

addition = addn(50,49)
print(addition)


def my_default(fname,lname="Indwar"):
    print(fname,lname)

my_default(fname="Ujjawal")

