programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary["Loop"] = "The action of doing something oer and over again."

empty_dictionary = {}

programming_dictionary["Bug"] = "A moth in your computer"

# print ("Prinitng keys")
# for thing in programming_dictionary:
#     print(thing)

for key in programming_dictionary:
    print(key)              # this prints the key
    print(programming_dictionary[key])  # this prints the value
    print(key + " " + programming_dictionary[key]) #this prints the key and the value