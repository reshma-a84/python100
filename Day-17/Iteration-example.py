class User:
    def __init__(self, userid):
        self.id = userid

    def print_name(self, userid):
        self.id = userid
        print(f"Userid{self.id} ")


usr = User(id)     # passing parameter to Class is important

i = 0
while i < 5:

    usr.id = i + 1
    usr.print_name(usr.id)
    i += 1
