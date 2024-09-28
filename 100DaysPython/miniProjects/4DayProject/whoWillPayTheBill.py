import random

friends = ["Anita", "Marta", "Ranczo", "Weronika"]


winner = random.randint(0,len(friends)-1)
print(friends[winner])

# Choice option
print(random.choice(friends))

# Nested lists:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
