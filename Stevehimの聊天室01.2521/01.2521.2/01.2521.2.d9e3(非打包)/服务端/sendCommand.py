import socket
import time
import openJson
import time
def broadcasting(msg, server, users):
    """
    负责给所有用户发出广播
    """
    for address in users["在线"]:
        try:
            msg_ = time.asctime() + '\n' + msg
            # 给所有用户广播
            server.sendto(msg_.encode(), address)
        except ConnectionResetError:
            # 报错后将该地址添加到离线字典中
            print("1_有错误")
            change_dict(2, address, users)

def server_send_recrod(msg, server, users):
    """
    接受msg并打印
    可以让服务端看见消息
    发送提示
    """
    print(msg)
    broadcasting(msg, server, users)
    chat_record(msg)

def chat_record(msg):
    record_file = open('D:\history\chat_history.txt', 'a')
    record_file.write(time.asctime() + '\n' + msg + "\n")
    record_file.close()

def change_dict(number,addr,users):
    if number == 1:
        users["在线"][addr] = users["离线"][addr]
        del users["在线"][addr]
    elif number == 2:
        users["离线"][addr] = users["在线"][addr]
        del users["在线"][addr]
    elif number == 3:
        users["黑名单"][addr] = addr
    else:
        print("错误")

def addAddr(t_n, addr, users, token):
    users["在线"][addr] = token[t_n]["name"]
    print(users)
def addPasswd(t_n,user_passwd,token):
    token[t_n]['password'] = user_passwd.decode()
    openJson.dumpJson(token)