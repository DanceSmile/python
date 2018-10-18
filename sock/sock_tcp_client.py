'''
tcp
一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
'''

# 导入
import socket
# 创建socket socket.AF_INET表示ipv4协议　　socket.SOCK_STREAM表示tcp连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        print("close")
        # 退出循环
        break

# 数据获取，header和body
data = b''.join(buffer)
header, html = data.split(b'\r\n\r\n',1)

# 写入文件
with open('./baidu.html','wb') as f:
    f.write(html)
s.close()
