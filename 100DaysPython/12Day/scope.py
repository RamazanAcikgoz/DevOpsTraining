enemies = 1 

def increase_enemies():
    # Local scope
    # Variables declared inside functions have local scope.
    # They are only seen by other code within the same block of code
    # Exists within function
    enemies = 2
    print(f"enemies inside function : {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope example
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)  # NameError: name 'potion_strength' is not defined

# Global scope : 
# Global scope is the scope where the variable is defined
# It is accessible from anywhere in the code
# Global variables are variables that are defined outside of any function or class in Python.
# They might be used in functions
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health) # It is possibble

drink_potion()

# Namespace 
# A namespace is a mapping from names to objects. 
# Namespaces are used to organize objects 