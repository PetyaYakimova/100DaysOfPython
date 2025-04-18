states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

print(states_of_america[0])
print(states_of_america[2])
print(states_of_america[-1])

states_of_america[2] = "New York"
print(states_of_america[2])

states_of_america.append("Hawaii")
print(states_of_america)

states_of_america.extend(["Ohio", "Colorado"])
print(states_of_america)
