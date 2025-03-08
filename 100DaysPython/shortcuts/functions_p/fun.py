# Functions are known as first-class citizens in Python
# It means we can pass them around as values in addition to calling them

def hello_world():
    print("Hello, World!")

hello_world()


def print_name(name):
    print(name + " is here!")

print_name("Ranczo")


def add_two(num):
    return num + 2

print(add_two(6))

def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Ranczo", 25, "Toyota")) # position argument
print(contact_card(age = 32, car_model='Porsche', name= 'Rocky')) # keyword argument


def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(25)) # returns True
print(can_drive(15)) # returns False


 
