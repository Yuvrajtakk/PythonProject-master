class User:

    def __init__(self):
        print("new user is created.... ")



user_1 = User()
user_1.id = "101"
user_1.username = "Yuvraj tak"
print(user_1.username)

user_2 = User()
user_2.id = "102"
user_2.username = "Rohit"
print(user_2.username)


class Car:
    def __init__(self,seats):
        self.seats = seats

jeep = Car(5)
print(jeep.seats)

class Useer:
    def __init__(self, user_id, username):
        self.id =user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self,user):
        user.follower += 1
        self.following += 1

user_3 = Useer("101","Yuvraj")
user_4 = Useer("102","Vaidk")
user_5 = Useer("103","Shruti")
user_6 = Useer("104","Varshi")
print(user_3.username)
print(user_4.id)
print(user_5.username)
print(user_6.username)

user_3.follow(user_4)
print(user_3.follower)
print(user_3.following)
print(user_4.follower)
print(user_4.following)
