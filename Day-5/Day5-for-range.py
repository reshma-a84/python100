# for number in range(0, 10):  #range is not inclusive of the last number. So if you need to print 1 to 10 then range should be (1, 11)
#     print (number)

# for number in range(1, 11, 2):
#     print (number)

total = 0
for number in range(1, 101):
    total += number

print (total)
