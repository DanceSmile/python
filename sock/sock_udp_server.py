'''
TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。
相对TCP，UDP则是面向无连接的协议

UDP协议不需要建立连接，只需要知道对方的IP地址和端口号
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 7777))


while True:
    data, address = s.recvfrom(1024)
    print('Received from %s:%s.' % address)
    s.sendto(b'Hello, %s!' % data, address)



# 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
