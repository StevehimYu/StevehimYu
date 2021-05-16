import socket
import threading

def send(sock, addr):
    while True:
        string = input()
        message = name + ":" + string
        sock.sendto(message.encode("utf-8"), addr)
        if string == "/exit":
            break
        if string == "/leave":
            break

def recv(sock, addr):
    sock.sendto(name.encode("utf-8"), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))

name = input("name:")
host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("219.150.218.20", 44605)
tr = threading.Thread(target=recv, args=(host,server), daemon=True)
ts = threading.Thread(target=send, args=(host,server))
tr.start()
ts.start()
ts.join()
host.close()