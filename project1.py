class user():
    user_name=[]
    user_number=0

    def __init__(self, user_name, user_family, user_password, user_age):

        self.name=user_name
        self.family=user_family
        self.age=user_age
        self.password=user_password
        user.user_name.append(user_name)
        user.user_number +=1
        print(f"welcome {self.name} joon")

    for key, value in user_name:
        print(f'{key == range(1,100)} : {value} ')

    def logUot(self):
        user.user_number -=1
        user.user_name.remove(self.name)
        print(f"{self.name} logged out")
    def show_full_name(self):
        print(f"{self.name}{self.family}")

    def Computing_year_age(self):
        return 2021 - self.age


user1=user("ali","yousefi",1234,22)