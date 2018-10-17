'''
和客户端编程相比，服务器编程就要复杂一些。
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
如果某个客户端连接过来了，
服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

accept()是接受新连接
listen()是进入监听状态，表示愿意接收连接请求。
listen之后有连接请求就将其放到队列中，accept()时把新连接请求从队列中取出，建立新的socket。
'''

# 导入
import socket
import threading
# 创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口
s.bind(('127.0.0.1', 8888))

# 开始监听端口,监听新的连接　 小于1024的端口号必须要有管理员权限才能绑定
s.listen(5)

print('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcp_link(sock, address):
    print("new treading for %s:%s" % address)
    sock.send(b'welcome')
    while True:
        # 最多接收1024
        data  = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('send message')
        # 发送数据到客户端
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # 断开连接
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # accept()会等待并返回一个客户端的连接
    sock, addr = s.accept()

    # 创建新的进程和客户端通讯
    t = threading.Thread(target=tcp_link, args=(sock,addr))
    t.start()

    print(socket, addr)



