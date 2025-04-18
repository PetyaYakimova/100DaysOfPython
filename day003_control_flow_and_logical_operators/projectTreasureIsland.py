print("Welcome to Treasure Island!")
direction = input("You are at a crossroads do you go left (L) or right(R)? ")

if direction == 'L':
    swim_wait = input("There is huge lake before you. Do you wish to swim (S) or wait (W)? ")
    if swim_wait == 'W':
        door = input(
            "Good choice. A few magical doors appear in front of you. Which one do you choose: yellow(Y), red(R), "
            "or blue(B)? ")
        if door == 'Y':
            print("You win!")
        else:
            print("You loose. Game over!")
    elif swim_wait == 'S':
        print("Crocodiles ate you. Game over!")
    else:
        print("You chose invalid option")
elif direction == 'R':
    print("You fell into a hole. Game over!")
else:
    print("You chose invalid direction")
