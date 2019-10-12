# I/O多路复用
import selectors
import socket


def accept(sock, mask):
    conn, addr = sock.accept() # 得到连接对象conn
    conn.setblocking(False) # 设置为非阻塞
    sel.register(conn, selectors.EVENT_READ, read)# 把conn对象和对应的read方法注册到sel对象
    print(conn)

def read(conn, mask):
    try:
        msg = conn.recv(1024)
        if msg:
           conn.send(msg)
        else:
           sel.unregister(conn)# 如果收到的消息为空,注销conn对象,对于linux系统
    except ConnectionResetError as e:
       print(e)
       sel.unregister(conn)# 连接突然中断,注销conn对象,对于windows系统

sel = selectors.DefaultSelector() # 创建selectors对象
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建socket对象
sock.bind(('127.0.0.1', 8090))
sock.listen(100)
sock.setblocking(False) # 设置socket对象为非阻塞

sel.register(sock, selectors.EVENT_READ, accept)# 把sock对象和对应的accept方法注册到sel对象
while True:
      events = sel.select()# 监听已经注册的对象
      for key, mask in events:
            # sock = key.fileobj
            # data = key.data
            callback = key.data # 回调函数
            # print(callback)
            callback(key.fileobj, mask)# 调用回调函数