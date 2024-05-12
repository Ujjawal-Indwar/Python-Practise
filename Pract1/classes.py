class Cars:
    u=100

    #class constructor

    def __init__(self) -> None:
        pass
    
    
    def my_function(self, value):
        print(self.u *  value)

my_car = Cars()
my_car.my_function(10)
print(my_car.u)