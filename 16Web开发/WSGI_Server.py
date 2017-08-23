# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from WSGI_py import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 命令行可以看到wsgiref打印的log信息
# 127.0.0.1 - - [22/Aug/2017 10:02:49] "GET / HTTP/1.1" 200 20
# 127.0.0.1 - - [22/Aug/2017 10:02:49] "GET /favicon.ico HTTP/1.1" 200 28
# 127.0.0.1 - - [22/Aug/2017 10:02:52] "GET /joey HTTP/1.1" 200 21
# 127.0.0.1 - - [22/Aug/2017 10:02:52] "GET /favicon.ico HTTP/1.1" 200 28