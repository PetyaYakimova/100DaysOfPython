capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested lists in dictionaries
travel_log = {
    "France": ["Paris", "Strasbourg"],
    "Germany": ["Berlin", "Munich", "Stuttgart"]
}
print(travel_log["France"][1])

# Nested list in a list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested dictionary in a dictionary
new_travel_log = {
    "France": {
        "num_times_visited": 2,
        "cities_visited": ["Paris", "Strasbourg"],
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Berlin", "Munich", "Stuttgart"]
    },
}
print(new_travel_log["France"]["num_times_visited"])
print(new_travel_log["Germany"]["cities_visited"][2])
