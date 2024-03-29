class User:
    def __init__(self, user_id, username):     # the init function is called everytime when a new object is created from this class
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def __repr__(self):
        pass


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Angela"

user_1 = User("001", "angela")
user_2 = User("002", "Jules")
print(user_1)
# print(user_1.id)
# print(user_1.username)
# print(user_1.follower)
# print(user_2.id)
# print(user_2.username)

user_1.follow(user_2)   # Here user1 is following user 2
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
