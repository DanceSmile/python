'''
Model-View-Controller，中文名“模型-视图-控制器”
'''

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/sign", methods=["GET", "POST"])
def sign():
    username = request.form['username']
    return render_template("sign.html", username=username)

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")



app.run(debug=True, port=9000)

'''
有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。
'''