class User:
    # To initialize attributes - make a constructor
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_1.followers = 15
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "Pamela")
print(user_2.username)
print(user_2.followers)
user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)
