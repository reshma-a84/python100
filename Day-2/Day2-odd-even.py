# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))
result = number % 2

if result == 1:
    print (f"Number {number} is an odd number")
else:
    print (f"Number {number} is an even number")