from wmain.autosave import WAutoSave, WSave
    
class D(WSave):
    def __init__(self):
        self.d = 4

class B(WSave):

    def __init__(self):
        self.b = 12
        self.d = D()
        
class Friend2(WSave):

    def __init__(self):
        self.score = 100

class Friend(WSave):

    def __init__(self):
        self.score = 100
        self.friend2 = Friend2()

class UserIni(WSave):

    def __init__(self):
        self.name = "user"
        self.age = 20
        self.gender = "male"
        self.friend = Friend()
        self.is_good = True
        self.friends = ["sb", "bb", "cc"]

if __name__ == '__main__':
    user = UserIni()
    user.name = "sb"
    user.bind_save_file("test_autosave.ini")
    print(user.friend.score)
    user.friend.score = 80
    user.friend.friend2.score = 90
    user.save()