# Fix the errors : 
# Fix any errors (red underlines) that show up in the editor
# before you run your code. The warnings (yellows) are optional fixes

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a an invalid number. Please try againg with a numerical response such as 15.")
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}")