import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

# Creating a data frame from the above dictionary values
print(pandas.DataFrame(data_dict)) # it creates a table from the above dictionary

# Output
# ======
#   students  scores
# 0      Amy      76
# 1    James      56
# 2   Angela      65

# Convert the data into CSV file
data = pandas.DataFrame(data_dict)
data.to_csv("sample.csv")


