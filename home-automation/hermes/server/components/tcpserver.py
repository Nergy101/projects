from socket import *

class receive:
    def __init__(self):
        pass

    def receive(self, msg):
        host = ""
        port = 13333
        buf = 1024
        addres = (host, port)
        TCPsock = socket(AF_INET, SOCK_STREAM)
        TCPsock.bind(addres)
        TCPsock.listen(10)
        name = 'SERVER1'
        while True:
            c, addr = TCPsock.accept()
            data = c.recv(buf)
            data = str(data)
            print('connection accepted from ' + repr(addr[0]))
            print(data[2:-1])
            # POSSIBLE message
            c.send(bytes(msg, "utf-8"))



