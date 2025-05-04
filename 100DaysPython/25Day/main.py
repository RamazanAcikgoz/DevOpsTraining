# Open csv file and add it into the list
# import csv

#with open("weather_data.csv") as csv_file:
#    days = [name.strip() for name in csv_file.readlines()]
#print(days)

# Or we can use csv library

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
#print(type(data))
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

# From pandas API documentation
print(data["temp"].mean())
# Max value
print(data["temp"].max())

# Get data in Columns
# Be aware "text" is capital sensitive it is apply for both line 39 and 40
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])

# Get high temp
print(data[data.temp == max(data.temp)])

tuesday = data[data.day == "Tuesday"]
print(tuesday.condition)

# Monday
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a datafame from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

# transfer data to csv file
data.to_csv("new_data.csv")