
# Convert temps in dictionary from Celsius to Fahrenheit
weather = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
result = {k: v * 1.8 + 32 for (k, v) in weather.items()}
print(result)
