# Functions as Inputs
# def function_a(something):
#   Do this with something
#   Then do this
#   Finally do this
#
# def function_b():
#   Do this
#
# function_a(function_b)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2,3, add)
print(result)

#  Higher order function :
# It is a function which could work with other functions
# Calculator() function is a higher order function
