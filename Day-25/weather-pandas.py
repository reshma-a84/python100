import pandas

# print(pandas.read_csv("weather_data.csv.py")) # or
# Output
# ======
#          day   temp  condition
# 0     Monday     12      Sunny
# 1    Tuesday     14       Rain
# 2  Wednesday     15       Rain
# 3   Thursday     14     Cloudy
# 4     Friday     21      Sunny
# 5   Saturday     22      Sunny
# 6     Sunday     24      Sunny


data = pandas.read_csv("weather_data.csv.py")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

data_list = data['temp'].to_list()
print(len(data_list))

print(data["temp"].max()) # to print the max value in the temp column.

# Get Data in Columns
print(data["condition"])

# Alternative way to the above code is
print(data.condition) # works exactly of how the previous line works

# Get data in Row
print(data[data.day == "Wednesday"])

print(data[data.temp == data.temp.max()])

wed = data[data.day == 'Wednesday']
print(wed.condition)

# Convert the temp from Cel to F
wed_temp = int(wed.temp)
wed_temp_F = wed_temp * 9/5 + 32
print(wed_temp_F)

