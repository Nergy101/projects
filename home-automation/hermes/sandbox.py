from socket import *
host = '192.168.178.31'
port = 13000
buf = 1024
addr = ((host, port))
UDPSock = socket(AF_INET, SOCK_STREAM)
UDPSock.connect(addr)
msg = 'test'
UDPSock.send(bytes(msg, "utf-8"))
UDPsock.close()
