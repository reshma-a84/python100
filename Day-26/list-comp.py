# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
# # Output
# [2, 3, 4]

# The above can be achieved using list comprehension
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = 'Angela'
new_name = [letter for letter in name]
print(new_name)


range_list = range(1,5)
new_range = [nr * 2 for nr in range_list]
print(new_range)

# or
range_list1 = [num * 2 for num in range(1,5)]
print(range_list1)

