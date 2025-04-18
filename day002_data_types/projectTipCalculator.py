print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_per_person = bill * (100 + tip_percentage) / 100 / people
print(f"Each person should pay: ${round(total_per_person, 2)}")
