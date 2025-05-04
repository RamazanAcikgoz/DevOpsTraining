import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_squirrel_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count"     : [gray_squirrel, black_squirrel, cinnamon_squirrel]
}

squirrel_data = pandas.DataFrame(data_squirrel_dict)

print(squirrel_data)
squirrel_data.to_csv("squirrel_data.csv")