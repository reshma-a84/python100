# Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# Option 1
# dict["c"] = [1,2,3]         #This will change the last key-value pair to hold a List. It's valid to have mided Types in the dictionary's values
# print(dict)


# # Option 2
# for key in dict:
#     dict[key] += 1
# print(dict)

# # Option 3
# dict[1] = 4
# print(dict)

# # Option 4
print(dict[1])       # Key Error . Here we have to mention only key values and the keys here are "a" "b" and "c"