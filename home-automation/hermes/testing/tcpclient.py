from socket import *

host = '192.168.178.31'#, "192.168.178.30" # set to IP address of target computer
port = 13333
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_STREAM)
name = 'server1'
UDPSock.connect(addr)
print('connected to ' + host)
msg = 'this is ' + name
UDPSock.send(bytes(msg, "utf-8"))
print('message sent.')
data = UDPSock.recv(1024)
print(data)
