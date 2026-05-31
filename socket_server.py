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

all_data=b""
#第一次接收的字节数量
data1=client_socket.recv(1024)
print(f"第一次接收的字节数量：{len(data1)}")
all_data+=data1
#第二次接收的字节数量
data2=client_socket.recv(1024)
print(f"第二次接收的字节数量：{len(data2)}")
all_data+=data2
#第三次接收的字节数量
data3=client_socket.recv(1024)
print(f"第三次接收的字节数量：{len(data3)}")
all_data+=data3

data=client_socket.recv(1024)
print(f"客户端说:{all_data.decode('utf-8')}")

