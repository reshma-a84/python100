# Reading a file
# file = open("my_file.txt") or
# with open("my_file.txt") as file:    #using with you dont have to close the file using close() function
#     contents = file.read()
#     print(contents)
# file.close()


# Writing into a file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text111.")

with open("new_file.txt", mode="w") as file:
    file.write("Hello there new file")
