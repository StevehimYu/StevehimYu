import time
import sendCommand
import openJson
import time
def recvMsg(server, data, users, addr, userName):
    if data.decode() == "/exit":
        exit_command()
    elif data.decode() == "/list":
        list_command(server, users, addr)
    elif data.decode() == "/leave":
        leave_command(addr, users, userName, server)
    else:
        sendCommand.server_send_recrod(data.decode('utf-8') , server, users)

def exit_command():
    # 广播
    exit_msg = time.asctime() + "\n" + token_name + "退出了聊天室"
    server_send_recrod(exit_msg)

def list_command(server, users, addr):
    # 遍历在线用户字典
    for user in users["在线"].keys():
        list_msg = (users["在线"][user] + ':' + user[0] + ':' + str(user[1])).encode()
        # 发送信息
        print(users["在线"])
        server.sendto(list_msg, addr)
def leave_command(user_addr, users, userName, server):
    # 添加到离线用户字典
    sendCommand.change_dict(2, user_addr, users)
    # 广播离线信息
    leave_msg = time.asctime() + "\n" + userName + "暂时离开了聊天室"
    sendCommand.server_send_recrod(leave_msg, server, users)
    print(users["在线"])