# Which line of code will print "Steak"?

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

# Option 1
print(order["main"][2])

# Option 2
print(order["dessert" - 1][2][0])

# Option 3
print(order["main"][2][0])          # Right answer

# Option 4
# print(order[main][2][0])

# Option 5
print(order["main"][1][0])