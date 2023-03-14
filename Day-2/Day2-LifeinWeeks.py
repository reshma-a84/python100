# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = input("What is your current age? ")

years = 90 - int(age)

print(f"You have {years * 365} days, {years * 52} weeks, and {years * 12 } months left")