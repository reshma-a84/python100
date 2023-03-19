class User:
    def __init__(self, userid):
        self.id = userid    # Constructor used to initialize the attribute

    def print_userid(self):
        print(f"Userid{self.id} ")


usr = User(id)     # passing parameter to Class is important
itr = int(input("How many iterations do you want? : "))
i = 0
while i < itr:

    usr.id = i + 1
    usr.print_userid()
    i += 1
