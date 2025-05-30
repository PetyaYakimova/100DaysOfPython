import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

# Calculate average temperature in 2 ways
avg_temp = sum(data_list) / len(data_list)
print(avg_temp)
print(data["temp"].mean())

print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
# Get the day with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = monday.temp[0]
print(f"Monday temp: {monday_temp}")
