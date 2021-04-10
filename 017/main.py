# Quiz project Udemy day 17 My day 8
import uuid

class User:
    def __init__(self, user_id, username):
        print("New User Created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, who):
        who.followers += 1
        self.following += 1


user = User(uuid.uuid4(), "Dave")
user2 = User(uuid.uuid4(), "Bailey")
# print(user.username)
# print(user.id)
# print(user2.username)
# print(user2.id)
user.follow(user2)
print(user.following)
print(user.followers)
print(user2.following)
print(user2.followers)


