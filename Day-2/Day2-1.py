# To show how prints with different data types
from hashlib import new

print("Hello")

print(12345)  # prints as is

print(123 + 345)  # prints as sum o 123 + 345 = 468

print("123" + "345")  # treats the lines as string and concatenates them

print(123_345_567)  # the "_" is used to make a large number readable. However the output is "123345567"

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# ===========================Exercise=====================================
num_char = len(input("What is your name : ? "))

# print("Your name has " + num_char + "characters.")   --> this line will throw the error TypeError: can only concatenate str (not "int") to str
# so you have to do type casting or type conversion

new_num_char = str(num_char)
print("num char is of data type :", type(num_char))
print("new_num_char is of data type : ", type(new_num_char))
print("Your name has " + new_num_char + " characters.")
