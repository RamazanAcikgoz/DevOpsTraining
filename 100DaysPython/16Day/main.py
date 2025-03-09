# Documentation https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
# PyPi https://pypi.org/project/prettytable/



from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Name", ["Electric", "Water", "Fire"])

print(table)