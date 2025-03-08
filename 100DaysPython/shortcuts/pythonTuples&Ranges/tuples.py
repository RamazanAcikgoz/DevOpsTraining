# Tuple : is a fixed with immutable sequence type
# List : is a dynamic with mutable sequence type
# These are commonly used to represent things where you know the exact
# order and how many items are in it.

point = (2.9, 3.0,4.5)
print(point[0])

# Tuple is immutable
# point[0] = 4.0  # This will raise an error

point_3d = point + (5.0,) #, it is necessary
print(point_3d)

x, y, z, r = point_3d # unpack the tuple
print(x, y, z, r)

# Common way to see tuple used
print("My name is: %s %s " % ("Ranczo", "Zoro"))