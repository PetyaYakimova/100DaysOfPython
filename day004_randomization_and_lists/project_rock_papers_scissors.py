import random

options = ["Rock", "Paper", "Scissors"]

player_choice = int(input(f"What do you choose? Type 0 for {options[0]}, 1 for {options[1]} and 2 for {options[2]}. "))

computer_choice = random.randint(0, 2)
print(f"Computer chose {[options[computer_choice]]}")

if player_choice >= 3 or player_choice < 0:
    print("You chose wrong number")
elif computer_choice == player_choice:
    print("Draw")
elif computer_choice == 0:
    if player_choice == 1:
        print("You win")
    else:
        print("You loose")
elif computer_choice == 1:
    if player_choice == 2:
        print("You win")
    else:
        print("You loose")
elif computer_choice == 2:
    if player_choice == 0:
        print("You win")
    else:
        print("You loose")
