import pandas

data = pandas.read_csv("./squirrel_census_data_2018.csv")

squirrel_dict = {
    "colors": ["gray", "cinnamon", "black"],
    "squirrels": [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]),
                  len(data[data["Primary Fur Color"] == "Black"])]}

print(squirrel_dict)
info = pandas.DataFrame(squirrel_dict)
info.to_csv("./squirrels.csv")

