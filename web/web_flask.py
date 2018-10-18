'''
更上一层的抽象框架flask
'''

from flask import  Flask
from flask import  request

app = Flask(__name__)

@app.route("/",methods =['GET', "POST"])
def home():
    return "home"

@app.route("/form")
def form():
    return '''
        <form action="/sign" method="post">
          <p><input name="username"></p>
          <p><input name="password" type="password"></p>
          <p><button type="submit">Sign In</button></p>
        </form>
    '''

@app.route('/sign',methods=['POST'])
def sign():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == "__main__":
    app.run(port=5002, debug=True)


'''
小结
有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数
这样，编写Web App就更加简单了。
在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的
Web框架都提供了自己的API来实现这些功能。
Flask通过request.form['name']来获取表单的内容。
'''