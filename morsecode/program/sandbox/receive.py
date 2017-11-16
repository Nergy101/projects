from socket import *

host = ""
port = 8989
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
UDPSock.bind(addr)

print('waiting for replies')
(data, addr) = UDPSock.recvfrom(buf)
print('recieved the deets')
data = str(data)
addr = str(addr)
print(data)
