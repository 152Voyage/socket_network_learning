import socket

# 创建一个服务端对象，ipv4 tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定服务端的ip和端口
server.bind(('127.0.0.1', 7777))
# 设置等待连接队列的最大长度为5
server.listen(5)
print("server start listing")
# 等待客户端
client_socket, client_address = server.accept()
print(f"client address is{client_address}")

# 无限循环，一直接收数据
while True:
    data = client_socket.recv(1024)

    # 如果收到空字节，说明客户端断开连接
    if not data:
        print("客户端断开连接")
        break

    print(f"客户端说:{data.decode('utf-8')}")

# 关闭连接
client_socket.close()
server.close()