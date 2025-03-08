# Dictionaries   
colours = {
    "apple" : "red",
    "banana" : "yellow",
    "cherry" : "red",
    "date" : "brown"
}

print(colours["apple"])
# Output: red

colours["Plumm"] = "green"

empty_dictionary = {} # empty dict

# Wipe an existing dictionary
characters = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
characters = {}
print(characters)

# Edit an item in a dict
characters["a"] = 6

# Loop through dict
for thing in characters:
    print(thing) # It will print out just keys 
    print(characters[thing]) # it will give value as well 