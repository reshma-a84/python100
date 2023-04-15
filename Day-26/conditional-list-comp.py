# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Create a new list of names which is short that is 4 letters or less

short_name = [name for name in names if len(name) < 5]
print(short_name)


# if length of names is longer than 5 then convert them to uppercase
cap_name = [name.upper() for name in names if len(name) > 5]
print(cap_name)
