from game_data import data
import random


def format_data(account):
    """Takes the account data and returns it in a printable format"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"


score = 0
has_lost = False

print("Welcome to Higher or Lower game!")

a_choice = random.choice(data)
while not has_lost:
    b_choice = random.choice(data)
    while b_choice['name'] == a_choice['name']:
        b_choice = random.choice(data)

    print(f"Compare A: {format_data(a_choice)}")
    print('VS')
    print(f"Against B: {format_data(b_choice)}")

    user_choice = input('Who do you think has more followers? A or B? ').upper()

    # Clear the screen
    print("\n" * 20)

    correct_choice = 'B'
    if a_choice['follower_count'] > b_choice['follower_count']:
        correct_choice = 'A'

    if correct_choice == user_choice:
        score += 1
        print(f'You are right! Current score: {score}')
    else:
        has_lost = True
        print(f'You are wrong! Your final score is: {score}')
    a_choice = b_choice
