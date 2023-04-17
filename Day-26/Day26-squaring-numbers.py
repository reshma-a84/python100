numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# to write one line of code for squaring all the above numbers

# squared_numbers = [num * num for num in numbers]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
