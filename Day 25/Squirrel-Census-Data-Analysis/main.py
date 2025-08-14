import pandas

from main_maheen import gray_squirrel, cinnamon, fur_data

census = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250814.csv")

gray_squirrels = len(census[census["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(census[census["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(census[census["Primary Fur Color"] == "Black"])

fur_data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels, cinnamon_squirrels, black_squirrels]
    }

df = pandas.DataFrame(fur_data_dict)
df.to_csv("Fur Color.csv")