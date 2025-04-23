alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):
    result = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += letter
    print(f"Here is the {direction}d result: {result}")


should_continue = 'yes'

while should_continue == 'yes':
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(direction=command, original_text=message, shift_amount=shift)
    should_continue = input("Do you want to go again? Write 'yes' or 'no'\n")

print("Goodbye!")
