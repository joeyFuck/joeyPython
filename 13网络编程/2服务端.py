import socket
import threading
import time

# 为下文对连接的处理 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1) # 很关键,不然资源一会儿就耗完了
        if not data or data.decode('utf-8') == 'exit':
            break  # 没有数据发送过来或者发送的是exit,则break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 一 创建连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 二 绑定端口:
s.bind(('127.0.0.1', 9999))  # 因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
# 三 监听端口
s.listen(5) # 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
print('Waiting for connection...')
while True: # 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()





