'''
Python对SMTP支持有smtplib和email两个模块
email负责构造邮件，smtplib负责发送邮件
'''

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import  MIMEMultipart
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr


def __format__ (s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input("From: ")
password = input("password: ")
to_addr = input('To: ')

# 构建消息

msg = MIMEMultipart()

msg['From'] = __format__('python love <%s>' % from_addr)
msg['To'] = __format__(' receive user <%s>' % to_addr)
msg['Subject'] = Header('python love ', 'utf-8').encode()

# plain 不表示纯文本，html表示网页
text_msg = MIMEText('hello world send from python <h1> html　</h1>', 'html', "utf-8")
msg.attach(text_msg)

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('./avatar.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)




smtp_server = 'smtp.qq.com'

# 导入
import smtplib


# 发送邮件
# 创建smtp服务
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)

# 用户登录
server.login(from_addr, password)

# 发送
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()