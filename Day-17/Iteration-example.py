class User:
    def __init__(self, userid):
        self.id = userid

    def print_userid(self, userid):
        self.id = userid
        print(f"Userid{self.id} ")


usr = User(id)     # passing parameter to Class is important
itr = int(input("How many iterations do you want? : "))
i = 0
while i < itr:

    usr.id = i + 1
    usr.print_userid(usr.id)
    i += 1
