'''
requests
Python第三方库，处理URL资源特别方便
'''

# 导入
import requests

# get访问
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)

# 带参数访问,　带header访问
r = requests.get('https://www.douban.com/search?source=suggest', params={'q':'python'}, header={})
# 获取最终请求地址
print(r.url)
# 获取编码
print(r.encoding)
# 获取bytes对象
print(r.content)
# 获取json
print(r.json)

# post 请求
r = requests.post('https://accounts.douban.com/login',data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params) # 内部自动序列化为JSON

# file上传
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post('url', files=upload_files)


# 获取头信息
r.headers
r.headers['Content-Type']

# 传入cookie请求
r = requests.get('url', cookies={'token': '12345', 'status': 'working'})
# 获取cookie
r.cookies
