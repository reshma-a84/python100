# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Sample input Julie, Pari, Snow, Pups, Milky, Kunju, Millie, Timmy

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

total_name_count = len(names)
random_name = names[random.randint(0, total_name_count - 1)]

print(random_name + " is going to buy the meal today!")

#if random.choice() is used

random_name = random.choice(names)
print(random_name + " is going to buy the meal today!(with choice)")
