# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S' or size == 's':
    bill = bill + 15
elif size == 'M' or size == 'm':
    bill = bill + 20
elif size == 'L' or size == 'l':
    bill += 25

if add_pepperoni == 'Y' or add_pepperoni =='y':
    if size in ['S','s']:
        bill += 2
    elif size in ['M','m''L','l']:
        bill += 3

if extra_cheese in ['Y','y']:
    bill += 1

print(f'Your final bill is: {bill}')