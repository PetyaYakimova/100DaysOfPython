numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# List comprehension
# new_list = [new_item for item in list]
newer_list = [n + 1 for n in numbers]
print(newer_list)

name = "Name"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Donovan", "Elly"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
