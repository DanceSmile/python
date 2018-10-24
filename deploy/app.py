from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "hello flask!"


if __name__ == '__main__':
    app.run(port=9000, debug=True)

'''
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:9090
# 指向网站目录
chdir = /home/zero/python3-webapp/deploy
# python 启动程序文件
wsgi-file = app.py
# python 程序内用以启动的 application 变量名
callable = app
# 处理器数
processes = 4
# 线程数
threads = 2
#状态检测地址
stats = 127.0.0.1:9191
socket = /tmp/flask.sock
'''

'''
server {
        listen    80;
        server_name  flask.test;

        location / {
                include uwsgi_params;
                uwsgi_pass unix:/tmp/flask.sock;
        }
 }
'''
