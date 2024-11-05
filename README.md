# wmain 为化简操作而做的项目
## 一. 配置管理
```python
from wmain.autosave import WAutoSave
# 创建自己的参数类, 假设是账号, 密码, 邮箱
class Friend(WAutoSave):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class User(WAutoSave):

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.friend = Friend("friend_name", 20, "friend_address")

# 创建实例
user = User('admin', '123456', 'admin@example.com')
# 绑定文件
user.bind_autosave("user.json")
# 第一次运行输出 friend_name, 第二次运行输出 new_friend_name
print(user.friend.name)  
# bind之后的任何修改都可以改动到文件中
# 仅支持str, int, float, WAutoSave, 其他类型不会自动保存
user.username = "new_username"
user.password = "new_password"
user.email = "new_email"
user.friend.name = "new_friend_name"
```

## 二. requests中session的重新封装
```python
from wmain.requests import WSession
session = WSession()
session.ini.set_proxy(7890)
# 发送请求, 请求头已经随机携带
# 修改请求头
# session.ini.set_ua("mac")
# session.ini.set_ua("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
resp = session.get("https://www.baidu.com")
print(resp.status_code)
# 直接用xpath
elements = resp.xpath('//*[@class="title-content-title"]')
str_elements = resp.xpath_str('//*[@class="title-content-title"]')
# 打印xpath结果
print(elements)
print(str_elements)
# 更加方便的cookie导入, cookie_str请自己定义
session.load_cookies_str(cookie_str)
# 保存到文件, 方便下次导入cookie
session.save_cookies_file("cookies.txt")
# session.load_cookies_file("cookies.txt")
```
## 三. 多线程的封装
```python
from wmain.thread import WMultiThread, WLock
import time
# lock参数会自动传入, 最后一个参数必需有lock
def task(print_num, lock):
    lock.acquire()
    print(f"{print_num} has been printed")
    lock.release()
    time.sleep(1)
# 创建线程
thread = WMultiThread(8)
tasks = range(100)
thread.run(task, tasks)
# 等待所有线程结束
while thread.is_running:
    time.sleep(1)
print("All tasks have been finished")
```

