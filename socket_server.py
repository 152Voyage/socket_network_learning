import socket
#创建一个服务端对象，ipv4 tcp
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定服务端的ip和端口
server.bind(('127.0.0.1',8888))
# 设置等待连接队列的最大长度为5
server.listen(5)
print("server start listing")
#等待客户端
client_socket,client_address=server.accept()
print(f"client address is{client_address}")

#一次最多只接收客户端1024字节
data=client_socket.recv(1024)
print(f"客户端说:{data.decode('utf-8')}")