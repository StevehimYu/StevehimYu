import time
import socket
import sendCommand
import openJson


def testConnect(server):
    firstData, addr = server.recvfrom(1024)
    if len(firstData) == 0:
        print("未连接")
    else:
        print("测试连接成功")
        return addr
        pass


def testToken(server, user_token, addr, users, token):
    # 开始检测
    print("开始检测:" + user_token.decode())
    if user_token.decode() not in token:
        print("该token不存在")
        server.sendto("/close".encode(), addr)
        # 如果不在，骂他
        server.sendto("Go away your mother f**k".encode('utf-8'), addr)
        # 把地址加到黑名单
        sendCommand.change_dict(3, addr, users)
    elif user_token.decode() in token:
        t_n = user_token.decode()
        print("通过该token")
        if token[t_n]["password"] == "":
            print("该用户无密码")
            server.sendto("/input passwd".encode(), addr)
            user_passwd, addr = server.recvfrom(1024)
            sendCommand.addPasswd(t_n, user_passwd, token)
            sendCommand.addAddr(t_n, addr, users, token)
            print("成功")
            pass
        else:
            print("有密码，正在检验")
            server.sendto("/passwd".encode(), addr)
            testPasswd(server, t_n, token, users)
def testPasswd(server, t_n, token, users):
    time.sleep(0.5);
    passwd, addr = server.recvfrom(1024)
    if passwd.decode() in token[t_n]["password"]:
        print("检验成功")
        server.sendto("成功进入，可输入消息".encode(), addr)
        sendCommand.addAddr(t_n, addr, users, token)
        sendCommand.addPasswd(t_n, passwd, token)
    else:
        server.sendto("Go away your mother f**k".encode('utf-8'), addr)
        sendCommand.change_dict(3, addr, users)