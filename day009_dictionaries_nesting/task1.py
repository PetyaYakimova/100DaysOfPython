programming_dictionary = {
    "Bug": "An error in a program, that prevents the program of running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(programming_dictionary["Bug"])

# Add new item in the dictionary
programming_dictionary["Dictionary"] = "Storing keys with values."
print(programming_dictionary.keys())
print(programming_dictionary)

# Redefine a value in the dictionary
programming_dictionary["Bug"] = "An issue."
print(programming_dictionary)

# Looping through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
