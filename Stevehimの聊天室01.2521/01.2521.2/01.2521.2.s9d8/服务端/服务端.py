import socket
import time
import json
import os
import sendCommand
import testThings
import exit_leave_list
from socket_ import socket_
import openJson
# 创建socket对象
server = socket_()
print("检测状态")

token, users = openJson.OJ()
while True:
    try:
        data, addr = server.recvfrom(1024)
        print(addr)
        print("开始检测地址")
        if addr in users["离线"]:
            userName = users["离线"][addr]
            # 改为在线
            sendCommand.change_dict(1, addr, users)
            # 广播
            print("欢迎" + userName + "回到聊天室")
        elif addr in users["在线"]:
            print("在线")
            userName = users["在线"][addr]
            exit_leave_list.recvMsg(server, data, users, addr, userName)
            continue
        elif addr in users["黑名单"]:
            # 骂人
            server.sendto("Go away your mother f**k".encode('utf-8'), addr)
        elif addr not in users["离线"] or users["在线"]:
            print("检测token")
            testThings.testToken(server, data, addr, users, token)
        else:
            print("有错误")


    except ConnectionResetError:
        print(ConnectionResetError)















    # 原代码
    '''
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
        elif data.decode() in token:
            t_n = data.decode()
            print("通过")
            if token[t_n]["password"] == "":
                server.sendto("/input passwd".encode(), addr)
            continue
        if data.decode() not in token[t_n]["password"]:
            print("jj")
        else:
            token_name = token[t_n]['name']
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
    '''