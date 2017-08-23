# 需安装Flask
# 处理3个URL，分别是：
#
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。
# 同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中
# Flask自带的Server在端口5000上监听： * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return  '<h3>Hello,admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()




