def greeting():
    print("Hello, World!")

greeting()

def greet_with_name(name): #name is parameter
    print(f"Hello, {name}!")

print()
greet_with_name("Ranczo") # Given name is arguments

def person(name, age, location): # It is positional
    print(f"Name: {name}, Age: {age}, Location: {location}")

person("Ranczo",32,"Tokio") # It is positional arguments

# Keywords arguments
person(name="Marta", age=32, location="Rome")
person(location="Rome",name="Marta", age=32)
person(name="Marta", location="Rome", age=32)