# A list is an ordered sequence of items
my_list = [1, 2, 3, 4, 5]

# Last item of list :
print(my_list[-1])  # Output: 5

# slicing
print(my_list[0:2]) # not including 2nd index
print(my_list[2:4]) # Start with 2nd index not including 4th index
print(my_list[1:]) # from 1st index to end of list
print(my_list[:3]) # from start of list to 3rd index

# Slicing with step
print(my_list[::2]) # every 2nd item
print(my_list[1::2]) # every 2nd item starting from 2nd index
print(my_list[::-1]) # It will print reverse way of list

# Lists are mutable : They can be modified in-memory