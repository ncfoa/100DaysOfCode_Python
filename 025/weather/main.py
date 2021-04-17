
# My way:
# weather_data = []
# with open("./weather_data.csv", "r") as f:
#     csv = f.read()
#     csv_list = csv.split("\n")
#     f.close()
#     for i in csv_list:
#         i_s = i.split(",")
#         weather_data.append(i_s)
#     weather_data.pop(0)
#     temps = []
#     for i in weather_data:
#         temps.append(int(i[1]))
# print(weather_data)
# print(temps)

# Instructors way:
# import csv
#
# with open("./weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#           temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

# Instructor showing pandas
import pandas
data = pandas.read_csv("./weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"].tolist())
# temp_total = 0
# avg = sum(data["temp"].tolist()) / len(data["temp"].tolist())
# max_temp = data["temp"].max()
# print(int(avg))
# print(max_temp)
#
# print(data[data.temp == data.temp.max()])
#
print(data.temp * 1.8 + 32)
