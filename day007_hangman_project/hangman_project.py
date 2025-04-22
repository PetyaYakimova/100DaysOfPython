import random

words = ["camel", "bamboo", "baboon", "microphone", "apple"]
lives = 6

chosen_word = random.choice(words)
# print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()[0]

    is_correct_letter = False

    if guess not in correct_letters:
        display = ""
        for letter in chosen_word:
            if letter == guess:
                correct_letters.append(guess)
                is_correct_letter = True
                display += letter
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

    if not is_correct_letter:
        if guess in correct_letters:
            print(f"You have already tried the letter {guess}")
        else:
            print(f"You guessed {guess} and it is not in the word.")
        lives -= 1
        print(f"Lives left: {lives}/6")

    if lives <= 0:
        game_over = True
        print('You loose!')
    else:
        print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
