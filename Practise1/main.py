# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

Boss = input("Enter the boss name \n")
print("Your Boss is "+Boss)


def u_name(name):{
    print(f" The user name is {name.upper()}")
}

u_name("ujjawal indwar")

def display_course(course_topic,course_name,course_hours):
    print(f"\n course topic : {course_topic}")
    print(f" course name : {course_name}")
    print(f" course hours : {course_hours}")

display_course("Java", "Advance Java",10)
display_course(course_name="Python Master",course_topic="Python",course_hours=20)

def get_car_info(car_maker,car_model,car_year):
    car_info = f"\nCar Info: {car_maker.upper()} {car_model.title()} {car_year}"
    return car_info


BMW = get_car_info("BMW","GLX21",2023)
Volvo = get_car_info("Volvo","VG7",2024)
Lamborghini=get_car_info("lamborghini","urus",2024)
print(BMW,"\n",Volvo,"\n",Lamborghini)