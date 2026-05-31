import socket
#创建客户端对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8888))
#向服务端发送 一个哇是3字节，1000个就是三千字节
date="哇"*1000
client.send(date.encode('utf-8'))