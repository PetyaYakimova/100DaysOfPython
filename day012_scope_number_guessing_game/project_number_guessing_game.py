import random

EASY_TRIES = 10
HARD_TRIES = 5
NUMBER = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num_guesses = 0
if difficulty == 'easy':
    num_guesses = EASY_TRIES
else:
    num_guesses = HARD_TRIES

has_won = False
while num_guesses > 0 and not has_won:
    print(f"You have {num_guesses} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number == NUMBER:
        print("You win!")
        has_won = True
    else:
        if guessed_number < NUMBER:
            print("Too low.")
        else:
            print("Too high.")
        print("Guess again")
        num_guesses -= 1

if not has_won:
    print(f"You lose! The number was {NUMBER}")
