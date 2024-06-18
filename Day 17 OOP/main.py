class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0  # default
        self.following = 0  # default

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("101", "Rocky")
print(user1.id)

user2 = User("102", "John")
print(user2.username)

user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)
