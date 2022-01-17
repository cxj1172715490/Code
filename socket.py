# ------------------------------- 服务端---------------------------------------------------
import socket
import datetime

# 1、创建服务端套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定ip和端口号
address = ("192.168.26.51", 8088)
server_socket.bind(address)
# 3、设置监听
server_socket.listen(128)  # 128:表示最大等待连接数

while True:
    print("等待客户端连接...")
    # 4、等待客户端的连接请求
    new_socket, client_addr = server_socket.accept()
    print("连接到客户端的地址为：", client_addr)

    # 5、接收客户端传入数据
    rev_data = new_socket.recv(1024)  # 表示一次最多接受1024个字节
    if rev_data:
        print("接收到客户端的数据：", rev_data.decode(encoding="utf-8"))
        
        server_send_data = f"[{datetime.datetime.now()}]:{rev_data.upper().decode(encoding='utf-8')}"
        # 6、向客户端发送数据
        send_data = new_socket.send(server_send_data.encode(encoding="utf-8"))

        new_socket.close()
    else:
        break

# 7、关闭套接字连接
server_socket.close()

# --------------------------------------------客户端----------------------------------------------------
import socket

while True:
    # 1、创建套接字服务对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、绑定服务端的ip和端口号
    address = ("192.168.26.51", 8088)
    client_socket.connect(address)
    client_data = input('> ')
    if client_data:
        # 3、向服务端发送数据
        client_socket.send(client_data.encode(encoding="utf-8"))

        # 4、接受到来自服务端的数据
        recv_data = client_socket.recv(1024)
        print("接收到服务端返回的数据：", recv_data.decode(encoding="utf-8"))
    else:
        break

# 5、关闭套接字连接
client_socket.close()
