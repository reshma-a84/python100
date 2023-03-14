#Simple Function
def greet():
    print ("Hello Julie!!")
    print ("How do you do Jack Bauer?")
    print ("How is everything?")

greet()

#Function with input arguments
def greet_with_name(name):
    print (f"Hello {name}, How are you")
    print (f"How do you do {name}?")

greet_with_name("Pari")

#Function with multiple input arguments
def greet_with(name, location):
    print (f"Hello {name}")
    print (f"How is {location}?")

greet_with("Pari","trichy")

#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")