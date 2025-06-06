try:
    file = open("fake_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_real_key"])
except FileNotFoundError:
    file = open("fake_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
# If no exceptions were raised - then the else will be completed
else:
    content = file.read()
    print(content)
# Finally will be executed no matter if exceptions were raised or not
finally:
    file.close()
    print("File was closed")
