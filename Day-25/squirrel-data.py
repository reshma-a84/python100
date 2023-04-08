# Challenge for this program is to use the squirrel data from the csv file downloaded, extract the data using filter as "Primary Fur Color", count them accordingly and store it on another csv file

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinn_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

print(gray_squirrels)
gray_squirrels_count = len(gray_squirrels)
cinn_squirrels_count = len(cinn_squirrels)
black_squirrels_count = len(black_squirrels)
print(gray_squirrels_count)
print(cinn_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirrels_count, cinn_squirrels_count, black_squirrels_count]
}

# Convert the above datafram into csv file
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel-count.csv")