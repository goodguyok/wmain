from wmain.api import api_cjy
from wmain.requests import WSession

s = WSession()
s.ini.set_proxy(7890)
r = s.get("https://cas.jlu.edu.cn/tpass/code")
print(api_cjy.get_QR("captcha.jpeg"))
