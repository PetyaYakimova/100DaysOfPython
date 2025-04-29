enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global scope
player_health = 10


# Local scope - potion_strength can be used only inside function
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)


drink_potion()
print(player_health)
