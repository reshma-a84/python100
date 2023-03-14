 #Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")

# a = two_digit_number[0]
# b = two_digit_number[1]
# c = int(a) + int(b)

#or 
c = int(two_digit_number[0]) + int(two_digit_number[1]) #shorter version of line 5,6 and 7

print(c)