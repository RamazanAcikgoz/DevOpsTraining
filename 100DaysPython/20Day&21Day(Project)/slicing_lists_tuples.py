# Slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5])
print(piano_keys[2:5:2]) # It says take from 2. positon till 5th position on every 2nd index 'c','e'
print(piano_keys[1:6:3]) # 'b' 'e'
print(piano_keys[::2]) # Get every 2nd value --> 'a' 'c' 'e' 'g'
print(piano_keys[::-2]) # It will go reverse way --> 'g' 'e' 'c' 'a'

# It is the same for tuples as well
print(piano_tuple[1:])
