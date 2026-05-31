import socket
#创建客户端对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))
#向服务端发送
date="hello tcp/ip"
client.send(date.encode('utf-8'))