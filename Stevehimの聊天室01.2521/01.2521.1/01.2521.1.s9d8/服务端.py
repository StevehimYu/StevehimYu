import socket
import time
import json
import os

# 定义socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip,端口
ip_port = ('127.0.0.1', 50665)
# 服务器名称
server_name = "server"
# 绑定
server.bind(ip_port)
print("监听并等待连接中......")

try:
    with open('users.json') as f_obj:
        users = json.load(f_obj)
    with open('token.json') as f_obj:
        token = json.load(f_obj)
except FileNotFoundError:
    os.system("u_a_t.py")
    with open('users.json') as f_obj:
        users = json.load(f_obj)
    with open('token.json') as f_obj:
        token = json.load(f_obj)

def broadcasting(msg):
    """
    负责给所有用户发出广播
    """
    for address in users["在线"]:
        try:
            # 给所有用户广播
            server.sendto(msg.encode(), address)
        except ConnectionResetError:
            # 报错后将该地址添加到离线字典中
            print("1_有错误")
            users["离线"][addr] = users["在线"][addr]
            # 从在线用户字典删除
            del users["在线"][addr]


def server_send_recrod(msg):
    """
    接受msg并打印
    可以让服务端看见消息
    发送提示
    """
    print(msg)
    broadcasting(msg)
    chat_record(msg)


def chat_record(string):
    record_file = open('D:\history\chat_history.txt', 'a')
    record_file.write(string + "\n")
    record_file.close()


def change_dict(number):
    if number == 1:
        users["在线"][addr] = users["离线"][addr]
        del users["在线"][addr]
    elif number == 2:
        users["离线"][addr] = users["在线"][addr]
        del users["在线"][addr]
    else:
        print("错误")


while True:
    try:
        data, addr = server.recvfrom(1024)
        if addr in users["离线"]:
            # 改为在线
            change_dict(1)
            # 广播
            print("欢迎" + token_name + "回到聊天室")
        # 是否在黑名单内
        elif addr in users["黑名单"]:
            server.sendto("Go away your mother f**k".encode('utf-8'), addr)
        if addr not in users["在线"] or users["离线"]:
            # 发送的头数据是否在token字典里
            if data.decode() not in token:
                # 如果不在，骂他
                server.sendto("Go away your mother f**k".encode('utf-8'), addr)
                # 把地址加到黑名单
                users["黑名单"][addr] = data.decode()
            else:
                token_name = token[str(data.decode())]['name']
            # 欢迎标语
            enter_msg = time.asctime() + '\n' + token_name + "进入聊天室."
            # 广播到所有用户
            server_send_recrod(enter_msg)
            # 加入用户字典
            users["在线"][addr] = token_name
            print(users["在线"])
            continue
        # 检测状态
        # 是否退出
        elif "/exit" in data.decode("utf-8"):
            # 广播
            exit_msg = time.asctime() + "\n" + token_name + "退出了聊天室"
            server_send_recrod(exit_msg)
        # 在线用户列表
        elif "/list" in data.decode("utf-8"):
            # 遍历在线用户字典
            for user in users["在线"].keys():
                list_msg = (users["在线"][user] + ':' + user[0] + ':' + str(user[1])).encode()
                # 发送信息
                print(users["在线"])
                server.sendto(list_msg, addr)
        # 进入离线状态
        elif "/leave" in data.decode("utf-8"):
            # 添加到离线用户字典
            change_dict(2)
            # 广播离线信息
            leave_msg = time.asctime() + "\n" + users["在线"][addr] + "暂时离开了聊天室"
            server_send_recrod(leave_msg)
            print(users["在线"])
        else:
            # 普通发言,广播
            msg = time.asctime() + "\n" + data.decode("utf-8")
            server_send_recrod(msg)


    except ConnectionResetError:
        print(ConnectionResetError)
