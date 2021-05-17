import socket
def socket_():
    # 定义socket对象
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # ip,端口
    ip_port = ('127.0.0.1', 50665)
    # 服务器名称
    server_name = "server"
    # 绑定
    server.bind(ip_port)
    return server