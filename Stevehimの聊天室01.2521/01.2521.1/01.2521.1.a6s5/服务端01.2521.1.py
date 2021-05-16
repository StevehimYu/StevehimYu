import socket
import time
#定义socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ip,端口
ip_port = ('127.0.0.1',50665)
#服务器名称
server_name = "server"
#绑定
server.bind(ip_port)
print("监听并等待连接中......")
users = {
    "在线":{},
    "离线":{}
}
token = {}

def broadcasting(msg):
    '''
    负责给所有用户发出广播
    '''
    for address in users["在线"]:
        try:
            #给所有用户广播
            server.sendto(msg.encode(), address)
        except ConnectionResetError:
            #报错后将该地址添加到离线字典中
            print("1_有错误")
            users["离线"][addr] = users["在线"][addr]
            #从在线用户字典删除
            del users["在线"][addr]
def server_send_recrod(msg):
    '''
    接受msg并打印
    可以让服务端看见消息
    发送提示
    '''
    print(msg)
    broadcasting(msg)
    chat_record(msg)

def chat_record(string):
    record_file = open('D:\history\chat_history.txt', 'a')
    record_file.write(string + "\n")
    record_file.close()
while True:
    try:
        data, addr = server.recvfrom(1024)
        if data in token:
            if addr in users["离线"]:
                # 改为在线
                users["在线"][addr] = users["离线"][addr]
                # 广播
                print("欢迎" + data.decode("utf-8") + "回到聊天室")
            if addr not in users["在线"] or users["离线"]:
                #欢迎标语
                enter_msg = time.asctime() + '\n' + data.decode() + "进入聊天室."
                #广播到所有用户
                server_send_recrod(enter_msg)
                #加入用户字典
                users["在线"][addr] = data.decode("utf-8")
                print(users["在线"])
                continue
            #检测状态
            #是否退出
            elif "/exit" in data.decode("utf-8"):
                #广播
                exit_msg = time.asctime() + "\n" + users[addr] + "退出了聊天室"
                server_send_recrod(exit_msg)
            #在线用户列表
            elif "/list" in data.decode("utf-8"):
                #遍历在线用户字典
                for user in users["在线"].keys():
                    list_msg = (users["在线"][user] + ':' + user[0] + ':' + str(user[1])).encode()
                    #发送信息
                    print(users["在线"])
                    server.sendto(list_msg, addr)
            #进入离线状态
            elif "/leave" in data.decode("utf-8"):
                #添加到离线用户字典
                users["离线"][addr] = users["在线"][addr]
                #从在线用户字典删除
                del users["在线"][addr]
                #广播离线信息
                leave_msg = time.asctime() + "\n" + users[addr] + "暂时离开了聊天室"
                server_send_recrod(leave_msg)
                print(users["在线"])
            else:
                #普通发言,广播
                msg = time.asctime() + "\n" + data.decode("utf-8")
                server_send_recrod(msg)
        else:
            server.sendto("Go away your mother f**k".encode('utf-8'), addr)

    except ConnectionResetError:
        print(ConnectionResetError)