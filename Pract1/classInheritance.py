class Car:
    name = ""
    color = ""
    make = ""
    brand = ""
    def __init__(self,brand,color) :
        self.brand = brand
        self.color = color

    def car_details(self):
        print("This is a ", self.brand," and the color is ",self.color)

my_car = Car("BMW", "white")
my_car.car_details()


'''
class Benz(Car):
    pass
'''
class Benz(Car):
    def car_details(self):
        return super().car_details()
        print("I also need a sports car")

class BMW(Car):
    pass

my_benz = Car("Benz 100", "black")

my_benz.car_details()

my_benz2 = Benz("Benz200","Green")
my_benz2.car_details()