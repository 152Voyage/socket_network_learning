import socket
import time
#创建客户端对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',7777))

#TCP 默认会把两次小的 send 合并成一个 TCP 数据包发送（Nagle 算法）。
# 所以服务端一次 recv 就收到了全部数据。
#我们需要延时来服务端只调用一次 recv(1024)，但客户端发两次数据

client.send("hello tcp/ip".encode('utf-8'))
time.sleep(0.1)  # 等待100毫秒，强制TCP分包
client.send("hi".encode('utf-8'))