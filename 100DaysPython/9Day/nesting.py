# nesting 
#
# {
# Key : [List]
# Key2 : {Dict}
# }

capitals = {
    "Turkiye": "Ankara",
    "Poland": "Warsaw",
    "Japan": "Tokio"
}

travel_log = {
    "Turkiye": ["Istanbul", "Ankara", "Antalya"],
    "Poland": ["Warsaw", "Krakow", "Gdansk"],
}

print(travel_log["Turkiye"][1])

# Nested list: 
nested_list = ["A", "B", ["C","D"]]
print(nested_list[2][1]) # Output: D

visit_log = {
    "Turkiye": {
        "num_times_visited" : 30,
        "visited_cities" : ["Istanbul", "Ankara", "Antalya"]
    },
    "Poland": {
        "num_times_visited" : 20,
        "visited_cities" : ["Warsaw", "Krakow", "Gdansk"]
    },
}

print(visit_log["Poland"]["visited_cities"][2]) # Gdansk