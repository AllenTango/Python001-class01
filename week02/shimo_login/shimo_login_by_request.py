import requests
from fake_useragent import UserAgent
from config import name, pwd

ua = UserAgent(verify_ssl=False)
# 随机选择 User-Agent ，random 是实例的属性
# Referer 说明你是从哪里来的
# x-requested-with 防止 crsf

headers = {
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest'
}

s = requests.Session()

login_url = 'https://shimo.im/login?from=home'

form_data = {
    'ck': '',
    'name': name,
    'password': pwd,
    'remember': 'true'
}

resp = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

print(resp.status_code)

# 验证登录是否成功，
resp = s.get('https://shimo.im/dashboard/favorites', headers=headers)
print(resp)
print(resp.text)
