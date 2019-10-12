import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 8090))
while True:
     msg = input('>>>').strip()
     if msg:
       conn.send(msg.encode('utf-8'))
       msg = conn.recv(1024)
       print(msg.decode('utf-8'))