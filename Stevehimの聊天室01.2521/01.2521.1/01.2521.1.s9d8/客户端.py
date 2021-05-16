import socket
import threading

token = "1h$3f&4w@2x]3q:3y&9j=3w!0g+2t!9e.6s[4d)8f!0"
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
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))


host = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("219.150.218.20", 44605)
tr = threading.Thread(target=recv, args=(host,server), daemon=True)
ts = threading.Thread(target=send, args=(host,server))
tr.start()
ts.start()
ts.join()
host.close()