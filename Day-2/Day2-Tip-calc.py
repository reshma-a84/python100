#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line
print("Welcome to the tip calculator")
total = input("What was the total bill? : $")
percent = input("How much '%' is the tip? :")
people = input("Split between ?: ")

tip_as_percent = int(percent) / 100
total_tip_amt = int(total) * tip_as_percent
total_bill = float(total) + float(total_tip_amt)
bill_per_person = total_bill / int(people)
final_amt = round(bill_per_person, 2)
final_amt = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amt}")

