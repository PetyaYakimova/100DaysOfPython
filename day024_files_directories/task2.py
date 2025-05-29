# "w" more rewrites
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# "a" mode appends
with open("my_file.txt", mode="a") as file2:
    file2.write("More new text.")
