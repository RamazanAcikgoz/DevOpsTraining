# Dictionaries are known as associative arrays #hash
# instead of having index they have key
# Dictionaries are keys themselves need to be immutable so they cannot be change
# Dictionaries are dynamic
# Dictionaries values are mutabke

ages = {'kevin': 29, 'alex': 15, 'bob': 24}
print(ages['kevin']) #accessing value using key

ages['Ranczo'] = 32
print(ages) #adding new key value pair

# Deletion or pop will delete last item return the value
del ages['bob']

# Get
print(ages.get('Ranczo'))

# Keys & values
print(ages.keys())
print(ages.values())

# Dict function 
weights = dict(kevin=98, rocky=100)
print(weights) #converting list to dict

# Tuples into dictionaries
colors = dict([('RA', 'blue'), ('MA', 'black')])
print(colors) #converting tuple to dict