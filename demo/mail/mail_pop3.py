'''
Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。
'''

import poplib
from email.parser import Parser


# 输入邮件地址, 口令和POP3服务器地址:
email = input('email: ')
password = input('password: ')
server = 'pop.qq.com'

# 连接到pop3服务器：
server = poplib.POP3(server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

# 身份验证
server.user(email)
server.pass_(password)

# list()返回所有邮件的编号:
response, mails, octets = server.list()
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index-1)
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

print( (msg.get("Subject",'').encode('utf-8')) )

server.quit()
