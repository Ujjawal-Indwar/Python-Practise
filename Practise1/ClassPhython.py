
class Car:

    def __int__(self, make_and_model, year,gearbox):
        self.make_and_model = make_and_model
        self.year = year
        self.gearbox = gearbox
    def drive(self):
        print(f"{self.make_and_model} {self.year} {self.gearbox}")

    def stop_driving(self):
        print(f"{self.make_and_model}{self.year}{self.gearbox}")


my_bmw = Car('BMW 325i', 2022, 'AUTOMATIC')

print(f"My car's make and model is {my_bmw.make_and_model}")
print(f"My car's year of production is {my_bmw.year}")
print(f"f My car's gearbox is {my_bmw.gearbox}")

