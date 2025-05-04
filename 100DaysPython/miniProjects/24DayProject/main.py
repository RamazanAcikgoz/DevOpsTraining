# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Read the template letter
with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter_template = file.read()

# Read names from the file (or use a list instead)
with open('./Input/Names/invited_names.txt', 'r') as file:
    names = [name.strip() for name in file.readlines()]

print(names)

# Create output letters
for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as output_file:
        output_file.write(personalized_letter)

