class Car:
    #     def __init__(self, **kw):
    #         self.make = kw["make"] #this is defined like a dictionary value
    #         self.model = kw["model"]
    #
    #
    # # my_car = Car(make="Nissan", model="GT-R")
    # my_car = Car(make="Nissan") # here we are not passing the value of model and thus the execution will produce and error. To overcome this we use the get method along with kw.
    #
    # print(my_car.model)
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
