def testPasswd(sock, addr):
    Command ,addr= sock.recvfrom(1024)
    if Command.decode() == "/input passwd":
        test_passwd = input("第一次进入，请你输入初始密码:")
        sock.sendto(test_passwd.encode(), addr)
    elif Command.decode() == "/passwd":
        test_passwd = input("请输入密码:")
        sock.sendto(test_passwd.encode(), addr)
    elif Command.decode() == "/close":
        exit()
    else:
        print(Command)