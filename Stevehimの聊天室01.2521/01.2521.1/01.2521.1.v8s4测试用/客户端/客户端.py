import socket
import threading
import time

def send(sock, addr):
    while True:
        string = input()
        message = string
        sock.sendto(message.encode("utf-8"), addr)
        if string == "/exit":
            break
        if string == "/leave":
            break

def recv(sock, addr):
    sock.sendto(token.encode(), addr)
    sock.sendto(password.encode(), addr)
    while True:
        data = sock.recv(1024)
        if data.decode('utf-8') == "/input passwd":
            password = input("请您设置您的密码:")
        else：
            print(data.decode("utf-8"))


try:
    with open('token.json') as f_obj:
        token = json.load(f_obj)
except FileNotFoundError:
    os.system("u_a_t.py")
    with open('token.json') as f_obj:
        token = json.load(f_obj)


host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("219.150.218.20", 44605)
password = input("请您设置您的密码:")
tr = threading.Thread(target=recv, args=(host,server), daemon=True)
ts = threading.Thread(target=send, args=(host,server))
tr.start()
ts.start()
ts.join()
host.close()