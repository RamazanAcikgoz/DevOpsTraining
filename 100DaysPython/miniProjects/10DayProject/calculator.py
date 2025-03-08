from os import system
import art

print(art.logo)

def sum(a, b):
    return a + b
def mul(a, b):
    return a * b
def sub(a, b):
    return a - b
def div(a, b):
    return a / b

operator_list = {
    '+': sum,
    '-': sub,
    '*': mul,
    '/': div,
}

#print(operator_list['*'](6,6))
def calculator():
    should_continue = True
    num_one = float(input("what's the first number? : "))

    while should_continue:
        for x in operator_list:
            print(x)
        choice = input("Pick an operation: ")
        num_two = float(input("what's the second number? : "))
        final_answer = operator_list[choice](num_one,num_two)
        print(f"{num_one} {choice} {num_two} = {final_answer}") 

        cont = input(f"Type 'y' to continue calculating with {final_answer}, or type 'n' to start a new calculation: ").lower()
    
        if cont == 'y':
            num_one = final_answer
        else:
            should_continue = False
            system('cls')
        calculator() # recursive


calculator()