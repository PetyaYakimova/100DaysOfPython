import random
import my_module

print(f"The number from my module is: {my_module.my_favourite_number}")

random_integer = random.randint(1, 10)
print(f"Random integer: {random_integer}")

random_float_0_to_1 = random.random()
print(f"Random float between 0 and 1: {random_float_0_to_1}")

random_float = random.uniform(2.5, 5.6)
print(f"Random float with given boundaries: {random_float}")
