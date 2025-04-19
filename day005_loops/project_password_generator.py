import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '*', '^', '(', ')', '-', '+', '=']

print("Welcome to the PyPassword Generator!")

nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_symbols = []

for _ in range(nr_letter):
    password_symbols.append(random.choice(letters))

for _ in range(nr_symbols):
    password_symbols.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_symbols.append(random.choice(numbers))

random.shuffle(password_symbols)

final_pass = ""
for symbol in password_symbols:
    final_pass += symbol

print(f"Your password is {final_pass}")
