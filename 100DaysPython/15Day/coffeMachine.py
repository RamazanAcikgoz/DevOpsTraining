# import resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

# TODO: 4. Check resources sufficient
def check_resources(order):
    """Check if there are enough resources to make the selected choice"""
    ingredients = MENU[order]["ingredients"]

    for item in ingredients:
        if ingredients[item] > resources.get(item, -0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Coin Operation
# Penny -> 1 cent (0.01$)
# Nickel -> 5 cents (0.05$)
# Dime -> 10 cents (0.10$)
# Quarter -> 25 cents (0.25$)
# TODO: 5. Process coins
def coin_calculator():
    """Returns the total calculated from inserted coins."""
    print("Please insert coins.")
    pennies = int(input("How many pennies?: ")) * 0.01
    nickels = int(input("How many nickels?: ")) * 0.05
    dimes = int(input("How many dimes?: ")) * 0.10
    quarters = int(input("How many quarters?: ")) * 0.25
    return quarters + dimes + nickels + pennies

# TODO: 6. Check if user inserted enough coin
def transaction_checker(coins, cost):
    """Checks if the coins is enough, updates profit, and offers change."""
    if coins < cost:
        print("Sorry, that's not enough money. Please insert more coins.")
        return coin_calculator()
    else:
        change = round(coins - cost, 2)
        money["value"] += cost  # Add earnings to machine
        if change > 0:
            print(f"Here is your ${change:.2f} in change.")
        print("Transaction successful!")
        return True  # Transaction successful

# TODO: 7. Deduction of resources and Make Coffee\
def deduct_resources(drink, menu, resources):
    """Deducts the required ingredients from resources after making a drink."""
    for items in menu[drink]["ingredients"]:
        resources[items] -= menu[drink]["ingredients"][items]

def make_coffe(drink):
    """Main function to process orders, check resources, handle payment, and serve coffee."""
    cost = MENU[drink]["cost"]
    print(f"The cost of {drink} is ${cost:.2f}")

    if not check_resources(drink):
        return "Not enough resource "

    payment = coin_calculator()  # Get user's money
    if transaction_checker(payment, cost):  # If transaction is successful
        deduct_resources(drink, MENU, resources)  # Deduct ingredients
        print(f"Here is your {drink}. Enjoy! ☕")

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):
# The prompt should show again to serve the next customer
is_on = True
coin_amount = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off machine
    if choice == "off":
        is_on = False
    # TODO: 3. Print report
    elif choice == "report": # current resources
        for item in resources:
            unit = "ml" if item in ["water", "milk"] else "gr"
            print(f"{item.capitalize()}: {resources.get(item)}{unit}")
        print(f"Money: ${money.get('value')}")
    elif choice == "espresso":
        make_coffe(choice)
    elif choice == "latte":
        make_coffe(choice)
    elif choice == "cappuccino":
         make_coffe(choice)
    else:
        print("Please correct choice")