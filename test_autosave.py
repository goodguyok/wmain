from wmain.autosave import WAutoSave
    
class D(WAutoSave):
    def __init__(self):
        self.d = 4

class B(WAutoSave):

    def __init__(self):
        self.b = 12
        self.d = D()
        
class Friend2(WAutoSave):

    def __init__(self):
        self.score = 100

class Friend(WAutoSave):

    def __init__(self):
        self.score = 100
        self.friend2 = Friend2()

class UserIni(WAutoSave):

    def __init__(self):
        self.name = "user"
        self.age = 20
        self.gender = "male"
        self.friend = Friend()

if __name__ == '__main__':
    user = UserIni()
    user.name = "sb"
    user.bind_autosave("test_autosave.ini")
    print(user.friend.score)
    user.friend.score = 80
    user.friend.friend2.score = 90