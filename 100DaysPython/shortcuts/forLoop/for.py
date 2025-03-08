

colors = ['Blue', 'Green', 'Red', 'Purple'] # List
for color in colors:
    print(color)


point = (2.1, 3.0, 7) # Tuples
for value in point:
    print(value)

ages = {'kevin': 59, 'Rocky': 40, 'Kayla': 21} # Dictionary
for key in ages:
    print(key, ages[key])
    print(f"{key} is {ages[key]} ")

for name, age in ages.items():
    print(f"Person named : {name}")
    print(f"Age of {age}")

for letter in "my_string":
    print(letter)

list_of_points = [(1, 2), (2, 3), (3,4)]
# Iterate over the list of tuples
for x,y in list_of_points:
    print(f"x: {x}, y: {y}")