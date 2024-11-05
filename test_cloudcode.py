from wmain.requests import WSession
from wmain.api.cloud_code import api_cloudcode
s = WSession()
s.ini.set_proxy(7890)
r = s.get("https://cas.jlu.edu.cn/tpass/code")
print(api_cloudcode.Post4_by_base64("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"))
print(api_cloudcode.Post4("captcha.jpeg"))
f = open("captcha.jpeg", "rb").read()
print(api_cloudcode.Post4_by_bytes(f))