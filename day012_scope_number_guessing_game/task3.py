enemies = 1


# To modify a global variable in a local scope
def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Correct way to modify a global variable
def increase_correctly():
    return enemies + 1


enemies = increase_correctly()
print(f"Enemies outside edited: {enemies}")
