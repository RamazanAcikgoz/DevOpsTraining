# Describe the problem
# untangle the problem see what is exactly problem

def my_function():
    for i in range(1,20): #21 
        if i == 20:
            print("You got it")

my_function()


# Describe the problem - write your answers as comments: 
# 1. What is the for loop doing?
# 2. What is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i ?

# Caption 2 --> Reproduce the bug
# Caption 3 --> Play computer and evaluate each line :
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994: # year <= 1994
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")