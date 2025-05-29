file = open("my_file.txt")
contents = file.read()
print(contents)

file.close()

with open("my_file.txt") as file2:
    contents2 = file2.read()
    print(contents2)
