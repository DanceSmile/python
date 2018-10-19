'''

'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'hello', ('127.0.0.1', 7777))

data = s.recv(1024)

print(data.decode('utf-8'))

s.close()

'''
UDP的使用与TCP类似，但是不需要建立连接。
此外，服务器绑定UDP端口和TCP端口互不冲突，
也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。
'''