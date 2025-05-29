# If file doesn't exist and mode is "w" - file will be created
with open("new_file.txt", mode="w") as file:
    file.write("New text in new file.")
