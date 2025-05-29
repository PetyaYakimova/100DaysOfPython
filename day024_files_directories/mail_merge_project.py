PLACEHOLDER = "[name]"

with open("./names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

for name in names:
    stripped_name = name.strip()
    letter = starting_letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./ready_to_send/{stripped_name}_letter.txt", mode="w") as file:
        file.write(letter)
